# Salon App
**Interactive Flask application**

To *request an appointment* the user can click on the <a href="http://m24-hairsalon-app.herokuapp.com/"> *Appointments*</a> on his or her device.
The administrator can call or message back by clicking one of the buttons. If the button *“whats app”* was clicked an *automatic message* is generated using the supplied data 
from the user, the administrator suggests a time buy amending the message before sending.
In the case that a client should want to book via telecon then the admin can press the small green + button and make a <a href="http://m24-hairsalon-app.herokuapp.com/admin/">*new appointment.*</a> 

After the user/client has received the treatment the admin/hair dresser can directly fill out
The transaction by going into admin/transactions and clicking on the (small green + button) a new transaction form will appear, the name of the client can be found under the dropdown menu.(Choose which client)
The exact treatment can be found in the drop down menu *Choose hair treatment*. 
The amount charged can be manually entered. 
A “Notes” field has been included to store any additional info about the treatment for example the exact colour mix last used.

In transactions you can add any type of payment received of payed out. In the drop down menu supplier you can choose your *trusted supplier* and also click on the link to
to make a quick order.

When the administrator/hairdresser clicks on graphs he or she can view
a bar chart showing each month’s turn over including expenditure. Beneath the barchart a pie chart shows proportional comparisons of each quarter. 
The JSON format dataset can be used to generate detailed excel spread sheets which can then be sent on to the accountant.

 

## Live Demo
<a href="https://m24-hairsalon-app.herokuapp.com/" >**Follow this link to view deployed version of the web app **</a>

## Components
This Web App was built using html css and front-end framework *Materialixe*, the backend uses microframework *Flask*. 


#### Flask
Is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.

#### Python
A Python file name app.py renders index.html and builds a web server using pymongo to interact with MongoDB

#### MongoDB database
stores data in flexible, JSON-like documents, meaning fields can vary from document to document and data structure can be changed over time

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
the Procfile gives Heroku the information to run the app. Requirements.txt is a file that contains all the Python packages (pip3 installs) required to run the app. mLab MongoDB was chosen to host the dataset on the server.

## Installation

Follow the below instructions to get this project up & running on Mac (commands will be slightly different for Windows)
## Local deployment
Clone the github repository or download the zipfile.
Go to https://mlab.com register create a db name it m24_salon_app
in the database you have created  click on add collection and make the following tables:
requests
services
suppliers
transactions

create some data manualy within the collections to start the ball rolling.
send me an email request for the db code if you need it.

When your database has been created you will see somthing like this in your mongodb mongo homepage:

mongo ds111072.mlab.com:??????/m24_salon_app -u <dbuser> -p <dbpassword>
mongodb://<dbuser>:<dbpassword>@ds111072.mlab.com:???????/m24_salon_app


## Delpoyment to Heruku
If you haven't already, log in to your Heroku account and follow the prompts below to create a new SSH public key:
* $ heroku login
Clone the repository
Use Git to clone m24-hairsalon-app's source code to your local machine.
* $ heroku git:clone -a m24-hairsalon-app
* $ cd m24-hairsalon-app
Deploy your changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.
* $ git add .
* $ git commit -am "make it better"
* $ git push heroku master

That's it.

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



