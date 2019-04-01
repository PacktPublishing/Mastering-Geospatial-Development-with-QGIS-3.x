# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TestPlugin
                                 A QGIS plugin
 This is the description of the plugin
                             -------------------
        begin                : 2014-12-19
        copyright            : (C) 2014 by Luigi Pirelli
        email                : luipir@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load TestPlugin class from file TestPlugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .test_plugin import TestPlugin
    return TestPlugin(iface)
