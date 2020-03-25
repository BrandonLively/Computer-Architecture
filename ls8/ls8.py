#!/usr/bin/env python3

"""Main."""

import sys
import os
from cpu import *

basedir = os.path.abspath(os.getcwd())
filedir = os.path.join(basedir, "examples")

filename = "mult.ls8"

filepath = os.path.join(filedir, filename)

cpu = CPU()

cpu.load(filepath)
cpu.run()