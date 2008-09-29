#!/usr/bin/python

"""
Global configuration file for Mozilla l10n scripts
"""

# Our language's ISO 639-2 code at Mozilla localizations
MOZLANG = "eu"

# Set this to the product(s) you are localizing. Available options are:
# FX (Firefox), TB (Thunderbird), CA (Calendar)
# Example: PRODUCTS = ["FX", "TB"]
PRODUCTS = ["TB"]

# Set this to True if using comm-central repository (Fx, Tb, Sb, ...)
# If set to False, it'll think we're using mozilla-central repository (Fx only)
COMM_CENTRAL = True

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
    DIRS.extend(DIRS_CM)
if "TB" in PRODUCTS:
    DIRS.extend(DIRS_TB)
    if "dom" not in DIRS:
        DIRS.extend(DIRS_CM)
if "CA" in PRODUCTS:
    DIRS.extend(DIRS_CA)

# l10n.ini location for compare-locales
# Firefox
if COMM_CENTRAL:
    FX_L10N_INI = "comm-central/mozilla/browser/locales/l10n.ini"
else:
    FX_L10N_INI = "mozilla-central/browser/locales/l10n.ini"
# Thunderbird
TB_L10N_INI = "comm-central/mail/locales/l10n.ini"
# No l10n.ini for Calendar yet
CA_L10N_INI = ""

