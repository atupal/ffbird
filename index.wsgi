#!/usr/bin/env python2
import os
import sys

os.system('git pull')
# add the current dir to python path
CURRENT_DIR = os.path.expanduser(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, CURRENT_DIR)

from app import app

if 'SERVER_SOFTWARE' in os.environ:
  import sae
  application = sae.create_wsgi_app(app)
else:
  app.run(host='0.0.0.0')
