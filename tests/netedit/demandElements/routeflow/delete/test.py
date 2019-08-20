#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2019 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2019-07-16
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot, ['--gui-testing-debug-gl'])

# go to demand mode
netedit.supermodeDemand()

# go to route mode
netedit.routeMode()

# create route using three edges
netedit.leftClick(referencePosition, 274, 414)
netedit.leftClick(referencePosition, 570, 250)
netedit.leftClick(referencePosition, 280, 60)

# press enter to create route
netedit.typeEnter()

# go to vehicle mode
netedit.vehicleMode()

# change vehicle
netedit.changeElement("routeFlow")

# create vehicle
netedit.leftClick(referencePosition, 274, 414)

# go to delete mode
netedit.deleteMode()

# delete vehicle
netedit.leftClick(referencePosition, 90, 414)

# Check undo
netedit.undo(referencePosition, 1)

# go to delete mode
netedit.deleteMode()

# delete vehicle and edge
netedit.leftClick(referencePosition, 90, 414)
netedit.leftClick(referencePosition, 90, 414)

# Check undo
netedit.undo(referencePosition, 2)

# Change to network mode
netedit.supermodeNetwork()

# go to delete mode
netedit.deleteMode()

# try to delete an edge with demand elements
netedit.leftClick(referencePosition, 274, 414)

# wait warning
netedit.waitDeleteWarning()

# disable protect demand elemnts
netedit.changeProtectDemandElements(referencePosition)

# now delete edge with their route
netedit.leftClick(referencePosition, 274, 414)

# Check undo
netedit.undo(referencePosition, 2)
netedit.redo(referencePosition, 2)

# save routes
netedit.saveRoutes(referencePosition)

# save network
netedit.saveNetwork(referencePosition)

# quit netedit
netedit.quit(neteditProcess)