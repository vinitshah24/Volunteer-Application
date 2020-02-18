# Volunteer-Application

### Instructions for running the App

 Install requirements for the project:
 pip install -r requirements.txt
 
 Execute the below command in MySQL:
 CREATE DATABASE volunteer_db;
 
 Run the following commands to create required tables:
 python db_manager.py init
 python db_manager.py migrate
 python db_manager.py upgrade
 
 Run the application:
 python run.py
