import os
import shutil
from setuptools.command.build_ext import build_ext as build_ext_orig
from setuptools.extension import Extension
from setuptools import setup

class build_ext(build_ext_orig):
    def run(self):
        for ext in self.extensions:
            dst = os.path.join(os.path.dirname(self.get_ext_fullpath(ext.name)),
                               ext.name, '%s.so' % ext.name) 
            src = os.path.join(ext.name, '%s.so' % ext.name)
            shutil.copy(src, dst)

setup(
  name = 'onedatafs',
  ext_modules = [Extension('onedatafs', sources=[])],
  version='0.0.1',
  description='This is onedatafs compiled lib installed in a hackish way',
  author='Enol Fernández',
  packages=['onedatafs'],
  cmdclass={ 'build_ext': build_ext,},
  include_package_data=True)
