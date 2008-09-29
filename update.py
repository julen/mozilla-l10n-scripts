#!/usr/bin/python

"""
Script to update localizations from the repositories
"""

from config import *
from datetime import datetime
from optparse import OptionParser
import os
import subprocess

# TODO: well, it's not TODO but just an easily feasible idea: run
#       compare-locales after updating repositories to log the status
#       of the localizalization.

# Create command-line option parser and parse arguments
parser = OptionParser()
parser.add_option("--en", dest="en", action="store_true", default=False, \
    help="Checkout en-US files only.")
parser.add_option("--l10n", dest="l10n", action="store_true", default=False, \
    help="Checkout l10n only.")

(options, args) = parser.parse_args()

# Base directory for operations
basedir = os.getcwd()

# Check if we have the repositories and if not, pull them
if COMM_CENTRAL:
    if not os.path.exists("comm-central"):
        cmd = ["hg", "clone", "http://hg.mozilla.org/comm-central"]
        subprocess.call(cmd)
        os.chdir("comm-central")
        cmd = ["python", "client.py", "checkout", "--skip-inspector",
               "--skip-ldap", "--skip-chatzilla", "--skip-venkman"]
        subprocess.call(cmd)
        os.chdir(basedir)
else:
    if not os.path.exists("mozilla-central"):
        cmd = ["hg", "clone", "http://hg.mozilla.org/mozilla-central/"]
        subprocess.call(cmd)
if not os.path.exists(os.path.join("l10n", MOZLANG)):
    cmd = ["hg", "clone", "http://hg.mozilla.org/l10n-central/%s/" % (MOZLANG)]

# Update requested repositories -- hg doesn't have partial clone/checkouts :(
if not options.l10n:
    print
    print "Checking out en-US repository changes..."
    print
    if COMM_CENTRAL:
        if not os.path.exists("comm-central"):
            print
            print "Repository not found -- checking for the first time"
            print
            cmd = ["hg", "clone", "http://hg.mozilla.org/comm-central"]
            subprocess.call(cmd)
        os.chdir("comm-central")
        cmd = ["python", "client.py", "checkout", "--skip-inspector",
               "--skip-ldap", "--skip-chatzilla", "--skip-venkman"]
        subprocess.call(cmd)
        os.chdir(basedir)
    else:
        if not os.path.exists("mozilla-central"):
            print
            print "Repository not found -- checking for the first time"
            print
            cmd = ["hg", "clone", "http://hg.mozilla.org/mozilla-central/"]
            subprocess.call(cmd)
        else:
            os.chdir("mozilla-central")
            cmd = ["hg", "pull", "-u"]
            subprocess.call(cmd)
            os.chdir(basedir)

if not options.en:
    print
    print "Checking out l10n repository changes for '%s'..." % (MOZLANG)
    print
    if not os.path.exists(os.path.join("l10n", MOZLANG)):
        print
        print "Repository not found -- checking for the first time"
        print
        cmd = ["hg", "clone", "http://hg.mozilla.org/l10n-central/%s/" % (MOZLANG)]
        subprocess.call(cmd)
    else:
        os.chdir(os.path.join("l10n", MOZLANG))
        cmd = ["hg", "pull", "-u"]
        subprocess.call(cmd)
        os.chdir(basedir)

