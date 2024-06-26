#!/usr/bin/env python

# Copyright Contributors to the Open Shading Language project.
# SPDX-License-Identifier: BSD-3-Clause
# https://github.com/AcademySoftwareFoundation/OpenShadingLanguage

command  = testshade("-g 1 1 -od uint8 -o Fout out.tif " +
                     "--layer upstream upstream --layer downstream test " +
                     "--connect upstream out downstream a " +
                     "--connect upstream struct1 downstream mystruct1" 
                     )

# Run again, this time considering userdata (lockgeom=0) parameters to be
# isconnected(). This time, parameter c should look like a connection.
command += testshade("--userdata_isconnected " +
                     "--layer upstream upstream --layer downstream test " +
                     "--connect upstream out downstream a " +
                     "--connect upstream struct1 downstream mystruct1")
