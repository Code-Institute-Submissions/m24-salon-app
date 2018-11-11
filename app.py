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
    
    
@app.route("/admin/show_graphs")
def show_graphs():
    total_income = 0.0
    total_outgoing = 0.0
    transactions = mongo.db.transactions.find()
    for transaction in transactions:
        total_income += transaction['moneyin']
        total_outgoing += transaction['moneyout']
    balance = total_income - total_outgoing
    return render_template("admin/show_graphs.html", transactions=transactions, total_income=total_income, total_outgoing=total_outgoing, balance=balance)        

@app.route("/admin/get_graphs", methods=['GET'])
def get_graphs():
    graphs=mongo.db.transactions.find()
    return render_template("admin/show_graphs.html" )

@app.route("/admin/show_transactions")
def show_transactions():
    transactions=mongo.db.transactions.find()
    services=mongo.db.services.find()
    appointments=mongo.db.appointments.find()
    suppliers=mongo.db.suppliers.find()
    return render_template("admin/show_transactions.html", transactions=transactions, services=services, appointments=appointments, suppliers=suppliers)        

       
@app.route("/admin/add_transaction", methods=['POST','GET'])
def add_transaction():
    transactions=mongo.db.transactions.find()
    services=mongo.db.services.find()
    appointments=mongo.db.appointments.find()
    suppliers=mongo.db.suppliers.find()
    return render_template("admin/add_transaction.html", transactions=transactions, services=services, suppliers=suppliers, appointments=appointments)  

@app.route("/admin/insert_transaction", methods=['POST'])
def insert_transaction():
    mongo.db.transactions.insert_one(request.form.to_dict())
    return redirect(url_for('show_transactions'))
 
@app.route('/admin/edit_transaction/<transaction_id>', methods=['GET','POST'])
def edit_transaction(transaction_id):
    return render_template('admin/edit_transaction.html', 
    transaction=mongo.db.transactions.find_one({'_id': ObjectId(transaction_id)}))

@app.route('/admin/confirm_delete_transaction/<transaction_id>') 
def confirm_delete_transaction(transaction_id):
    transaction = mongo.db.transactions.find_one({'_id': ObjectId(transaction_id)})
    return render_template('admin/confirm_delete_transaction.html', transaction=transaction) 
    
@app.route('/admin/delete_transaction/<transaction_id>', methods=["GET","POST"]) 
def delete_transaction(transaction_id):
    mongo.db.transactions.remove({'_id': ObjectId(transaction_id)})
    return redirect(url_for("show_transactions"))
   
@app.route("/admin/update_transaction/<transaction_id>", methods=['POST'])
def update_transaction(transaction_id):
    transaction = mongo.db.transactions
    transaction.update({"_id": ObjectId(transaction_id)}, request.form.to_dict())
    return redirect(url_for("show_transactions")) 
    

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
    
@app.route("/add_appointment_user")
def add_appointment_user():
    services = mongo.db.services.find()
    return render_template('add_appointment_user.html', services=services)

@app.route("/insert_appointment_user", methods=['POST'])
def insert_appointment_user():
    mongo.db.appointments.insert_one(request.form.to_dict())
    return redirect(url_for('get_index'))

@app.route("/admin/")
def get_appointments():
    appointments=mongo.db.appointments.find()
    return render_template("admin/show_appointments.html", appointments=appointments)

@app.route("/admin/filter_today")
def filter_today():
    todays_date = datetime.datetime.today().strftime('%-d %B, %Y')
    filtered_appointments = mongo.db.appointments.find({"due_date": todays_date})
    return render_template("admin/show_appointments.html", appointments=filtered_appointments)    

@app.route('/admin/edit_appointment/<appointment_id>', methods=['GET','POST'])
def edit_appointment(appointment_id):
    return render_template('admin/edit_appointment.html', 
    appointment=mongo.db.appointments.find_one({'_id': ObjectId(appointment_id)}))
    
@app.route("/admin/update_appointment/<appointment_id>", methods=['POST'])
def update_appointment(appointment_id):
    appointments = mongo.db.appointments
    appointments.update({"_id": ObjectId(appointment_id)}, request.form.to_dict())
    return redirect(url_for("get_appointments"))
    
@app.route('/admin/confirm_delete_appointment/<appointment_id>', methods=["GET","POST"]) 
def confirm_delete_appointment(appointment_id):
    appointment = mongo.db.appointments.find_one({'_id': ObjectId(appointment_id)})
    return render_template('admin/confirm_delete_appointment.html', appointment=appointment)        
    
@app.route('/admin/delete_appointment/<appointment_id>') 
def delete_appointment(appointment_id):
    mongo.db.appointments.remove({'_id': ObjectId(appointment_id)})
    return redirect(url_for("get_appointments"))   
   
@app.route("/admin/insert_appointment", methods=['POST'])
def insert_appointment():
    mongo.db.appointments.insert_one(request.form.to_dict())
    return redirect(url_for('get_appointments'))
    
    
    
     

@app.route("/admin/add_appointment")
def add_appointment():
    services = mongo.db.services.find()
    appointment = mongo.db.appointments.find()
    return render_template('admin/add_appointment.html', services=services , appointment=appointment)
    
    

   
    
    
    
    
    
    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)



