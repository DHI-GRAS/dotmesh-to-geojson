from marshmallow import Schema, validate
from webargs import fields


class Polygon(Schema):
    type = fields.Constant("Polygon", required=True, description="Object type")
    coordinates = fields.List(
        fields.List(fields.Tuple((fields.Float, fields.Float)), required=True),
        required=True,
        description="Coordinates",
        validate=validate.Length(min=1),
    )

    class Meta:
        ordered = True


class PolygonFeature(Schema):
    type = fields.Constant("Feature", required=True, description="Object type")
    geometry = fields.Nested(Polygon, many=False, required=True, description="Geometry")
    properties = fields.Dict(
        keys=fields.String, missing={}, description="Feature properties"
    )

    class Meta:
        ordered = True


class PolygonFeatureCollection(Schema):
    type = fields.Constant(
        "FeatureCollection", required=True, description="Object type"
    )
    features = fields.Nested(
        PolygonFeature, many=True, required=True, description="Features"
    )

    class Meta:
        ordered = True


class Point(Schema):
    type = fields.Constant("Point", required=True, description="Geometry type")
    coordinates = fields.List(
        fields.Float,
        validates=validate.Length(2),
        required=True,
        description="Point coordinates",
    )

    class Meta:
        ordered = True


class PointFeature(Schema):
    type = fields.Constant("Feature", required=True, description="Object type")
    geometry = fields.Nested(Point, many=False, required=True, description="Geometry")
    properties = fields.Dict(
        keys=fields.String(), missing={}, description="Feature properties"
    )

    class Meta:
        ordered = True


class PointFeatureCollection(Schema):
    type = fields.Constant(
        "FeatureCollection", required=True, description="Object type"
    )
    features = fields.Nested(
        PointFeature, many=True, required=True, description="Features"
    )

    class Meta:
        ordered = True
