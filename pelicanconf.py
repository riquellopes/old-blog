#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Henrique Lopes'
SITENAME = u'Henrique Lopes'
SITEURL = 'http://blog.henriquelopes.com.br'
GITHUB_URL = 'http://github.com/riquellopes'
GITHUB_BRANCH = "pelican"
PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'
HTML_LANG = u'pt-BR'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('PythonBrasil', 'http://wiki.python.org.br/'),)

# Social widget
SOCIAL = (('github', 'http://github.com/riquellopes'),
          ('linkedIn', 'https://www.linkedin.com/in/riquellopes'),
          ('twitter', 'https://twitter.com/riquellopes'),
          ('delicious', 'https://delicious.com/riquellopes'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

READERS = {"html": None}
MD_EXTENSIONS = (['codehilite', 'extra'])
STATIC_PATHS = ['extra/CNAME', 'imagens', 'extra/robots.txt', 'extra/google4907ef7739dd27da.html']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/google4907ef7739dd27da.html': {'path': 'google4907ef7739dd27da.html'}
}

# Plugins
PLUGIN_PATHS = [
    'pelican-plugins',
]

PLUGINS = ["sitemap"]
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.5,
        'pages': 0.3
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Theme
RELATIVE_URLS = True
THEME = 'pelican-theme/'

DISQUS_SITENAME = 'riquellopes'
DISQUS_NO_ID = True
GOOGLE_ANALYTICS = "UA-72238128-1"
