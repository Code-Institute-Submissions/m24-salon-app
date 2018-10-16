# Salon App
**Interactive Flask application**

To *request an appointment* the user can click on the <a href="http://m24-plug-humancode.c9users.io:8080/">*green button*</a> inside the home page .
<br/>He or she can<a href="http://m24-plug-humancode.c9users.io:8080/add_request_user"> *pick a date*</a> and give their contact details:name mobile & email address
and with a drop down menu choose what type of treatment.

Mean while back at the salon the administrator is able to see the in coming<a href="http://m24-plug-humancode.c9users.io:8080/admin/"> *Appointments*</a> on his or her device.
The administrator can call or message back by clicking one of the buttons. If the button *“whats app”* was clicked an *automatic message* is generated using the supplied data 
from the user, the administrator suggests a time buy amending the message before sending.
In the case that a client should want to book via telecon then the admin can press the small green + button and make a <a href="http://m24-plug-humancode.c9users.io:8080/admin/add_request_admin">*new appointment.*</a> 

After the user/client has received the treatment the admin/hair dresser can directly fill out
The transaction by going into admin/transactions and clicking on the (small green + button) a new transaction form will appear, the name of the client can be found under the dropdown menu.(Choose which client)
The exact treatment can be found in the drop down menu *Choose hair treatment*. 
The amount charged can be manually entered. 
A “Notes” field has been included to store any additional info about the treatment for example the exact colour mix last used.

In transactions you can add any type of payment received of payed out. In the drop down menu supplier you can choose your *trusted supplier* and also click on the link to
to make a quick order.

When the administrator/hairdresser clicks on graphs he or she can view
a bar chart showing each month’s turn over including expenditure. Beneath the barchart a pie chart shows proportional comparisons of each quarter. 
The JSON format dataset can be used to generate detailed excel spread sheets which can be then be sent on to the accountant.

This Web App was built as the second project for the Code Institute's classroom bootcamp. 
It is an app which uses html css and Pythons backend *Flask* framework and front-end framework is *Materialixe*. 

## Live Demo
<a href="http://m24-plug-humancode.c9users.io:8080/" >**Follow this link to view deployed version of the web app **</a>

## Components

#### Flask
A Python micro-framework that was used to serve the data and render the HTML pages for this Application

#### Python
A Python file name app.py renders index.html and builds a web server using pymongo to interact with MongoDB

#### MongoDB database

### Materialize

#### Queue.js
An asynchronour helper library for JavaScript

#### Crossfilter.js
A Javascript based data manipulation library that enables two way data binding - you will see this in action when a section of the piechart is clicked, the bar chart changes showing that particular quarter.

#### D3.js
A JavaScript based visualisation engine that renders interactive charts and graphs in svg format when given data, which are then passed in to divs in graphs.html

#### Dc.js
A Javascript based wrapper library for d3.js - makes plotting charts easier

## Deployment / Hosting

This Application was deployed and is hosted on Heroku - gunicorn Python package runs the http server for the app, 
the Procfile gives Heroku the information to run the app and requirements.txt is a file that contains all the Python packages (pip3 installs) required to run the app. mLab MongoDB was chosen to host the dataset on the server.

## Installation

Follow the below instructions to get this project up & running on Mac (commands will be slightly different for Windows)

1. Download MongoDB & Robomongo
2. Go to folder you want to put the cloned project in your terminal & type:
    `$ git clone https://github.com/steviebolton/m24-salon-app`
3. Create & Activate a new Virtual Environment in terminal:
    Create: `$ python3 -m venv ~/virtualenvs/name_of_environment`
    Activate: `$ source ~/virtualenvs/name_of_environment/bin/activate`
4. Install the project dependancies:
    `$ sudo pip3 install -r requirements.txt`
5. Get Mongod running
    `$ mongod --config config/mongoConfig.conf`
6. Open the folder in vscode and use the internal Terminal 
7. Navigate to the 'app.py', right click and select 'python3 app.py in terminal'
8. You should see it running below - go to your browser and type '127.0.0.1:5000' into the address bar and the application should appear

## Future updates

As yet this app does not yet have an admin login
but that can easily be solved by putting a password protection on the directory admin.
future features will be separated pages for incoming and out going transactions.


## Testing
This Application was tested across a range of browsers
it has gone through w3d.com and been put through various jasmin tests


## Graphic design front end
logo and layout was created by Steve Bolton,
The Company actually exists.

## Backend dev
Steve Bolton



