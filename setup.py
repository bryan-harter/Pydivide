#
#To upload the latest version, change "version=0.X.X+1" and type:
#    python setup.py sdist upload
#
#
#

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pydivide',
      version='0.2.9',
      description='A tool to plot MAVEN Key Parameter data',
      url='http://github.com/MAVENSDC/pydivide',
      author='MAVEN SDC',
      author_email='mavensdc@lasp.colorado.edu',
      license='MIT',
      keywords='tplot maven lasp idl divide',
      packages=['pydivide'],
      install_requires=['pytplot',
                        'netCDF4==1.2.7'], #1.2.8 will break the toolkit, check future versions
      include_package_data=True,
      zip_safe=False)