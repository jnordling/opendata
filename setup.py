from setuptools import setup, find_packages

version = '0.1'

setup(name='opendata',
      version=version,
      description="ArcGIS Open Data API",
      long_description="Python bindings to the OpenData data.json",
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7'],
      keywords='OpenData Python API',
      author='Jon Nordling',
      author_email='jonnordling@gmail.com',
      url='https://github.com/onaio/onapie',
      license='MIT',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      test_suite='opendata',
      install_requires=['requests'],)