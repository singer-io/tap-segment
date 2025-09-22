

from setuptools import setup, find_packages


setup(name="tap-segment",
      version="0.0.1",
      description="Singer.io tap for extracting data from Segment API",
      author="Stitch",
      url="http://singer.io",
      classifiers=["Programming Language :: Python :: 3 :: Only"],
      py_modules=["tap_segment"],
      install_requires=[
        "singer-python==6.1.1",
        "requests==2.32.4",
        "parameterized"
      ],
      entry_points="""
          [console_scripts]
          tap-segment=tap_segment:main
      """,
      packages=find_packages(),
      package_data = {
          "tap_segment": ["schemas/*.json"],
      },
      include_package_data=True,
)
