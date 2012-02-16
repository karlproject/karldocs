import os

from pyramid.config import Configurator

from scribble.build_sphinx_data import build_sphinx_data as build_sphinx
from scribble.models import SiteRoot


def main(global_config, **local_config):
    settings = global_config.copy()
    settings.update(local_config)
    sphinx_build = settings['sphinx_build']
    if not os.path.exists(sphinx_build):
        build_sphinx(settings)
    settings['sphinx_data'] = os.path.join(sphinx_build, 'data')
    static_dir = os.path.join(sphinx_build, 'static')

    def get_root(request):
        return SiteRoot(settings)

    config = Configurator(root_factory=get_root, settings=settings)
    config.scan('scribble')
    config.add_static_view('static', static_dir)
    config.add_static_view('scribble_static', 'scribble:static')
    return config.make_wsgi_app()
