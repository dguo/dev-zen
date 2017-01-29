from __future__ import print_function

import os
from subprocess import call
import sys

def main():
    if os.access('./dev', os.X_OK):
        call(['./dev'] + sys.argv[1:])
    else:
        print('There is no executable dev script to run.')
