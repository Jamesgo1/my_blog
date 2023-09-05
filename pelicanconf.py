AUTHOR = 'James Gough'
SITENAME = "James Gough"
SITESUBTITLE = "Data, programming, life, etc"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('github', "https://github.com/Jamesgo1"),
    ('twitter', "https://twitter.com/james_a_gough"),
)


DEFAULT_PAGINATION = 5
DEFAULT_DATE = "fs"

USE_FOLDER_AS_CATEGORY = True

THEME = r"themes/pelican-clean-blog"
SLUGIFY_SOURCE = "basename"
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = Truecd
