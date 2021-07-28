#!/usr/bin/env python

#import necessary libraries
#pip install flask 
#export FLASK_APP=flask-app
#flask run
from flask import Flask, json, render_template, request, jsonify

import os

#create instance of Flask app
app = Flask(__name__)

#decorator 
@app.route("/")
def home_page():
    welcome_msg = '<p>Nobel Data</p> \
    <p>/all for all years</p> \
    <p>/all/year for one year</p> \
    <p>/add_data for input data function, returns data</p>'
    return welcome_msg

@app.route("/all")
def all():
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))
    #render_template is always looking in templates folder
    return render_template('index.html',data=data_json)

@app.route("/all/<year>")
def get_year(year):
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))
    data = data_json['prizes']
    year = request.view_args['year']
    output_data = [x for x in data if x['year']==year]
    #render_template is always looking in templates folder
    return render_template('index.html',data=output_data)


@app.route("/add_data", methods=["POST", "GET"])    
def add_data():
    if request.method == "POST":
        # data in a diction
        data = request.form
        # file path
        filenm = "./static/nobel.json"

        with open(filenm,'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside prizes
            file_data["prizes"].append(data)
            # Sets file's current position at offset. not understanding this step
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
        # I'd like to return a statement that it was added and the data
        # but I don't know how do that, possibly a new html page
        # way beyond my current capabilities
        return '<p>Data added </p>'

    else:    
        return render_template("add_data.html")

if __name__ == "__main__":
    app.run(debug=True)
