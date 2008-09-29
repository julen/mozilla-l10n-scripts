#!/usr/bin/python
"""
Script that runs compare-locales.
"""

from config import *
from subprocess import call

print
print "Running compare-locales"
print "--------------------------------------------------------"
print

if "FX" in PRODUCTS:
    print
    print "* Firefox"
    call(["compare-locales", FX_L10N_INI, "l10n", MOZLANG])
    print
    raw_input("Press ENTER to continue.")
if "TB" in PRODUCTS:
    print
    print "* Thunderbird"
    call(["compare-locales", TB_L10N_INI, "l10n", MOZLANG])
    print
    raw_input("Press ENTER to continue.")
if "CA" in PRODUCTS:
    print
    print "* Calendar doesn't have l10n.ini yet!"
    print
    raw_input("Press ENTER to continue.")

