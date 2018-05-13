#!/usr/bin/env python3

import io
import os

from setuptools import setup, find_packages

with io.open('about.md', 'r', encoding='utf-8') as f:
    ABOUT = f.read()

NAME = 'Orange3-WONDER'

MAJOR = 0
MINOR = 0
MICRO = 30
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

AUTHOR = 'Luca Rebuffi, Paolo Scardi, Alberto Flor'
AUTHOR_EMAIL = 'paolo.scardi@unitn.ut'

URL = 'https://github.com/WONDER-project/Orange3-WONDER'
DESCRIPTION = 'Whole POwder PatterN MoDEl in Orange.'
LONG_DESCRIPTION = ABOUT
LICENSE = 'GPL3+'

CLASSIFIERS = [
    'Development Status :: 1 - Planning',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Programming Language :: Python :: 3 :: Only'
]

KEYWORDS = [
    'orange3 add-on',
    'orange3-wonder'
]

PACKAGES = find_packages()

PACKAGE_DATA = {
    'orangecontrib.xrdanalyzer.view.widgets': ['icons/*.*'],
    'orangecontrib.xrdanalyzer.view.widgets': ['icons/*.*'],
    'orangecontrib.xrdanalyzer.controller.fit.data': ['*.*', 'delta_l_files/*.*'],
}

NAMESPACE_PACAKGES = ["orangecontrib",
                      "orangecontrib.xrdanalyzer",
                      "orangecontrib.xrdanalyzer.view",
                      "orangecontrib.xrdanalyzer.view.widgets",
                      "orangecontrib.xrdanalyzer.view.untrusted",
                      ]

INSTALL_REQUIRES = sorted(set(
    line.partition('#')[0].strip()
    for line in open(os.path.join(os.path.dirname(__file__), 'requirements.txt'))) - {''})

ENTRY_POINTS = {
    'orange.widgets':
        ('WONDER = orangecontrib.xrdanalyzer.view.widgets',
         'WONDER - UNTRUSTED = orangecontrib.xrdanalyzer.view.untrusted',
         ),
    'orange3.addon':
        ('Orange3-WONDER = orangecontrib.xrdanalyzer',)



}

import shutil, sys

from distutils.core import setup
from distutils.extension import Extension

ext_modules=[
    Extension("orangecontrib.xrdanalyzer.controller.fit.wppm_functions",               ["orangecontrib/xrdanalyzer/controller/fit/wppm_functions.pyx"]),
    Extension("orangecontrib.xrdanalyzer.controller.fit.fitters.fitter_minpack",       ["orangecontrib/xrdanalyzer/controller/fit/fitters/fitter_minpack.pyx"]),
    Extension("orangecontrib.xrdanalyzer.controller.fit.fitters.fitter_minpack_util",  ["orangecontrib/xrdanalyzer/controller/fit/fitters/fitter_minpack_util.pyx"]),
]

from Orange.canvas.application.addons import PipInstaller

class Package:
    def __init__(self, package_url="", name=""):
        self.package_url = package_url
        self.name = name

def create_recovery():

    root_path = os.path.join("orangecontrib", "xrdanalyzer")
    recovery_root_path = os.path.join(root_path, "recovery")

    shutil.rmtree(recovery_root_path)
    os.makedirs(recovery_root_path)
    open(os.path.join(recovery_root_path,  "__init__.py"), 'a').close()

    for path, dirs, files in os.walk(root_path):
        recovery_path = os.path.join(recovery_root_path, path[26:])
        if not recovery_path.endswith("__pycache__"):
            if not os.path.exists(recovery_path):
                os.makedirs(recovery_path)

                if os.path.exists(os.path.join(path, "__init__.py")):
                    shutil.copyfile(os.path.join(path, "__init__.py"), os.path.join(os.path.join(recovery_path,  "__init__.py")))

            for file in files:
                if file.endswith(".pyx"):
                    shutil.copyfile(os.path.join(path, file), os.path.join(recovery_path,  file[:-1]))

if __name__ == '__main__':

    is_sdist = False
    for arg in sys.argv:
        if arg == 'sdist':
            is_sdist = True
            break

    if is_sdist:
        create_recovery()

    #########################################################
    # check if Chyton is present, in case it install it
    #########################################################

    if not is_sdist:
        try:
            from Cython.Distutils import build_ext
        except:
            try:
                pip = PipInstaller()
                pip.arguments.append("--no-warn-script-location")
                pip.install(Package(package_url="Cython"))
            except:
                pass


    try:
        from Cython.Distutils import build_ext

        setup(
            name=NAME,
            version=VERSION,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            url=URL,
            description=DESCRIPTION,
            long_description=LONG_DESCRIPTION,
            license=LICENSE,
            packages=PACKAGES,
            package_data=PACKAGE_DATA,
            keywords=KEYWORDS,
            classifiers=CLASSIFIERS,
            install_requires=INSTALL_REQUIRES,
            namespace_packages=['orangecontrib'],
            entry_points=ENTRY_POINTS,
            cmdclass = {'build_ext': build_ext},
            ext_modules = ext_modules,
        )
    except:
        #########################################################
        # in case of problems: restore full python installation
        # not cython files are replaced by recovery files generated
        # during sdist
        #########################################################

        setup(
            name=NAME,
            version=VERSION,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            url=URL,
            description=DESCRIPTION,
            long_description=LONG_DESCRIPTION,
            license=LICENSE,
            packages=PACKAGES,
            package_data=PACKAGE_DATA,
            keywords=KEYWORDS,
            classifiers=CLASSIFIERS,
            install_requires=INSTALL_REQUIRES,
            namespace_packages=['orangecontrib'],
            entry_points=ENTRY_POINTS
        )