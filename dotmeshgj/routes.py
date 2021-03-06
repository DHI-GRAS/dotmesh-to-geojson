from flask import Blueprint, request
from flask_cors import cross_origin

import dotmeshgj.schemas

bp = Blueprint("routes", __name__, url_prefix="/")


def _validate_dump(response, schema):
    serialized = schema.dump(response)
    errors = schema.validate(serialized)
    if errors:
        raise ValueError(errors)
    return serialized


def _parse_points(datalines):
    import numpy as np

    header = datalines[0]
    crs = header.split()[3]
    if crs.lower() not in ("long/lat", b"long/lat"):
        raise ValueError(f"Mesh must be LONG/LAT. Got {crs}.")
    nrows = int(header.split()[2])
    data = np.genfromtxt(
        datalines, dtype=float, skip_header=1, usecols=[1, 2], max_rows=nrows
    )
    if not np.isfinite(data).all():
        raise ValueError("Parsed data contains NaN")
    return data


def _mesh_to_polygon(points):
    import scipy.spatial
    import shapely.geometry

    hull = scipy.spatial.ConvexHull(points)
    return shapely.geometry.Polygon(points[hull.vertices])


def _polygon_to_geojson(polygon):
    import shapely.geometry

    return shapely.geometry.mapping(polygon)


@bp.route("/convert", methods=["POST"])
@cross_origin()
def convert():
    """Get convex hull of .mesh as GeoJSON
    ---
    post:
        summary: /convert
        description:
           Returns the convex hull of the mess as GeoJSON
        responses:
            200:
                description: Response
                schema: PolygonFeatureCollection
    """
    datalines = request.data.splitlines()
    if not len(datalines) > 1:
        return "Data was not a multi-line file", 400

    try:
        points = _parse_points(datalines)
    except ValueError as err:
        return str(err), 400
    polygon = _mesh_to_polygon(points)
    if not polygon.is_valid:
        return "Unable to get valid polygon from this mesh", 400
    geojson = _polygon_to_geojson(polygon)
    response = {
        "type": "FeatureCollection",
        "features": [{"type": "Feature", "geometry": geojson}],
    }
    return _validate_dump(response, dotmeshgj.schemas.PolygonFeatureCollection())
