#!/usr/bin/python

"""
Script to update localizations from the repositories
"""

from config import *
from datetime import datetime
from optparse import OptionParser
import os
import subprocess
import sys

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

# Update requested repositories -- hg doesn't have partial clone/checkouts :(
if not options.l10n:
    print
    print "Checking out en-US repository changes..."
    print

    repodir = os.path.join("mozilla", REPO)

    if not os.path.exists("mozilla"):
        try:
            os.mkdir("mozilla")
        except OSError:
            print "Error: couldn't create 'mozilla' directory"
            sys.exit(0)
        os.chdir("mozilla")
        print
        print "Repository not found -- checking for the first time"
        print
        #TODO: use a different repository for 1.9.2 when it becomes available
        cmd = ["hg", "clone", "http://hg.frenchmozilla.fr/", REPO]
    else:
        os.chdir(repodir)
        cmd = ["hg", "pull", "-u"]

    print cmd
    subprocess.call(cmd)
    os.chdir(basedir)

if not options.en:
    print
    print "Checking out l10n repository changes for '%s'..." % (MOZLANG)
    print

    l10nbasedir = os.path.join("l10n", REPO)
    l10ndir = os.path.join(l10nbasedir, MOZLANG)

    if not os.path.exists(l10ndir):
        try:
            os.makedirs(l10nbasedir)
        except OSError:
            print "Error: couldn't create %s directory" % (l10nbasedir)
            sys.exit(0)
        os.chdir(l10nbasedir)
        print
        print "Repository not found -- checking for the first time"
        print
        if REPO == "1.9.1":
            cmd = ["hg", "clone", "http://hg.mozilla.org/releases/\
l10n-mozilla-1.9.1/%s/" % (MOZLANG)]
        else:
            cmd = ["hg", "clone", "http://hg.mozilla.org/l10n-central/%s/" % (MOZLANG)]
    else:
        os.chdir(l10ndir)
        cmd = ["hg", "pull", "-u"]

    print cmd
    subprocess.call(cmd)
    os.chdir(basedir)

