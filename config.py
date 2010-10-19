#!/usr/bin/python

"""
Global configuration file for Mozilla l10n scripts
"""

import os

# Our language's ISO 639-2 code at Mozilla localizations
MOZLANG = "eu"

# Set this to the product(s) you are localizing. Available options are:
# FX (Firefox), TB (Thunderbird), CA (Calendar), TK (Toolkit)
# Example: PRODUCTS = ["FX", "TB"]
PRODUCTS = ["TB"]

# Set this to the repository you are working on.
# Available options: 1.9.1, 1.9.2, mozilla-central
REPO = "1.9.2"

# Parameters passed to moz2po/po2moz scripts
COMMON_PARAMS = ["--errorlevel=traceback", "--progress=verbose", "--exclude=*.xhtml", "--exclude=*.inc", "--exclude=*.xml" "--exclude=*.rdf", "--exclude=*.js", "--exclude=*.html", "--exclude=*.txt", "--exclude=*.css", "--exclude=*.mk"]
MOZ2PO_PARAMS = ["--duplicates=msgctxt"] + COMMON_PARAMS[:]
PO2MOZ_PARAMS = COMMON_PARAMS[:]


#
# WARNING: Do not edit below this line unless you know what you are doing
#

# Firefox directories
DIRS_FX = ("browser", "other-licenses/branding/firefox", "services/sync")
# Thunderbird directories
DIRS_TB = ("mail", "other-licenses/branding/thunderbird", "editor/ui")
# Calendar directories
DIRS_CA = ("calendar", "other-licenses/branding/sunbird")
# Mobile directories
DIRS_MB = ("mobile", )
# Common directories (Toolkit)
DIRS_CM = ("dom", "netwerk", "security/manager", "toolkit")

# Set DIRS according to the PRODUCT choice
DIRS = []
if "FX" in PRODUCTS:
    DIRS.extend(DIRS_FX)
if "TB" in PRODUCTS:
    DIRS.extend(DIRS_TB)
if "TK" in PRODUCTS:
    DIRS.extend(DIRS_CM)
if "CA" in PRODUCTS:
    DIRS.extend(DIRS_CA)
if "MB" in PRODUCTS:
    DIRS.extend(DIRS_MB)

# Repository base location and repository URL
REPO_BASEURL = "http://hg.mozilla.org.tr/"
REPO_URL = REPO_BASEURL + "%s/mozilla-l10n/" % (REPO)

# en-US base repository dirname
# WARNING: if you change this, you'll have to edit ini files accordingly
REPO_BASEDIR = "mozilla"
REPODIR = os.path.join(REPO_BASEDIR, REPO)
ENUSDIR = os.path.join(REPODIR, "en-US")
INIDIR = os.path.join(REPODIR, "ini")

# l10n.ini location for compare-locales
# Firefox
FX_L10N_INI = os.path.join(INIDIR, "browser.ini")
# Thunderbird
TB_L10N_INI = os.path.join(INIDIR, "mail.ini")
# Toolkit
TK_L10N_INI = os.path.join(INIDIR, "toolkit.ini")
# Calendar
CA_L10N_INI = os.path.join(INIDIR, "calendar.ini")
# Mobile
MB_L10N_INI = os.path.join(INIDIR, "mobile.ini")

