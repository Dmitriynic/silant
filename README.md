<h2 align="center">Forkit maintenance service for Silant company</h2>
<p aling="center">
   <img src="https://i.ibb.co/Xt153sR/Logotype-accent-RGB-2.jpg">
</p>
<p align="center">
   <img alt="Static Badge" src="https://img.shields.io/badge/Python-3.9.13-red">
   <img alt="Static Badge" src="https://img.shields.io/badge/Django-4.2.6-blue">
   <img alt="Static Badge" src="https://img.shields.io/badge/License-MIT-green">
</p>

## Descriptions

The service stores the following data about Silant warehouse
equipment:
<ul>
<li>loader equipment</li>
<li>place of use</li>
<li>maintenance, breakdowns and repairs</li>
</ul>

The service emplements authorization, including
various roles: guest, client, service organization
and manager.

The client has access to data from certain machines.
Each machine has only one client.

The service organization has access to the data of certain machines.
Each car has only one service organization.

The manager has access to data on all machines, and alse
has the ability to edit directories.

## Functionality

The service has different functionality for users with different roles.
Key functionality: issuing information about cars in the form of tables from databases(technical characteristics,
maintenance, advertising, etc.).

The service displays data from the database in tabular form
depends on the level of user access rights.

Tables' data sorts by default for fields:
<ul>
<li>"factory shipment date" for the "machine" table</li>
<li>"date of maintenance" for the table "maintenance"</li>
<li>"date of refusal" for the "complaints" table</li>
</ul>

Tables have a filtering function based on the following fields:
<ul>
<li>model of equipment</li>
<li>engine model</li>
<li>transmission model</li>
<li>steering axle model</li>
<li>drive axle model for the "Machine" table</li>
<li>type of maintenance</li>
<li>serial number of the car</li>
<li>service company of the "Maintenance" table</li>
<li>failure node</li>
<li>recovery method</li>
<li>service company for the "Complaints" table</li>
</ul>

The rows in the table are clickable and lead 
to a page displaying complete data, including the "description"
field of entities that are specified in directories.

Authorization is carried out using a login/password assigned
by the system administrator. The user can't independently change
the login and/or password.

A user without authorization can obtain limited information about the equipment of a machine by entering its serial number. This type of user has access to a field for entering the serial number of the machine and a search button.

Search result: a table with data for a specific car with the following fields: table “Machine” (fields 1–10). 
If data on the serial number is not found, a message is displayed that there is no data about the car with that serial number in the system.

Authorized users have different access to data and receive tables with data about all machines available to them.

The data is located on several tabs (according to the tables “Machine”, “Maintenance”, “complaints”):
<ul>
<li><a href="https://ibb.co/sq1LV7s">machine</a></li>
<li><a href="https://ibb.co/QXzm8VR">maintenance</a></li>
<li><a href="https://ibb.co/sv4zgpH">complaints</a></li>
</ul>

<a href="https://i.ibb.co/DR8pSkv/2023-10-31-22-33-48.png">Data's model</a>

<a href="https://i.ibb.co/K054sF3/2023-10-31-22-33-56.png">Machine life cycle</a>

## How to run

`python -m venv venv`

Windows:
`venv\scripts\activate`

Linux and macOs:
`source venv/bin/activate`

`pip install django`

`pip install django-filters`

`cd silant`

`python manage.py runserver`
