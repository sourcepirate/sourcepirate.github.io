from __future__ import unicode_literals

AUTHOR = "sourcepirate"
SITENAME = "sourcepirate blog"
SITEURL = "https://sourcepirate.github.io"

PATH = "content"

TIMEZONE = "Asia/Kolkata"

DEFAULT_LANG = "en"
THEME = "./themes/cleanblog"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/sourcepirate'),
          ('github', 'https://github.com/sourcepirate'),
          ('facebook','https://facebook.com/sathya.shadow'),
          ('envelope','sathyanarrayanan@yandex.com'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
