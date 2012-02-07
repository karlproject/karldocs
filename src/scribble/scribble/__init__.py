import os

from pyramid.config import Configurator

from scribble.build_sphinx_data import build_sphinx_data
from scribble.models import SiteRoot


def main(global_config, **local_config):
    settings = global_config.copy()
    settings.update(local_config)
    sphinx_build = settings['sphinx_build']
    if not os.path.exists(sphinx_build):
        build_sphinx_data(settings)
    sphinx_data = os.path.join(sphinx_build, 'data')
    static_dir = os.path.join(sphinx_build, 'static')

    def get_root(request):
        return SiteRoot(sphinx_data)

    config = Configurator(root_factory=get_root, settings=settings)
    config.scan('scribble.views')
    config.add_static_view('static', static_dir)
    return config.make_wsgi_app()