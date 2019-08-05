#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, session, redirect, url_for, request, render_template
import base64
from urllib import request as reque
import re
import socket


app = Flask(__name__)
__author__ = "LoRexxar"


def get_picture(url):
    try:
        req = reque.Request(url)

        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
        req.add_header('Accept-Encoding', 'gzip, deflate, sdch')
        req.add_header('Cache-Control', 'max-age=0')
        req.add_header('Connection', 'Keep-Alive')
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36')

	   req = reque.urlopen(url, timeout=3)
        return req
    except reque.URLError as e:
        print e
	   return None
    except ValueError as e:
        print e
	   return None
    except socket.timeout as e:
	   print e
	   return None
    except:
	   return None

def check(url):
    
    if "localhost" in url:
        return 'you can\'t find localhost picture...'

    if not re.match("(http|https):\/\/[a-zA-Z]+(\.[\w\-]+)+[a-zA-Z]+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])", url):
        return 'NoNoNo, guys, Links must be accord with standard of .tid and contain domain name.'



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/show', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        
    	url = request.form['link']
    	
        if url is None:
            redirect(url_for('index'))

        if check(url) is not None:
            return check(url)

        if get_picture(url) is None:
            return 'urlopen error...'

        content = get_picture(url).read()
        image_content = base64.b64encode(content)

        return render_template('show.html', image_content=image_content)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, threaded=True)
