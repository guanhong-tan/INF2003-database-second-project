## StressBook
StressBook is a streamlined database-focused project to analyze and optimize performance, speed, and memory usage in an event booking system. This project simulates a concert booking environment, emphasizing efficient data management and high-performance querying under load. The project inspiration comes from a friend that complains about the hardship of booking a popular concert.  

## Prerequisite Software
1. Python
2. MongoDB
3. Install packages from requirements.txt

## Getting Started:
### Step 1: Download The Virutal Package In Your Computer
```bash
pip install virtualenv
```
or
```bash
py -m pip install virtualenv
```

### Step 2: Change To The Project Folder Directory (Note: Everyone Project Folder Directory Is Different) 
```bash
cd C:\Users\PC\Desktop\booking_system\INF2003-database-second-project
```

### Step 3 : Create Virtual Environment (Note: env is the name for our environment, it can be venv too, just a name)
```bash
py -m venv env 
```

### Step 4 : Activate Virutal Environment 
Operating System : Window
```bash
env\Scripts\activate
```
Operating System : MacOS
```bash
source env/bin/activate
```

### Step 5: Install Required Packages From Requirements.txt

```bash
pip install -r requirements.txt
```
or
```bash
py -m pip install -r requirements.txt
````

### Step 6: To Run The Flask Project
Change To The Project Directory
```bash
cd stressbook
```
Run The Project
``` bash
py main.py
```
or 
```bash
flask --app main --debug run
```


### Self Note For Future Self When Creating Virtual Environment
1. After step 4, you pip install the packages that you needed for the project
2. Pip freeze > requirements.txt (Create the requirements.txt file, inside contains all the packages and the respective versions)
3. Proceed to step 5 for the people who have pulled the project and created the virutal environment.
