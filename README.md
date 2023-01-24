# SCL-2022-DataPirates


<p align="center"> 
 <img src="https://i.ibb.co/bzCVQyz/Walkthrough-Logo.png" alt="Walkthrough-logo" border="0" width=300 height=300/>&nbsp; </a></p>


<p class="text-center mb-3" align="center">
<a href="https://walkthrough-datapirates.herokuapp.com/"><img src="https://forthebadge.com/images/badges/made-with-python.svg" border="0" title="Made with Python" /></a>
</p>

<p class="text-center mb-3" align="center">
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif" border="0" alt="Powered by Django." title="Powered by Django." /></a>
</p>

A Sushiksha Coding League project for guidance. Using this platform ‘WalkThrough’ making roadmaps can be much easier than the traditional method. It helps in making creative roadmaps and is easy to make even for users who are new to this platform. It allows people who are new to sign up and create a new account whereas people who already have existing accounts can sign in to create roadmaps or search for roadmaps they are interested in. Creating roadmaps gives the users a clear vision and helps them establish their goals. This will allow them to start moving ahead in the direction of the goals they want to achieve.




1. Backend Framework: **Django**
2. Front-end Framework: **Bootstrap**

## Features
1. User Registration and Login
2. Roadmap Creation and Updation
3. Search for Roadmaps through Categories and Titles
4. Subpost feature(Steps inside a Roadmap)
4. Star Feature
5. Follow Roadmap authors
6. Comment feature under each Roadmap
7. User Profile Creation and Updation

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

## Screenshots

- Landing Page
<img src="https://i.postimg.cc/SNrKJwKf/Screenshot-20230124-124553.png" alt="Landing Page">

- Explore Page(Displays all Roadmaps)
<img src="https://i.postimg.cc/sxmnbpYS/Screenshot-20230124-141935.png" alt="Explore Page">

- Register Page
<img src="https://i.postimg.cc/T3kgWt9B/Screenshot-20230124-142038.png" alt="Register Page">

- Login Page
<img src="https://i.postimg.cc/0jbDnDyc/Screenshot-20230124-142107.png" alt="Login Page">

- Author Profile Page
<img src="https://i.postimg.cc/QCVsMkXg/Screenshot-20230124-143820.png" alt="Profile Page">

- Home Page(Displays Roadmaps of following authors)
<img src="https://i.postimg.cc/YqGGnQ1m/Screenshot-20230124-143920.png" alt="Home Page">

- Roadmap Creation Page
<img src="https://i.postimg.cc/vZGvpPXN/Screenshot-20230124-154310.png" alt="Roadmap Creation Page">

- Edit Profile Page
<img src="https://i.postimg.cc/GpwTW9ch/Screenshot-20230124-160500.png" alt="Edit Profile Page">

- Roadmap Details Page
<img src="https://i.postimg.cc/4NGtdBqb/Screenshot-20230124-160736.png" alt="Roadmap Details Page">

- Comments Feature
<img src="https://i.ibb.co/t3Tgshd/Screenshot-20230124-170657.png" alt="Comments Feature">
