# SCL-2022-DataPirates
A SCL project for guidance

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#development">Development</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing / Adding Features</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>


1. Backend Framework: **Django**
2. Front-end Framework: **Bootstrap**

## Installation 

1. Fork and Clone
    <ol>
    <li>Fork sushiksha-website the Repo</li>
    <li>Clone the repo to your computer.</li>
    </ol>

2. Create a Virtual Environment for the Project

    In Windows
    ```bash
    python -m venv venv
    
    venv\Scripts\activate
    ```

    In Ubuntu/MacOS
    ```bash
    python -m virtualenv venv
    
    source venv/bin/activate
    ```
   
   If you are giving a different name then `venv`, then please mention it in `.gitigonre` first

3. Install all the requirements

    ```bash
    pip install -r requirements.txt
    ```
   
4. Checkout to develop branch
     ```git
    git status
    git pull
    git branch
    git checkout develop
    
    ```
   
5.     
    Change the config parameters (Optional, only if you want to enable mail sending functionality)
    ```python
   
   SECRET_KEY = 'Enter random character string'
   EMAIL_USER = 'your email username'
   EMAIL_PASS = 'Enter you email password'
   SLACK_AUTH_TOKEN: "token here"

    ```
   
   comment line #45 (If you are using badge giving feature other leave as it is) of users/signals.py (send_email.delay(array)) during development and uncomment before sending PR
   

6. Make migrations/ Create db.sqlite3

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
7. Create a super user.
    In django if you want to access admin page, you need to create an account first.
    ```djangotemplate
    python manage.py createsuperuser
    ```
   Then select your username and password.
   
8. Run server
    ```bash
    python manage.py runserver
    ```
