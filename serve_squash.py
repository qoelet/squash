# serving of squash

from bottle import route, run, send_file, abort, request, response, redirect, template
from squash import *
from settings import *

# Squash homepage, with form for generating short urls
@route('/')
def homepage():
	return template('squashit.tpl',title='Shorten your URLs with Squash!')
	
# Static files
@route('/static/:filename')
def static_file(filename):
    send_file(filename, root=MEDIA_ROOT)
    
# Gets long url and returns shortened url
@route('/shorten/', method='POST')
def squashurl():
    if 'url' in request.POST:
        url = request.POST['url']
        s = Squash()
        shortened_url = s.sendto_lightcloud(url)
    return template('squashed.tpl',title='Shorten your URLs with Squash!',result=(MYDOMAIN+shortened_url))
	
# Redirects to url
@route('/:id')
def transfer(id):
	s = Squash()
	fullurl = s.getfrom_lightcloud(id)
	if fullurl is not None:
	    redirect(fullurl)
	else:
	    return "Invalid id."


run(host='localhost', port=MYPORT)

