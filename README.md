# GiveWay Volunteer Application

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### :star: Backend: Python Flask
Create virtual environment for the application:<br />
```
virtualenv app
```
 
Source scripts to activate the virtualenv:<br />
```
source Scripts/activate
```
 
Install requirements for the project:<br />
```
pip install -r requirements.txt
```
 
Run the following commands to create required tables:<br />
```
python db_manager.py
```
 
Run the application:<br />
```
python run.py
```
### :star:	Frontend: Vue.js
Install the dependencies:<br />
```
npm install
```

Start the local server:<br />
```
npm run serve
```

Navigate to your localhost on port 8080 in your browser:<br />
```
localhost:8080
```