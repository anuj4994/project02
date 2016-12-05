# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:24:05 2016

@author: Anuj Shah
"""

from flask import Flask
from flask_restful import Resource, Api
from flask import Response
import json
import urllib
from flask import request
from flask_restful import reqparse
from flask.ext.mysql import MySQL

app = Flask(__name__)
api = Api(app)

mysql = MySQL()


# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'cloud'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
        
class getWorkInfo(Resource):
    def get(self,id):
        try:
            cursor.execute("select details,timestamp from cat where object_id = '/works/"+id+"' ")
            conn.commit()
	    st = ""
	    timestamp = ""
	    for record in cursor :
		st = record[0]
		timestamp = record[1]
	    js = json.loads(st)
	    authorLink = js["authors"][0]["author"]["key"]
	    url = "https://openlibrary.org"+authorLink+".json"
	    f = urllib.urlopen(url)
	    resp = json.loads(f.read())
    	    authorName = resp["name"]
            return {'Author Name': authorName , "details" : js, "Timestamp" : timestamp}

        except Exception as e:
            return {'error': str(e)}
class getSearchInfo(Resource):
    def get(self,word):
        try:
            cursor.execute("select object_id  from cat where details like '%"+word+"%'")
	    r = ""
	    ans = []
            for record in cursor :
		ans.append("http://54.70.113.238:5001"+record[0].replace('works','work'))
#	    data = cursor.fetchall()

            return {'works': ans}

        except Exception as e:
            return {'error': str(e)}



api.add_resource(HelloWorld, '/')
api.add_resource(getWorkInfo, '/work/<string:id>')
api.add_resource(getSearchInfo, '/search/<string:word>')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)

