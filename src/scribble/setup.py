from setuptools import setup, find_packages

requires = [
    'pyramid>=1.3a5',
    'pyramid_exclog',
    'waitress'
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
      """,
      )
