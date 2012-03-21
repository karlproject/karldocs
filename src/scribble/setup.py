from setuptools import setup, find_packages

requires = [
    'pyramid',
    'redis',
    'Sphinx',
    'SQLAlchemy', # Undeclared (inexplicable) dependency of sphinx webapp support
    ]

tests_require = requires + [
    'mock',
    'WebTest']

setup(name='scribble',
      version='0.0',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=tests_require,
      test_suite="scribble",
      entry_points = """\
      [paste.app_factory]
      main = scribble:main
      [console_scripts]
      build_sphinx_web = scribble.build_sphinx_data:main
      """,
      )
