#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Henrique Lopes'
SITENAME = u'Henrique Lopes'
SITEURL = ''
GITHUB_URL = 'http://github.com/riquellopes'
PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('PythonBrasil', 'http://wiki.python.org.br/'),)

# Social widget
SOCIAL = (('github', 'http://github.com/riquellopes'),
          ('linkedIn', 'https://www.linkedin.com/in/riquellopes'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MD_EXTENSIONS = (['codehilite', 'extra'])