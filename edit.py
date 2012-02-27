#!/usr/bin/env python
#
# Edit page command:
# Inputs:
#   PAGE_NAME - Name of a wiki page.
#

import init
import datetime
import tempfile
import subprocess
import sys

if len(sys.argv) is not 2:
    print "usage: edit [PAGE_NAME]"
    sys.exit(1)

mw = init.mw("[HOST]", "[PATH]")

page_name = sys.argv[1]

log_page = mw.site.Pages[page_name]
page_text = log_page.edit()
date = datetime.date.today()

try:
    temp = tempfile.NamedTemporaryFile(suffix='.logpage',prefix=str(date))
    temp.write(page_text)
    temp.seek(0)
    
    vim_cmd = ['vim', str(temp.name)]
    vim_proc = subprocess.call(vim_cmd)
    temp.seek(0)
    edit = temp.read()
   
    if page_text == edit:
        print "No update; exit without saving."
        sys.exit(0)

    log_page.save(edit, summary='')
    print "Saved update to %s." % (page_name)
finally:
    temp.close()

