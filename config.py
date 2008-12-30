#!/usr/bin/python

"""
Global configuration file for Mozilla l10n scripts
"""

# Our language's ISO 639-2 code at Mozilla localizations
MOZLANG = "eu"

# Set this to the product(s) you are localizing. Available options are:
# FX (Firefox), TB (Thunderbird), CA (Calendar), TK (Toolkit)
# Example: PRODUCTS = ["FX", "TB"]
PRODUCTS = ["TB"]

# Set this to the repository you are working on.
# Available options: 1.9.1
REPO = "1.9.1"

# Parameters passed to moz2po/po2moz scripts
COMMON_PARAMS = ["--errorlevel=traceback", "--progress=verbose", "-x *.xhtml", "-x *.inc", "-x *.xml", "-x *.rdf", "-x bookmarks.html", "-x welcome.xhtml", "-x platformKeys.properties", "-x pref-publish.dtd", "-x *.txt", "-x *.css", "-x charset.mk"]
MOZ2PO_PARAMS = ["--duplicates=msgctxt"] + COMMON_PARAMS[:]
PO2MOZ_PARAMS = COMMON_PARAMS[:]


#
# WARNING: Do not edit below this line unless you know what you are doing
#

# Firefox directories
DIRS_FX = ("browser", "extensions/reporter", "other-licenses/branding/firefox")
# Thunderbird directories
DIRS_TB = ("mail", "other-licenses/branding/thunderbird", "editor/ui")
# Calendar directories
DIRS_CA = ("calendar", "other-licenses/branding/sunbird")
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

# l10n.ini location for compare-locales
# Firefox
FX_L10N_INI = "ini/browser.ini"
# Thunderbird
TB_L10N_INI = "ini/mail.ini"
# Toolkit
TK_L10N_INI = "ini/toolkit.ini"
# Calendar
CA_L10N_INI = "ini/calendar.ini"

# en-US base repository dirname
# WARNING: if you change this, you'll have to edit ini files accordingly
REPODIR = "mozilla"

