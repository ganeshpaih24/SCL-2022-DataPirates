# SCL-2022-DataPirates
A SCL project for guidance

<p align="center"> 
 <img src="https://i.ibb.co/bzCVQyz/Walkthrough-Logo.png" alt="Walkthrough-logo" border="0" width=300 height=300/>&nbsp; </a></p>


<p class="text-center mb-3" align="center">
<a href="https://walkthrough-datapirates.herokuapp.com/"><img src="https://forthebadge.com/images/badges/made-with-python.svg" border="0" title="Made with Python" /></a>
</p>

<p class="text-center mb-3" align="center">
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif" border="0" alt="Powered by Django." title="Powered by Django." /></a>
</p>

Using this platform ‘WalkThrough’ making roadmaps can be much easier than the traditional method. It helps in making creative roadmaps and is easy to make even for users who are new to this platform. It allows people who are new to sign up and create a new account whereas people who already have existing accounts can sign in to create roadmaps or search for roadmaps they are interested in. Creating roadmaps gives the users a clear vision and helps them establish their goals. This will allow them to start moving ahead in the direction of the goals they want to achieve.


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
  </ol>
</details>


1. Backend Framework: **Django**
2. Front-end Framework: **Bootstrap**

## Installation 

1. Fork and Clone
    <ol>
    <li>Fork the Repo</li>
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
   
   
   comment line #45 (If you are using badge giving feature other leave as it is) of users/signals.py (send_email.delay(array)) during development and uncomment before sending PR
   

5. Make migrations/ Create db.sqlite3

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Create a super user.
    In django if you want to access admin page, you need to create an account first.
    ```djangotemplate
    python manage.py createsuperuser
    ```
   Then select your username and password.
   
7. Run server
    ```bash
    python manage.py runserver
    ```
