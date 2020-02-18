# Volunteer-Application

### Instructions for running the App

 Install requirements for the project:<br />
 pip install -r requirements.txt
 
 Execute the below command in MySQL:<br />
 CREATE DATABASE volunteer_db;
 
 Run the following commands to create required tables:<br />
 python db_manager.py init<br />
 python db_manager.py migrate<br />
 python db_manager.py upgrade
 
 Run the application:<br />
 python run.py
