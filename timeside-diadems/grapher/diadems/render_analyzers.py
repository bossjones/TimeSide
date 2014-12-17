# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2014 Guillaume Pellerin <yomguy@parisson.com>
# Copyright (c) 2013-2014 Thomas Fillon <thomas@parisson.com>

# This file is part of TimeSide.

# TimeSide is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# TimeSide is distributed in the hope that it will be useful,
# but _WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with TimeSide.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import division

from timeside.core import get_processor
from timeside.exceptions import PIDError

from timeside.grapher.render_analyzer import DisplayAnalyzer


# -------------------------------------------------
# From here define new Graphers based on Analyzers
# -------------------------------------------------

# IRIT 4Hz
irit4hz = get_processor('irit_speech_4hz')
Display4hzSpeechSegmentation = DisplayAnalyzer.create(
    analyzer=irit4hz,
    result_id='irit_speech_4hz.segments',
    grapher_id='grapher_irit_speech_4hz_segments',
    grapher_name='Speech segmentation',
    background='waveform')


# IRIT 4Hz with median filter
irit4hz = get_processor('irit_speech_4hz')
Display4hzSpeechSegmentation = DisplayAnalyzer.create(
    analyzer=irit4hz,
    result_id='irit_speech_4hz.segments_median',
    grapher_id='grapher_irit_speech_4hz_segments_median',
    grapher_name='Speech segmentation (median)',
    background='waveform')

# IRIT Monopoly
try:  # because of the dependencies on Aubio Pitch
    iritmonopoly = get_processor('irit_monopoly')
    DisplayMonopoly = DisplayAnalyzer.create(
        analyzer=iritmonopoly,
        result_id='irit_monopoly.segments',
        grapher_id='grapher_monopoly_segments',
        grapher_name='Mono/Poly segmentation',
        background='waveform')
except PIDError:
    pass

# Limsi SAD : 2 models
try:
    limsi_sad = get_processor('limsi_sad')

    DisplayLIMSI_SAD_etape = DisplayAnalyzer.create(
        analyzer=limsi_sad,
        analyzer_parameters={'sad_model': 'etape'},
        result_id='limsi_sad.sad_lhh_diff',
        grapher_id='grapher_limsi_sad_etape',
        grapher_name='Speech activity (ETAPE)',
        background='waveform')

    DisplayLIMSI_SAD_maya = DisplayAnalyzer.create(
        analyzer=limsi_sad,
        analyzer_parameters={'sad_model': 'maya'},
        result_id='limsi_sad.sad_lhh_diff',
        grapher_id='grapher_limsi_sad_maya',
        grapher_name='Speech activity (Mayan)',
        background='waveform')

except PIDError:
    pass

# IRIT Start Seg
irit_startseg = get_processor('irit_startseg')
DisplayIRIT_Start = DisplayAnalyzer.create(
    analyzer=irit_startseg,
    result_id='irit_startseg.segments',
    grapher_id='grapher_irit_startseg',
    grapher_name='Analogous start point',
    background='waveform')
