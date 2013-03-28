# -*- coding: utf-8 -*-

from flask import Flask, render_template
from utils import gametype, mapname, colour, geoip, trim
import parser

app = Flask(__name__, static_folder="/home/iw4m/web/static")

@app.route('/')
def index():
	servers = parser.load()
	return render_template('index.html', servers=servers, trim=trim, geoip=geoip, colour=colour, gametype=gametype, mapname=mapname, len=len)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
