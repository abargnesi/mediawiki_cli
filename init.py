#!/usr/bin/env python
import mwclient

class mw:

    '''
    Initialize the mediawiki site using mwclient.
    '''
    def __init__(self, host, path=None, username=None, password=None):
        self.site = mwclient.Site(host, path)

        if username and password:
            self.site.login(username,password)

