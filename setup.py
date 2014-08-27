#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.install import install


def _post_install():
    pass


class ts_install(install):
    def run(self):
        install.run(self)

        self.execute(_post_install,
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
    cmdclass={'install': ts_install},  # override install
)
