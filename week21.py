#!/usr/bin/env python

#import necessary libraries
# pip install flask 
#export FLASK_APP=flask-app
#flask run
from flask import Flask, json, render_template, request, jsonify, redirect, url_for
import requests
import os

#create instance of Flask app
app = Flask(__name__)

#decorator 
@app.route("/")
def home_page():
    welcome_msg = '<p>Nobel Data</p> \
    <p>/all for all years</p> \
    <p>/all/year for one year</p> \
    <p>/add_data for input data function</p>'
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

#this doesn't work, commenting it out
'''
@app.route("/datainput", methods=['POST', "GET"])
def datainput():
    data = {'year': '2025', 'category': 'test_garbage', 'laureates': 
    [{'id': 'test_1', 'firstname': 'Testing', 'surname': 'Lastname',
     'motivation': '"testing purposes"', 
     'share': '1'}]}
    
    json_url = os.path.join(app.static_folder,"","nobel.json")
    #response = requests.post(json_url, json=data) 
    #print(response.status_code) 
    #print(response.text)
    return jsonify(data)
'''

@app.route("/add_data", methods=["POST", "GET"])    
def add_data():
    if request.method == "POST":
        '''
        year = request.form['year']
        category = request.form['category']
        n_id = request.form['id']
        firstname = request.form['firstname']
        surname = request.form['surname']
        motivation = request.form['motivation']
        share = request.form['share']
        '''
        
        data = request.form
        
        filenm = "./static/nobel.json"

        with open(filenm,'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["prizes"].append(data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)

        '''
        json_url = os.path.join(app.static_folder,"","nobel.json")
        data_json = json.load(open(json_url))
        prizes_data = data_json['prizes']
        updated_data = prizes_data.append(data)
        '''
        return data
        #return redirect(url_for("save_data", data))
        
        '''(yr=year, cat = category, \
            num_id=n_id, fn=firstname, sn=surname, mot=motivation, shr=share)))
        '''

    else:    
        return render_template("add_data.html")

@app.route("/save_data")
def data(yr, cat, num_id, fn, sn, mot, shr):
    print(yr, cat)

if __name__ == "__main__":
    app.run(debug=True)
