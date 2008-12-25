#!/usr/bin/python

"""
Script to convert Mozilla l10n files to PO files.
"""

from config import *
from optparse import OptionParser
import os
import subprocess

# Create command-line option parser and parse arguments
parser = OptionParser()
parser.add_option("--dir", "-d", dest="directory", default=None,
    help="Execute moz2po in this directory. Default: all the directories \
needed for PRODUCTS.")

(options, args) = parser.parse_args()

# Override DIRS if -d is given
if options.directory:
    DIRS = options.directory

# Create base dirs if necessary
po_basedir = os.path.join("po", MOZLANG)
if not os.path.exists(po_basedir):
    os.makedirs(po_basedir)

# Run moz2po for each directory in DIRS
for dir in DIRS:
    print
    print "Running moz2po %s" % (dir)
    print "--------------------------------------------------------"
    current_inputdir = os.path.join("l10n", REPO, MOZLANG, dir)
    current_podir = os.path.join(po_basedir, dir)
    if not os.path.exists(current_podir):
        os.makedirs(current_podir)
    current_templatedir = os.path.join(REPODIR, dir, "locales", "en-US")
    MOZ2PO_PARAMS += ["-i", current_inputdir]
    MOZ2PO_PARAMS += ["-t", current_templatedir]
    MOZ2PO_PARAMS += ["-o", current_podir]
    cmd = ["moz2po"] + MOZ2PO_PARAMS
    proc = subprocess.Popen(cmd)
    proc.wait()
    print
    raw_input("Press ENTER to continue.")

