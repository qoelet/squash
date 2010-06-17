# The static folder bottle will serve static files from
MEDIA_ROOT = '/path/to/squash/staticfolder'

# Url to append to shortened url id
MYDOMAIN = 'http://example.com/'

# The port you want bottle to serve to
MYPORT = 8080

# If you're using lightcloud, replace with your own settings.
LIGHTCLOUD_LOOKUPS = ['127.0.0.1:41201','127.0.0.1:51201']
LIGHTCLOUD_STORAGES = ['127.0.0.1:44201','127.0.0.1:54201']