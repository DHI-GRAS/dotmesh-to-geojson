# dotmesh-to-geojson
Microservice to get the convex hull from a .mesh file

<a href="https://github.com/DHI-GRAS/dotmesh-to-geojson/actions?query=workflow%3APytest"><img src="https://github.com/DHI-GRAS/dotmesh-to-geojson/workflows/Pytest/badge.svg"></a>
[![codecov](https://codecov.io/gh/DHI-GRAS/dotmesh-to-geojson/branch/main/graph/badge.svg?token=WATJNK981X)](https://codecov.io/gh/DHI-GRAS/dotmesh-to-geojson)


## Usage

You can run this locally with 

```bash
pip install -e .
export FLASK_APP=dotmeshgj.app
export FLASK_ENV=development
flask run
```

API docs at `/apidoc`.

Just `POST` the bytes data from a .mesh file to the `/convert` endpoint and get a GeoJSON `FeatureCollection` with the convex hull.

Bad data should raise a 400 error (duh).


## Testing

```
pip install .[test]
pytest -v .
```
