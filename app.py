import os
import datetime
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from decimal import Decimal
import json


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'm24_salon_app'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

# User

@app.route("/")
def get_index():
    return render_template('index.html') 
    
  
@app.route("/add_request_user")
def add_request_user():
    services = mongo.db.services.find()
    return render_template('add_request_user.html', services=services)


@app.route("/insert_request_user", methods=['POST'])
def insert_request_user():
    mongo.db.requests.insert_one(request.form.to_dict())
    return redirect(url_for('get_index'))


@app.route("/admin/")
def get_requests_admin():
    requests=mongo.db.requests.find()
    return render_template("admin/show_appointments_admin.html", requests=requests)

@app.route("/admin/add_request_admin")
def add_request_admin():
    services = mongo.db.services.find()
    return render_template('admin/add_appointment_admin.html', services=services)

@app.route("/admin/insert_request_admin", methods=['POST'])
def insert_request_admin():
    mongo.db.requests.insert_one(request.form.to_dict())
    return redirect(url_for('get_requests_admin'))


@app.route("/admin/edit_request_admin")
def edit_request_admin():
    
    
    return render_template('admin/edit_appointment_admin.html')
  
  
@app.route("/admin/update_request_admin/<request_id>", methods=['POST'])
def update_request_admin(request_id):
    requests = mongo.db.requests
    requests.update({"_id": ObjectId(request_id)}, request.form.to_dict())
    return redirect(url_for("get_requests_admin")) 
  
  
@app.route("/admin/delete_request/", methods=["POST"])
def delete_request_admin():
    request_id = request.form['request_id']
    mongo.db.requests.remove({"_id": ObjectId(request_id)})
    return redirect(url_for("get_requests_admin"))
  
@app.route("/admin/filter_today")
def filter_today_admin():
    todays_date = datetime.datetime.today().strftime('%-d %B, %Y')
    filtered_requests = mongo.db.requests.find({"due_date": todays_date})
    return render_template("admin/appointments_admin.html", requests=filtered_requests)
    
  
@app.route("/admin/show_graphs_admin")
def show_graphs_admin():
    total_income = 0.0
    total_outgoing = 0.0
    transactions = mongo.db.transactions.find()
    for transaction in transactions:
        total_income += transaction['moneyin']
        total_outgoing += transaction['moneyout']
    balance = total_income - total_outgoing
    return render_template("admin/show_graphs_admin.html", transactions=transactions, total_income=total_income, total_outgoing=total_outgoing, balance=balance)        
 
 

@app.route("/data")
def get_data():
    transactions = mongo.db.transactions.find({}, {'_id': False})
    list_transactions = []
    for t in transactions:
        list_transactions.append(t)
    return json.dumps(list_transactions)
        
 #-----------------------------------------------------------------#
 
 
@app.route("/admin/show_transactions_admin")
def show_transactions_admin():
    transactions=mongo.db.transactions.find()
    services=mongo.db.services.find()
    requests=mongo.db.requests.find()
    suppliers=mongo.db.suppliers.find()
    return render_template("admin/show_transactions_admin.html", transactions=transactions, services=services, suppliers=suppliers, requests=requests)        
 #---------------------------Friday------------------------------#

@app.route('/edit_transaction_admin/<transaction_admin_id>')
def edit_transaction_admin(task_id):
    the_transaction_admin = mongo.db.transactions.find_one({'_id': ObjectId(task_id)})
    all_transactions = mongo.db.transactions.find()
    return render_template(
        'edit_transaction_admin.html', transaction_admin=the_transaction_admin, transactions=all_transactions)

 
#--------------------------------------------------------------------#
@app.route("/admin/add_transaction_admin", methods=['POST','GET'])
def add_transaction_admin():
    services = mongo.db.services.find()
    suppliers = mongo.db.suppliers.find()
    requests = mongo.db.requests.find()
    return render_template("admin/add_transaction_admin.html", services=services, suppliers=suppliers, requests=requests)  
        

@app.route("/admin/insert_transaction_admin", methods=['POST'])
def insert_transaction_admin():
    mongo.db.transactions.insert_one(request.form.to_dict())
    return redirect(url_for('show_transactions_admin'))


    


  
   
 #-----------------------------------------------------#


@app.route("/admin/admin_delete_transaction", methods=[ "POST"] )
def delete_admin_transaction_admin():
    transaction_id = request.form['transaction_id']
    mongo.db.transactions.remove({"_id": ObjectId(transaction_id)})
    return redirect(url_for("get_transactions_admin"))

@app.route("/admin/get_graphs_admin", methods=['GET'])
def get_graphs_admin():
    graphs=mongo.db.transactions.find()
    return render_template("admin/show_graphs_admin.html" )


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


#---------------test code-------------------#



#------------------------------------------------#
