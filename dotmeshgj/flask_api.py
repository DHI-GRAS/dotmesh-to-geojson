from flask import Flask
from flask_cors import CORS

from dotmeshgj.spec import spec_api, spec


def create_app(debug=False):
    from dotmeshgj import routes

    app = Flask(__name__)
    app.debug = debug
    CORS(app)
    app.register_blueprint(routes.bp)
    with app.test_request_context():
        spec.path(view=routes.convert)
    app.register_blueprint(spec_api)
    return app
