#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Calango'
SITENAME = 'Calango Hacker Club'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

CATEGORIES_URL = 'blog/categorias'
CATEGORIES_SAVE_AS = 'blog/categorias/index.html'
CATEGORY_URL = 'blog/categorias/{slug}'
CATEGORY_SAVE_AS = 'blog/categorias/{slug}/index.html'

TAG_URL = 'blog/tags/{slug}'
TAG_SAVE_AS = 'blog/tags/{slug}/index.html'
TAGS_URL = 'blog/tags'
TAGS_SAVE_AS = 'blog/tags/index.html'

AUTHOR_URL = 'blog/autores/{slug}'
AUTHOR_SAVE_AS = 'blog/autores/{slug}/index.html'
AUTHORS_URL = 'blog/autores'
AUTHORS_SAVE_AS = 'blog/autores/index.html'

INDEX_SAVE_AS = "blog/index.html"

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['./plugins']
PLUGINS = [
        'better_figures_and_images',
        'sitemap',
        ]

RESPONSIVE_IMAGES = True
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.2,
        'pages': 0.7
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    },
}

# Navbar Links
NAVBAR_HOME_LINKS = [
    {
        "title" : "Blog",
        "href" : "blog",
    },
]

# Blogroll
LINKS = (('Wiki Calango', 'http://calango.club/'),
         ('Google Groups', 'http://groups.google.com/group/calangohc'),
         ('Planeta Calango', 'http://planeta.calango.club/'),
         )

# Social widget
SOCIAL = (('Grupo no Facebug',
           'https://www.facebook.com/groups/calangohackerclube/'),
          ('Página no Facebug', 'https://www.facebook.com/calangohc'),
          ('Twitter', 'https://twitter.com/calangohc'),
          ('Google+', 'https://plus.google.com/+CalangohackerClub'),
          ('YouTube', 'https://www.youtube.com/c/%2BCalangohackerClub'),
          )

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "pelican-bootstrap3-hack"
BOOTSTRAP_THEME = "darkly"
SITELOGO = "images/logo.png"
CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = ['images', 'extra/custom.css']
EXTRA_PATH_METADATA = {'extra/custom.css': {'path': 'static/custom.css'},}
BOOTSTRAP_NAVBAR_INVERSE = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
HIDE_SOCIAL_ICONS = True

import glob
import json
import datetime

def datetime_parser(dct):
    if not ('data' in dct):
        return dct
    data = dct['data']
    try:
        data = datetime.datetime.strptime(data, "%d/%m/%y %H:%M")
    except:
        dct['data'] = ''
        return dct
    dct['data'] = data
    return dct

EVENTOS = [json.load(open(fname, 'r'), object_hook=datetime_parser) for fname in glob.glob("content/eventos/*.json")]
EVENTOS = sorted(EVENTOS, key=lambda dct: dct['data'])
