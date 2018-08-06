import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'm24_salon_app'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route("/")
def get_index():
    return render_template('index.html')  


@app.route("/add_request")
def add_request():
    services = mongo.db.services.find()
    return render_template('add_request.html', services=services)


@app.route("/insert_request", methods=['POST'])
def insert_request():
    mongo.db.requests.insert_one(request.form.to_dict())
    return redirect(url_for('get_index'))


@app.route("/edit_request")
def edit_request():
    request_id = request.args['request_id']
    
    req = mongo.db.requests.find_one({"_id": ObjectId(request_id)})
    return render_template('edit_request.html', request=req)
    
#dirty code---------------written--scum--faced--steve!---- 
@app.route("/")
@app.route("/get_request")
@app.route("/get_request_by_requests/<first_name>")
def get_requests(request_name=None):
    if request_name:
        requests=mongo.db.requests.find({"first_name": request_name})
    else:
        requests=mongo.db.requests.find()
        
    return render_template("appointments.html", requests=requests)


@app.route("/update_request/<request_id>", methods=['POST'])
def update_request(request_id):
    requests = mongo.db.request
    requests.update({"_id": ObjectId(request_id)}, request.form.to_dict())
    return redirect(url_for("get_requests")) 

@app.route("/delete_request/", methods=["POST"])
def delete_request():
    request_id = request.form['request_id']
    mongo.db.requests.remove({"_id": ObjectId(request_id)})
    return redirect(url_for("get_requests"))

#filthy code---------------written--scum--faced--steve!----
@app.route("/addresses")
def add_address():
    addresses = mongo.db.addresses.find()
    return render_template('add_address.html', addresses=addresses)     
    
@app.route("/show_address")
def show_address():
    addresses = mongo.db.addresses.find()
    return render_template('show_addresses.html', addresses=addresses)
    
       

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)





