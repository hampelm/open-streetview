Little scripts to get GPS traces. They'll eventually get some photos from a
USB webcam, too.

I'm using a GlobalSat BU-353 USB GPS reciever. It costs about $40 on Amazon.

## Using the app

Browse to `http://127.0.0.1:5000/static/index.html` to see the map.

## Getting started

You'll need the [Mac driver](http://www.usglobalsat.com/s-122-bu-353-support.aspx)
for the GPS reciever.

Create a virtualenv:

`mkvirtualenv geo --no-site-packages`

(or `workon geo` if you already have the virtualenv)

Install the dependencies:

`pip install -r requirements.txt`

Lots more dependencies:

`brew install opencv`

`brew install sdl sdl_ttf sdl_image sdl_mixer` and then

`pip install hg+http://bitbucket.org/pygame/pygame`

Might need to update your path:

`export PYTHONPATH="/usr/local/lib/python2.7/site-packages:$PYTHONPATH"`
