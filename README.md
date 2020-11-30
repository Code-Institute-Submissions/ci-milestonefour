# [Fitness 2020](fitness-2020-milestonefour.herokuapp.com)

Code Institute Milestone Project Four

This is a Fitness Subscription App, for Full Stack Frameworsk with [Django](https://www.djangoproject.com/
 Milestone Four Project.

Fitness 2020, is an App built using the Django Framework with Python programming language.
Expand....

Throughout this project I have used [Python](https://www.python.org/), a high-end programming
language along with [Django](https://www.djangoproject.com/), a python framework.

The deployed site can be found at [Fitness 2020](fitness-2020-milestonefour.herokuapp.com).

## Table Of Contents

**1. [UX](#ux)**
  * [User Stories](#user-stories)
  * [Design](#design)
    * [Framework](#framework)
    * [Color Scheme](#color-scheme)
    * [Icons](#icons)
    * [Typography](#typography)
  * [Wireframes](#wireframes)

**2. [Features](#features)**

  * [Existing Features](#existing-features)
  * [Features Left to Implement](#features-left-to-implement)

**3. [Technologies Used](#technologies-used)**

  * [Front-End Technologies](#front-end-technologies)
  * [Back-End Technologies](#back-end-technologies)

**4. [Testing](#testing)**

**5. [Github Repository](#github-repository)**

**6. [Deployment](#deployment)**

  * [Local Deployment](#how-to-run-this-project-locally)
  * [Heroku Deployment](#heroku-deployment)

**7. [Credits](#credits)**

## UX
This project Fitness 2020 is to provide a Fitness Subscription Service to a user but also provide clothing essentials for 
anyone who like to keep fit or regularly attends a gym. 

### Target Audience

* People who like to keep fit or get in shape
* People who regularly work out or train
* People who like to eat right

## User Stories
Expand....

## Design
Expand....

### Framework

  * [Bootstrap 4](https://getbootstrap.com/)
  * [jQuery 3.4.1](https://code.jquery.com/jquery/)
  * [Django 3.1.3](https://www.djangoproject.com/)
  Expand....

### Color Scheme
Expand....

### Icons
Expand....

* [Font Awsome 5.11.2](https://fontawesome.com/)

### Typography
Expand....

### Wireframes
Expand....

## Features
Expand....

### Home app
Expand....

**index (Home Page)**

**contact.html**

**delivery.html**
 
**return.html**

### Products App
Expand....

**product.html**

**product_detail.html**

### Profile App
Expand....

### Shopping Bag App
Expand....

### Checkout App
Expand....

### Base Template
Expand....

**Navbar**

**Footer**

## Features Left to Implement
Expand....

## Technologies Used
  * [GitPod](https://gitpod.io/workspaces/) - The IDE used for developing this project.
  * [GitHub](https://github.com/) - Used to store and share all of the project code remotely.
  * [Balsamiq](https://balsamiq.com/) - Used to create the wireframes for this project.

**Front-End Technologies**
  * [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
  * [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3)
  * [jQuery 3.4.1](https://code.jquery.com/jquery/)
  * [Stripe](https://stripe.com/docs/api)
  * [AWS S3 Bucket](https://aws.amazon.com/)
  * [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
  * [Font Awsome](https://www.bootstrapcdn.com/fontawesome/)
  * [Bootstrap4](https://www.bootstrapcdn.com/)

  **Back-End Technologies**
  * [Python 3.6.7](https://www.python.org/) - Used as the back-end programming language for this project.
  * [Django](https://docs.djangoproject.com/) -  Used as a Python web framework.
  * [Heroku](https://www.heroku.com/) - Used for deployment of the final project.
  * [PostgreSQL](https://www.postgresql.org/) - Used as the relational SQL database plugin via Heroku.

 # Testing 
 Expand....

## Automated Testing
Expand....

### Validation Services

  * **HTML**: I have used [https://validator.w3.org/](https://validator.w3.org/) Used to validate the HTML code.

  * **CSS**: I have used [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/) Used to validate the CSS code.

  * **JavaScript**: I have used [https://jshint.com/](https://jshint.com/) Used to check the JavaScript code.

### Coverage
Expand....

## Manual Testing
Expand....

#### Stripe payment testing
Expand.... more

My checkout app is using the stripe payment for the payment option. I tested this by using Stripes
test card (4242 4242 4242 4242) I tested the forms and ensured all my validation worked as expected
and my logic was performing as expected. The checkout app works from the Stripe API.

Card number - 4242424242424242

CVC - Any 3 digit number.

Expiry date - Any date in the future.

### Responsiveness
Expand....

### Known Bugs
Expand....

### GitHub Repository
Check and Expand....

1. Created a repository in GitHub called: mattjboland/ci-milestonefour

2. Initialised git from the terminal using Git Bash:

    git init

3. Created a .gitignore file and I have added the files and folders that won't need to push
to GitHub (i.e. .theia, .gitpod, .dockerfile, .gitpod.yml, env.py, __pycache__/, *.sqlite3, *.pyc)

4. Added the files that I was working on to the Staging area by using:

   git add .

5. Run the commit command with the first commit

  git commit -m “initial commit"

6. Copied from GitHub the following path and I ran it in the Git Bash terminal in order to
indicate where my remote repository is.

 git remote add origin 
 
 git push -u origin master

7. I've run regular commits after every important update to the code, and I pushed the changes
to GitHub using a chained command.

git add .; git commit -m "Commit message"; git push

## Deployment
Expand....

### How to run this project locally
Expand....

### Heroku Deployment
Check and Expand....

To deploy Fitness 2020 to heroku, use the following process:

1. Create a requirements.txt file using the terminal command pip freeze > requirements.txt.

2. Create a Procfile with the terminal command echo web: python app.py > Procfile.

3. git add and git commit the new requirements and Procfile and then git push the project 
to GitHub.

4. Sign up for a free Heroku account, Create a new app on the Heroku website by clicking the 
"New" button in your dashboard. Give it a name and set the region to Europe.

5. From the heroku dashboard of your newly created application, click on "Deploy" > 
"Deployment method" and select GitHub, and enable Automatic Deployment.

6. In the Heroku Resources tab, navigate to the Add-Ons section and search for Heroku Postgres. 
Select the free Hobby level. This will allow you to have a remote database instead of using the 
local sqlite3 database, and can be found in the Settings tab. You'll need to update your .env 
file with your new database-url details. Confirm the linking of the heroku app to the correct 
GitHub repository.

7. In the heroku dashboard for the application, click on settings tab and then click on the 
Reveal config vars button to configure environmental variables.

Set the following config vars:

Key	                        Value                    

8. In the Heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.

## Credits
Expand....

**Content**

All the product details, images and the contents are from https://www.zalando.ie/men-home/ and I modifed to use in the project.

**Tutorials**
Expand....

* [Python Django Tutorial by Corey Schafer](https://www.youtube.com/watch?v=F5mRW0jo-U4)

* [Django Tutorial // Build a Video Subscription Website](https://www.youtube.com/watch?v=zu2PBUHMEew)

* [Django and Stripe subscriptions — Part 1](https://medium.com/analytics-vidhya/how-to-build-a-django-membership-site-with-payment-integration-part-1-163552292aed)

* The [Django documentation](https://devdocs.io/django~1.11/)

### Acknowledgement
Expand....

**Disclaimer**
Expand....

 The content of this website is for educational purposes only.