#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.bdist_egg import bdist_egg as _bdist_egg


def _post_install():

    import os
    import sys
    from distutils.sysconfig import get_python_lib

    import setuptools
    print setuptools.__version__

    dest_dir = get_python_lib()

    packages = ['gobject', 'glib', 'pygst', 'pygst.pyc', 'pygst.pth',
                'gst-0.10', 'pygtk.pth', 'pygtk.py', 'pygtk.pyc']

    python_version = sys.version[:3]
    global_path = os.path.join('/usr/lib', 'python' + python_version)
    global_sitepackages = [os.path.join(global_path,
                                        'dist-packages'),  # for Debian-based
                           os.path.join(global_path,
                                        'site-packages')]  # for others

    for package in packages:
        for pack_dir in global_sitepackages:
            src = os.path.join(pack_dir, package)
            dest = os.path.join(dest_dir, package)
            if not os.path.exists(dest) and os.path.exists(src):
                os.symlink(src, dest)


class bdist_egg(_bdist_egg):
    def run(self):
        _bdist_egg.run(self)
        self.execute(_post_install, [],
                     msg="Running post install task")


CLASSIFIERS = [
    'Intended Audience :: Science/Research',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'Programming Language :: Python',
    'Programming Language :: JavaScript',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Multimedia :: Sound/Audio',
    'Topic :: Multimedia :: Sound/Audio :: Analysis',
    'Topic :: Multimedia :: Sound/Audio :: Players',
    'Topic :: Multimedia :: Sound/Audio :: Conversion',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ]

KEYWORDS = 'audio analysis features extraction MIR transcoding graph visualize plot HTML5 interactive metadata player'

setup(
    name = "TimeSide",
    url='https://github.com/yomguy/TimeSide/',
    description="open web audio processing framework",
    long_description=open('README.rst').read(),
    author="Guillaume Pellerin, Paul Brossier, Thomas Fillon, Riccardo Zaccarelli, Olivier Guilyardi",
    author_email="yomguy@parisson.com, piem@piem.org, thomas@parisson.com, riccardo.zaccarelli@gmail.com, olivier@samalyse.com",
    version='0.5.7',
    install_requires=[
        'numpy',
        'mutagen',
        'pillow',
        'h5py',
        'numexpr>=2.0.0',
        'tables',
        'pyyaml',
        'simplejson',
        'scipy',
        'matplotlib',
        'django>=1.4',
        'django-extensions',
        'djangorestframework',
        'south',
        ],
    platforms=['OS Independent'],
    license='Gnu Public License V2',
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    packages=['timeside'],
    include_package_data=True,
    zip_safe=False,
    scripts=['scripts/timeside-waveforms', 'scripts/timeside-launch'],
    cmdclass={'bdist_egg': bdist_egg},  # override bdist_egg
)
