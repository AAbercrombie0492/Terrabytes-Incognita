#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Anthony Abercrombie'
SITENAME = u'Terra[bytes] Incognita'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'MST'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "pelican-themes/bricks"

TYPOGRIFY = True
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Special thanks to Hawnuh Lee @ Postfloral for the imagery!', 'https://postfloral.com/'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/anthony.abercrombie.3'),
          ('LinkedIn', 'https://www.linkedin.com/in/anthony-abercrombie-67264895'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
