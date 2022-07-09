from flask import Flask, Blueprint
from flask_cors import CORS
from flask_restful import Api

from utils import cache
from views import ProxiesAPI


def create_app(behind_proxy: bool = False):
    app = Flask(__name__)
    app.config.from_mapping({
        'CACHE_TYPE': 'SimpleCache',
        'CACHE_DEFAULT_TIMEOUT': 600, 
        'CACHE_THRESHOLD': 5,
    })
    app.url_map.strict_slashes = False
    api_blueprint = Blueprint('api', __name__, url_prefix='/api')
    api = Api(api_blueprint)
    api.add_resource(ProxiesAPI, '/proxies')
    app.register_blueprint(api_blueprint)
    cache.init_app(app)
    CORS(app, resources=r'/api/proxies/?', methods=['GET', 'OPTIONS'])

    if behind_proxy:
        from werkzeug.middleware.proxy_fix import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

    return app
