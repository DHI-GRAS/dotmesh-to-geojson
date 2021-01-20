from flask import jsonify, render_template, Blueprint

from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin

from typing import Any
from dotmeshgj import __version__

ma_plugin = MarshmallowPlugin()

spec_api = Blueprint("spec_api", __name__, url_prefix="/")

spec = APISpec(
    title=".mesh to GeoJSON converter",
    version=__version__,
    openapi_version="2.0",
    info=dict(
        description="Calculates the convex hull of a .mesh file and returns it as GeoJSON"
    ),
    plugins=[FlaskPlugin(), ma_plugin],
)


@spec_api.route("/swagger.json", methods=["GET"])
def specification() -> str:
    return jsonify(spec.to_dict())


@spec_api.route("/apidoc", methods=["GET"])
def ui() -> Any:
    return render_template("apidoc.html")
