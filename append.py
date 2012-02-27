#!/usr/bin/env python
#
# Append to page command:
# Inputs:
#   PAGE_NAME - Name of a wiki page.
#
# Optional:
#   TEXT_TO_APPEND - Text to append to the wiki page.
#

import init
import datetime
import string
import subprocess
import sys
import tempfile

if len(sys.argv) not in (2,3):
    print "usage: append [PAGE_NAME] [TEXT_TO_APPEND] (leave off for vim buffer)"
    sys.exit(1)

append_arg=None
if len(sys.argv) is 3:
    append_arg = sys.argv[2]

mw = init.mw("[HOST]", "[PATH]")
page_name = sys.argv[1]
log_page = mw.site.Pages[page_name]
page_text = log_page.edit()

if page_text not in (None,""):
    page_text = string.join((page_text,'<br/>'), '')

# append text, save and exit if append text provided
if append_arg is not None:
    updated_page_text = string.join((page_text,append_arg))
    log_page.save(updated_page_text, summary='')
    print "Saved update to %s." % (page_name)
    sys.exit(0)

# delegate to vim for the append text
date = datetime.date.today()
try:
    temp = tempfile.NamedTemporaryFile(suffix='.logpage',prefix=str(date))
    vim_cmd = ['vim', str(temp.name)]
    vim_proc = subprocess.call(vim_cmd)
    edit = temp.read()
  
    if edit in ("",None):
        print "No update; exit without saving."
        sys.exit(0)

    updated_page_text = string.join((page_text,edit),'')

    log_page.save(updated_page_text, summary='')
    print "Saved update to %s." % (page_name)
finally:
    temp.close()

