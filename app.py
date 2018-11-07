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



@app.route("/data")
def get_data():
    transactions = mongo.db.transactions.find({}, {'_id': False})
    list_transactions = []
    for t in transactions:
        list_transactions.append(t)
    return json.dumps(list_transactions)
    
    
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

@app.route("/admin/get_graphs_admin", methods=['GET'])
def get_graphs_admin():
    graphs=mongo.db.transactions.find()
    return render_template("admin/show_graphs_admin.html" )

@app.route("/admin/show_transactions_admin")
def show_transactions_admin():
    transactions=mongo.db.transactions.find()
    services=mongo.db.services.find()
    requests=mongo.db.requests.find()
    suppliers=mongo.db.suppliers.find()
    return render_template("admin/show_transactions_admin.html", transactions=transactions, services=services, suppliers=suppliers, requests=requests)        

@app.route("/update_transaction_admin/<transaction_admin_id>", methods=['POST'])
def update_transaction_admin(transaction_admin_id):
    transactions = mongo.db.transactions
    transactions.update({"_id": ObjectId(transaction_admin_id)}, request.form.to_dict())
    return redirect(url_for("get_transaction"))        

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


    
    

    

@app.route('/admin/confirm_delete_transaction/<transaction_id>') 
def confirm_delete_transaction(transaction_id):
    transaction = mongo.db.transactions.find_one({'_id': ObjectId(transaction_id)})
    return render_template('admin/confirm_delete_transaction.html', transaction=transaction) 
    
    
@app.route('/admin/delete_transaction_admin/<transaction_id>', methods=["GET","POST"]) 
def delete_transaction_admin(transaction_id):
    mongo.db.transactions.remove({'_id': ObjectId(transaction_id)})
    return redirect(url_for("show_transactions_admin"))
   
  

    
    

    

@app.route('/admin/get_services')
def get_services():
    return render_template('admin/show_services.html',
    services=mongo.db.services.find())
    
@app.route('/admin/new_service')
def new_service():
    return render_template('admin/addservice.html')

@app.route('/admin/insert_service', methods=['POST'])
def insert_service():
    services = mongo.db.services
    services.insert_one(request.form.to_dict())
    return redirect(url_for('get_services'))
    
@app.route('/admin/edit_service/<service_id>')
def edit_service(service_id):
    return render_template('admin/edit_service.html',
    service=mongo.db.services.find_one({'_id': ObjectId(service_id)}))

@app.route('/admin/update_service/<service_id>', methods=['POST'])
def update_service(service_id):
    mongo.db.services.update(
        {'_id': ObjectId(service_id)},
        {'service_name': request.form['service_name']})
    return redirect(url_for('get_services'))
    
@app.route('/admin/confirm_delete/<service_id>') 
def confirm_delete(service_id):
    service = mongo.db.services.find_one({'_id': ObjectId(service_id)})
    return render_template('admin/confirm_delete_service.html', service=service)

@app.route('/admin/delete_service/<service_id>') 
def delete_service(service_id):
    mongo.db.services.remove({'_id': ObjectId(service_id)})
    return redirect(url_for("get_services"))
    
    


@app.route('/admin/get_suppliers')
def get_suppliers():
    return render_template('/admin/show_suppliers.html',
    suppliers=mongo.db.suppliers.find())
    
@app.route('/admin/new_supplier')
def new_supplier():
    return render_template('admin/addsupplier.html')

@app.route('/admin/insert_supplier', methods=['POST'])
def insert_supplier():
    suppliers = mongo.db.suppliers
    suppliers.insert_one(request.form.to_dict())
    return redirect(url_for('get_suppliers'))

@app.route('/admin/edit_supplier/<supplier_id>')
def edit_supplier(supplier_id):
    return render_template('admin/edit_supplier.html',
    supplier=mongo.db.suppliers.find_one({'_id': ObjectId(supplier_id)}))

@app.route('/admin/update_supplier/<supplier_id>', methods=['POST'])
def update_supplier(supplier_id):
    mongo.db.suppliers.update(
        {'_id': ObjectId(supplier_id)},
        {'supplier_name': request.form['supplier_name']})
    return redirect(url_for('get_suppliers'))

@app.route('/admin/confirm_delete_supplier/<supplier_id>') 
def confirm_delete_supplier(supplier_id):
    supplier = mongo.db.suppliers.find_one({'_id': ObjectId(supplier_id)})
    return render_template('admin/confirm_delete_supplier.html', supplier=supplier)

@app.route('/admin/delete_supplier/<supplier_id>') 
def delete_supplier(supplier_id):
    
    mongo.db.suppliers.remove({'_id': ObjectId(supplier_id)})
    return redirect(url_for("get_suppliers"))
    

    
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

@app.route("/admin/filter_today")
def filter_today_admin():
    todays_date = datetime.datetime.today().strftime('%-d %B, %Y')
    filtered_requests = mongo.db.requests.find({"due_date": todays_date})
    return render_template("admin/show_appointments_admin.html", requests=filtered_requests)    

@app.route('/admin/edit_request/<request_id>', methods=['GET','POST'])
def edit_request(request_id):
    return render_template('admin/edit_appointment.html', 
    request=mongo.db.requests.find_one({'_id': ObjectId(request_id)}))
    
@app.route("/admin/update_request_admin/<request_id>", methods=['POST'])
def update_request_admin(request_id):
    requests = mongo.db.requests
    requests.update({"_id": ObjectId(request_id)}, request.form.to_dict())
    return redirect(url_for("get_requests_admin"))
    
@app.route('/admin/confirm_delete_appointment/<request_id>', methods=["GET",""]) 
def confirm_delete_appointment(request_id):
    request = mongo.db.requests.find_one({'_id': ObjectId(request_id)})
    return render_template('admin/confirm_delete_appointment.html', request=request)        
    
@app.route('/admin/delete_request_admin/<request_id>', methods=["GET","POST"]) 
def delete_request_admin(request_id):
    mongo.db.requests.remove({'_id': ObjectId(request_id)})
    return redirect(url_for("get_requests_admin"))   
   
@app.route("/admin/insert_request_admin", methods=['POST'])
def insert_request_admin():
    mongo.db.requests.insert_one(request.form.to_dict())
    return redirect(url_for('get_requests_admin'))

@app.route("/admin/add_request")
def add_request():
    services = mongo.db.services.find()
    return render_template('admin/add_appointment_admin.html', services=services)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)



