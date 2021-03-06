#!/usr/bin/python

"""
Script to update localizations from the repositories
"""

from config import *
from datetime import datetime
from optparse import OptionParser
import errno
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

    if not os.path.exists(REPODIR):
        print
        print "Repository not found -- checking for the first time"
        print
        if not os.path.exists(REPO_BASEDIR):
            os.mkdir(REPO_BASEDIR)
        cmd = ["hg", "clone", REPO_URL, REPODIR]
    else:
        os.chdir(REPODIR)
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
        except OSError, e:
            if e.errno != errno.EEXIST:
                print "Error: couldn't create %s directory" % (l10nbasedir)
                sys.exit(0)
        os.chdir(l10nbasedir)
        print
        print "Repository not found -- checking for the first time"
        print
        if REPO != "mozilla-central":
            cmd = ["hg", "clone", "http://hg.mozilla.org/releases/\
l10n-mozilla-%s/%s/" % (REPO, MOZLANG)]
        else:
            cmd = ["hg", "clone", "http://hg.mozilla.org/l10n-central/%s/"\
                  % (MOZLANG)]
    else:
        os.chdir(l10ndir)
        cmd = ["hg", "pull", "-u"]

    print cmd
    subprocess.call(cmd)
    os.chdir(basedir)

