#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'rakesh'
SITENAME = "Tan Man Dhan"
SITEURL = 'https://tan-man-dhan.com/' 
SITESUBTITLE = 'a healthy relationship with your finances'

PATH = 'content'
#ARTICLE_PATHS = ['blog']
#ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
#ARTICLE_URL = '{date:%Y}/{slug}.html'
TIMEZONE = 'Asia/Calcutta'
DEFAULT_LANG = 'en'
SLUGIFY_SOURCE = 'title'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_CATEGORY = 'misc'
USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
ARTICLE_EXCLUDES = ['secrets']

# Blogroll
LINKS = (('About', '/about.html'),
         ('Contact', '/journal.html'),
         )

# Blogroll
OTHERS = (('Link1', 'http://getpelican.com/'),
         ('Link2', '#'),
         )
# Social widget
SOCIAL = (('LinkedIn', '#'),
          ('Twitter', '#'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
