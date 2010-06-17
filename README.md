# squash is a url shortener, written in Python #
@author Kenny Shen.

*requires?*

1. bottle.py - for serving squash as an app
2. lightcloud - my choice, but you can swap out with any key/val db of your preference. (lightcloud requires in turn a)tokyo cabinet b)tokyo tyrant c)hash_ring )

*files overview*

1. squash.py - contains code for squashing your urls. 

`from squash import Squash`
`s = Squash()`

2. settings.py - settings for port, media root, domain and db values.

3. serve_squash.py - bottle code for serving the app. (see for examples of routes, templates...etc)

*live example*

I'm using it at http://northpole.sg (not www.northpole.sg <- that points to my personal webpage.)


