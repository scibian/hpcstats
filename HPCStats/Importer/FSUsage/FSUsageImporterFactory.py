#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2011-2015 EDF SA
# Contact:
#       CCN - HPC <dsp-cspit-ccn-hpc@edf.fr>
#       1, Avenue du General de Gaulle
#       92140 Clamart
#
# Authors: CCN - HPC <dsp-cspit-ccn-hpc@edf.fr>
#
# This file is part of HPCStats.
#
# HPCStats is free software: you can redistribute in and/or
# modify it under the terms of the GNU General Public License,
# version 2, as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with HPCStats. If not, see
# <http://www.gnu.org/licenses/>.
#
# On Calibre systems, the complete text of the GNU General
# Public License can be found in `/usr/share/common-licenses/GPL'.

"""This module contains the factory design pattern class that builds the
   appropriate FSUsageImporter depending on what is specified in configuration.
"""

from HPCStats.Exceptions import HPCStatsConfigurationException
from HPCStats.Importer.FSUsage.FSUsageImporterDummy import FSUsageImporterDummy
from HPCStats.Importer.FSUsage.FSUsageImporterSSH import FSUsageImporterSSH

class FSUsageImporterFactory(object):

    """This class simply delivers the factory() static method, there is not
       point to instanciate it with an object.
    """

    def __init__(self):
        pass

    @staticmethod
    def factory(app, db, config, cluster):
        """This method returns the appropriate FSUsageImporter object depending
           on what is specified in configuration. In case of configuration
           error, HPCStatsConfigurationException is raised.
        """

        implem = config.get(cluster.name, 'fsusage')

        if implem == 'dummy':
            return FSUsageImporterDummy(app, db, config, cluster)
        elif implem == "ssh":
            return FSUsageImporterSSH(app, db, config, cluster)
        else:
            raise HPCStatsConfigurationException( \
                    "FSUsageImporter %s is not implemented" \
                      % (implem))
