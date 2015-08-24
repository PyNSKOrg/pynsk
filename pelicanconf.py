#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

PROJECT_DIR = os.path.normpath(
    os.path.abspath(os.path.dirname(os.path.abspath(__file__))))


def get_theme_path(theme_name):
    return os.path.join(PROJECT_DIR, 'themes', theme_name)

AUTHOR = 'Alexander Sapronov'
SITENAME = 'PyNSK - Новосибирское Python сообщество'
# SITEURL = 'http://pynsk.ru'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Novosibirsk'

DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/py_nsk'),
    ('facebook', 'https://www.facebook.com/PyNskCom'),
    ('vk', 'https://vk.com/pynsk'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DIRECT_TEMPLATES = (
    ('index', 'tags', 'categories', 'authors', 'archives', 'search')
)
MARKUP = ('rst', 'markdown',)

THEME = get_theme_path('pelican-bootstrap3')


SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

PLUGIN_PATHS = [
    'pelican-plugins',
]

PLUGINS = [
    'summary',
    'liquid_tags.img',
    'liquid_tags.video',
    'liquid_tags.include_code',
    'liquid_tags.notebook',
    'liquid_tags.literal',
    'tipue_search',
    'sitemap',
    # 'pelican_youtube',
    'optimize_images',
    'tag_cloud',
    'post_stats',
]
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'


DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
SHOW_ARTICLE_CATEGORY = True
DISPLAY_ARTICLE_INFO_ON_INDEX = False
TAGS_URL = 'tags.html'



MENUITEMS = [
    ('Категории', '/categories.html')
]
