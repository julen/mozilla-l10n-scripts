#!/usr/bin/python

"""
Script to convert Mozilla l10n files to PO files.
"""

from config import *
from datetime import datetime
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

# Backup the current repository, just in case
now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
if not os.path.exists("backup"):
    os.mkdir("backup")
backup_filename = os.path.join("backup", "%s_%s.tar.bz2" % (MOZLANG, now))
repo = os.path.join("l10n", MOZLANG)
cmd = ["tar", "--bzip2", "-cf", backup_filename, repo]
print "Making a copy of %s repository..." % (repo)
subprocess.Popen(cmd)
print
raw_input("Press ENTER to continue.")

po_basedir = os.path.join("po", MOZLANG)

# Run moz2po for each directory in DIRS
for dir in DIRS:
    print
    print "Running po2moz %s" % (dir)
    print "--------------------------------------------------------"
    current_dir = os.path.join(repo, dir)
    if not os.path.exists(current_dir):
        os.mkdir(current_dir)
    current_podir = os.path.join(po_basedir, dir)
    current_templatedir = os.path.join("mozilla", REPO, dir, "locales", "en-US")
    PO2MOZ_PARAMS += ["-i", current_podir]
    PO2MOZ_PARAMS += ["-t", current_templatedir]
    PO2MOZ_PARAMS += ["-o", current_dir]
    cmd = ["po2moz"] + PO2MOZ_PARAMS
    proc = subprocess.Popen(cmd)
    proc.wait()
    print
    raw_input("Press ENTER to continue.")

