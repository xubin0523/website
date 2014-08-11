#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mark'
SITENAME = u'Another Dimensiong'
SITEURL = ''

PATH = 'content'
PLUGIN_PATHS = ["../pelican-plugins"]
PLUGINS = ["assets", "tipue_search"]
#SITEMAP = {'format':'xml'}
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives',
                     'search', '404'))
SOCIAL_PROFILE_LABEL = 'Stay in Touch'
USE_FAVICON = True
TIMEZONE = 'Asia/Shanghai'
THEME = 'elegant'
DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
GOOGLE_ANALYTICS = 'UA-53683327-1'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'http://github.com/xubin0523'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
LANDING_PAGE_ABOUT = {'title':'About me',
	'details':'My name is Mark'} 
PROJECTS = [{
    'name': 'Logpad + Duration',
    'url': 'https://github.com/talha131/logpad-plus-duration#logpad--duration',
    'description': 'Vim plugin to emulate Windows Notepad logging feature,'
    ' and log duration of each entry'},
    {'name': 'Elegant Theme for Pelican',
    'url': 'http://oncrashreboot.com/pelican-elegant',
    'description': 'A clean and distraction free theme, with search and a'
    ' lot more unique features, using Jinja2 and Bootstrap'}]
