from setuptools import setup, find_packages

requires = [
    'pyramid',
    'Sphinx',
    ]

setup(name='scribble',
      version='0.0',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="scribble",
      entry_points = """\
      [paste.app_factory]
      main = scribble:main
      [console_scripts]
      build_sphinx_web = scribble.build_sphinx_data:main
      """,
      )
