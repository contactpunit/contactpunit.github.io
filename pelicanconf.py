#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Punit Jain'
SITENAME = 'My Tech Blogs'
SITEURL = ''
SITETITLE = 'Punit Jain'
SITESUBTITLE = 'Ideas and Thoughts'
SITELOGO = '/images/profile.png'

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

SOCIAL = (
    ('github', 'https://github.com/contactpunit'),
    ('envelope', 'mailto:contactpunitjain@gmail.com'),
    ('linkedin','https://np.linkedin.com/in/punit-jain-25302823'),
)

STATIC_PATHS = ['images', 'extra']
MAIN_MENU = True
MENUITEMS = (('Home','/'),('Archives', '/archives'),('Categories', '/categories'),('Tags', '/tags'))
PYGMENTS_STYLE = 'friendly'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

THEME = 'themes/Flex'

PLUGIN_PATHS = ['./pelican-plugins']

PLUGINS = ['sitemap', 'post_stats', 'feed_summary']

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
