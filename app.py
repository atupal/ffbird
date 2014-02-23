# -*- coding: utf-8 -*-
"""
  app.py
  ~~~~~~
  
  :author: atupal
  :licence: Apache, see the LICENCE for more detail
"""

try:
  import sae
except:
  sae = None

from flask import Flask
from flask import render_template

from random import randint

app = Flask(__name__, static_url_path='')

C = None
@app.route('/')
def index():
  if not sae:
    return render_template('single_game.html')

  try:
    C = cname = '%d' % randint(10000000, 99999999)
    from sae import channel
    socket = channel.create_channel(cname)
    print socket
  except Exception as e:
    return str(e)
  return render_template('index.html', cname=socket)

@app.route('/api', methods=['POST'])
def api():
  from sae import channel
  channel.send_message(C, "hello socket")
  print 'sucess'
  return 'test'

if __name__ == '__main__':
  app.run(host='1.0.0.0', debug=1)
