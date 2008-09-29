#!/usr/bin/python

"""
Script to create diffs.
"""

from config import *
from optparse import OptionParser
import os
import subprocess
import sys

# TODO: add an command-line option to set a bug number to create a directory
#       in which the diff will be saved.
# TODO: Just an idea, but with an extra argument (e.g. -a), we could append
#      the current datetime if -o is given.

# Create command-line option parser and parse arguments
parser = OptionParser()
parser.add_option("--dir", "-d", dest="directory", default=None,
    help="Directory in which diff will be executed (relative to l10n/MOZLANG \
dir). Filenames can be used too. Default: diff all the repository.")
parser.add_option("--output", "-o", dest="filename", default=None,
    help="Write diff output to this filename. Default: stdout")

(options, args) = parser.parse_args()

# Set diffing directory/file
if options.directory:
    DIR = os.path.join("l10n", MOZLANG, options.directory)
else:
  	DIR = os.path.join("l10n", MOZLANG)

if not os.path.exists("patches"):
    os.mkdir("patches")
if not os.path.exists(DIR):
    print "Error: directory not found. Aborting."
    sys.exit(0)

# Run command and write output
cmd = ["hg", "diff", DIR]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
proc_output = proc.communicate()[0]
if options.filename:
    output_filename = "patches/%s.diff" % (options.filename)
    try:
        output_file = open(output_filename, "w")
        output_file.write(proc_output)
        output_file.close()
        print "Wrote file %s" % (output_filename)
    except IOError:
        print "Error: I/O error"
else:
    print proc_output
