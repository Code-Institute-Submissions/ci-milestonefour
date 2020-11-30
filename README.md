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

* For people who like to keep fit or get in shape.
* For people who regularly work out or train.
* For people who like to eat right when training.
* For people who like to buy clothes for training etc.
* For people that want quick easy exercise plans.
* For people who want meal plans to suit their training regime.

## User Stories

* As a user I want to access all products on a webite.
* As a user I want to be able to browse a site easily.
* As a user I want to be able to purchase items quickly and easily.
* As a user I want to be able to purchase without having to log in.
* As a user I want to be able to have the option to register.
* As a user who is registered I want to be able to have an account.
* As a user who is registered I want to be able to log in and out easily.
* As a user I want to be able to seatch for particular products.
* As a user I want to be able to avail of free delivery when ordering.

## Design
I wanted to create a user friendly site the was easily navigated by users with a
design was visually appealing to the user.

### Framework

  * [Bootstrap 4](https://getbootstrap.com/)
  I used Bootstrap as the front end framework as I was familar with this framework as I have
  used before on other project. I like that it is easy to use and easy to style to suit the needs
  of any project.
  * [jQuery 3.4.1](https://code.jquery.com/jquery/)
  I used this to initialise some Bootstrap components and scripts where JavaScript wasnt needed.
  * [Django 3.1.3](https://www.djangoproject.com/)
  This was used for Back-End to tie in with the Front-End Bootstrap. I wasnt as familar with this
  but lessons through the course help me become some what familar. The rest was learned as I 
  proceeded building the project.

### Color Scheme
I went with a basic Black and White Color Scheme for most the pages in this site. I wanted to stay 
away from bright colors to help decrease and distraction a user might encounter. This also helps
the user to maybe purchase an item rather than leave the site. I used A simple background image 
to display in the backgound which keeps within the theme of the project.

### Icons

* [Font Awesome 5.11.2](https://fontawesome.com/)
I used Font Awesome Icons as again I was familar using these and they help to bring a site to life.
These were used in the Nav Bar, for social links int the footer. Tags for products, subtle icons on
buttons etc.

### Typography
I used Google Font Gloria Hallelujah as I like this font and believe it works well with theme of this
project.

### Wireframes
I used Balsamiq for the wireframes for this project during the planning stages. I tried to stick to
them as best as possible but during the course of the development slight changes or improvements
were made.

## Features
This project features apps (applications) created by using Django command **python3 manage.py startapp nameofapp**

### Home app
The home app includes the Homepage for the site index.html and the contact, return and delivery pages.

**index (Home Page)**
This is the main homepage for the site. This is where users and start to navigate through the site and
begin to search for products or subscriptons that are available to purchase.

**contact.html**
This is the contact page where users can see the contact details for the site, address, phone number etc.

**delivery.html**
 
**return.html**
This is the returns policy page where users can see the terms and conditions of returning products and getting 
refunds.

### Products App
The products app has all the products and subscriptions for the site.

**product.html**

This page displays all the clothing products available to purchase. All items have a description and an image.
Each product has a price and a rating. Clicking on the items brings the user to the following detail page.

**product_detail.html**

This page displays the individual product, where it displays a good clear image of the product and a description.
The user can then select the products size and a quantity they wish to add to the shopping bag. Or they can 
continue to browse by clicking the Keep Shopping button.

**subscriptions.html**

Much the same as the product.html page but this displays only the subscriptions available. Again clicking on
the items brings the user to the following subscripton detail page.

**subscription_detail.html**

This page displays the individual subscripton, where it displays a description. The user can then select the 
subscripton they wish to add to the shopping bag. Or they can continue to browse by clicking the Keep Shopping button.

**add_product.html**

This page is reserved for the shop owner to add more products to the site.

**edit_product.html**

This page is also reserved for the shop owner to edit products on the site.

### Profiles App
The profiles app is for registered users who have signed up and created an account. It displays the users profile and details
which can be updated at anytime. This page also provides the user with an order history where they can views past orders.

### Shopping Bag App
The shopping bag app features a summary of all the items added to the shopping bag. This includes the image of the
item, title and the price. A quantity field is displayed with each item in the bag, giving the ability to adjust the
quantity in their cart. The user can also see the total of the shopping bag and this will be updated when the user updates
the quantity in their shopping bag. This also tells the user in order to recieve free delivery they user needs to spend
another calculated total to bring it above the ammount that qualifies for free delivery. Alternatively it provides
an estimated cost of delivery.

### Checkout App
The checkout app allows the user to successfully checkout and purchase items in the shopping bag.

**checkout.html**

This page displays what is in the shopping bag and give the ability to purchase items safely and securely with Stripe. 
This page allows allows the user to save information for future purchases. When payments are made there are notifications
that pop up when payment is successful or if there is a problem with either the payment or a filed on the form. These are 
easy for the user to see and correct when and where necessary.

**checkout_success.html**

This page is displayed when a user successfully makes a purchase. It gives the user an order confirmation with order
number and date of the order. How much was charged to your card, a summary of item or items purchased and the delivery
information. It also tell the user that a confirmation email was sent to confirm the purchase with all details.

### Base Template
The base template is a template of features that will be extended to all pages within the site.

**Navbar**

The Navbar is a Bootstrap Navbar with mobile Navbar included. This was based on the sample from Code Institute but 
styled to suit the theme of this site. 

It features the name of the site which is also a home button to help user navigate abck to the home view. It also has
a search feature where users can search for particular products of interest. On the far right it has a dropdown for 
My Account, where users can register, log in and log out. It also has a link to the shopping bag which displays
the value of any contents that maybe in the shopping bag.

Then it has nav links for all products subscriptions clothing and special offers if there are any. This allows users
to navigate to particular pages within the site to view or purchase items as needed. Then directly below that a nice 
feature that explains to users that there is free delivery on all order above €50.

**Footer**

The Footer was based from two different examples and styed to suit the theme of this site. 

It has links to various pages within the site some social media links and the name of the site.

## Features Left to Implement
As I was under time restraints there are some features I would have like to include but didnt have the right amount 
of time to include.

1. The ability to track users subscribing the the site, or for sessions or subscriptions.
2. Better filtering of the products and subscriptions.
3. The ability for users to rate or favourite items on the site.
4. To include a contact us form on the contact page.
5. Delivery policy page.

## Technologies Used
  * [GitPod](https://gitpod.io/workspaces/) - The IDE used for developing this project.
  * [GitHub](https://github.com/) - Used to store and share all of the project code remotely.
  * [Balsamiq](https://balsamiq.com/) - Used to create the wireframes for this project.

**Front-End Technologies**
  * [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
  * [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3)
  * [jQuery 3.5.1](https://code.jquery.com/jquery/)
  * [JavaScript](https://www.javascript.com/)
  * [Stripe](https://stripe.com/docs/api)
  * [AWS S3 Bucket](https://aws.amazon.com/)
  * [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
  * [Font Awesome](https://www.bootstrapcdn.com/fontawesome/)
  * [Bootstrap4](https://www.bootstrapcdn.com/)

  **Back-End Technologies**
  * [Python 3.6.7](https://www.python.org/) - Used as the back-end programming language for this project.
  * [Django](https://docs.djangoproject.com/) -  Used as a Python web framework.
  * [Heroku](https://www.heroku.com/) - Used for deployment of the final project.
  * [PostgreSQL](https://www.postgresql.org/) - Used as the relational SQL database plugin via Heroku.

# Testing 

## Automated Testing
Automated testing is implemented to support manual testing during the development process.
The intent was not to achieve 100% coverage with automated testing as I am limited to time contraints
but on average this seems to be quite difficult to achieve.

Unit tests can be found in the the products app in test folder, test_admin.py, test_models.py, test_views.py,
test_forms.py files. Note: The tests should be added in local database, as The Heroku
hobby-tier does not give permissions to allow creation of databases that are required for python automated
testing. To run the test and check the output, the database (Postgres) code configuration in settings.py
should be temporarily commented out.

**Command used to run the tests:**

``python3 manage.py test``

### Coverage

Coverage was used to get the feedback during the testing and see the percentage of the unit tests implemented.
to generate a coverage report run the following command: 

``coverage report``

To generate the HTML file run the following command:

``coverage html ``

Then open index.html file in the newly created
directory, run the file in the browser to see the output.

### Validation Services

  * **HTML**: I have used [https://validator.w3.org/](https://validator.w3.org/) Used to validate the HTML code.

  * **CSS**: I have used [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/) Used to validate the CSS code.

  * **JavaScript**: I have used [https://jshint.com/](https://jshint.com/) Used to check the JavaScript code.

## Manual Testing
Expand....

#### Stripe payment testing

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

## Deployment

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

### How to run this project locally
The Fitness 2020 project was developed using the online IDE GitPod and using Git and GitHub for
version control. It is hosted on Heroku with static files and media files hosted in AWS S3 Bucket.

### Heroku Deployment

To deploy Fitness 2020 to heroku, use the following process:

1. Sign up for a free Heroku account, Create a new app on the Heroku website by clicking the 
"New" button in your dashboard. Give it a name and set the region to Europe.

2. In the Heroku Resources tab, navigate to the Add-Ons section and search for Heroku Postgres. 
Select the free Hobby level. This will allow you to have a remote database instead of using the 
local sqlite3 database, and can be found in the Settings tab. You'll need to update your .env 
file with your new database-url details. Confirm the linking of the heroku app to the correct 
GitHub repository. 

3. ``pip3 install dj_database_url``

4. ``pip3 install psycopg2-binary``

5. Then freeze requirements into requirements.txt

``pip3 freeze > requirements.txt``

6. This will ensure Heroku installs all our apps requirements when we deploy. 

7. Then head to seetings.py file and set up apps new database. First import the following,
``import dj_database_url`` at the top. Then scroll down to the database setting and comment
out the default configuration and replace it with a call to dj_database_url.parse and give 
it the database URL from Heroku. This can be found in Config Vars in app settings or include
command line by typing heroku config. So just copy and paste in.

8. With that saved were ready to connect our new Heroku database and run migrations. 

``python3 manage.py showmigrations``
``python3 manage.py migrate``

This will apply all migrations and get out database set up.

9. Now to import all our product data, we can use our fixtures again by loading categories
and then products.

``python3 manage.py loaddata categories``
``python3 manage.py loaddata products``

10. Then create a superuser to log in with.

``python3 manage.py createsuperuser``

Following the instructions in the terminal.

11. Back in settings.py remove the Heroku database config and uncomment the default so our
database URL doesnt end up in version control.

12. Then change the database setting to use an if statement so that when the database URL environmental
variable will be defined, we connect to Postgres and otherwise we connect to sqlite3.

13. Next set the enviroment variables, got to Heroku dashboard and click settings then Reveal Config Vars.
Set the following variables.

| Key	                        | Value                      |
|-------------------------------|----------------------------|
|AWS_ACCESS_KEY_ID              |<YOUR_AWS_ACCESS_KEY_ID>    |
|AWS_SECRET_ACCESS_KEY          |<YOUR_AWS_SECRET_ACCESS_KEY>|
|DATABASE_URL                   |<YOUR_DATABASE_URL>         |       
|EMAIL_HOST_PASS                |<YOUR_EMAIL_HOST_PASS>      |
|EMAIL_HOST_USER                |<YOUR_EMAIL_HOST_USER>      |
|SECRET_KEY                     |<YOUR_SECRET_KEY>           |
|STRIPE_PUBLIC_KEY              |<YOUR_STRIPE_PUBLIC_KEY>    |
|STRIPE_SECRET_KEY              |<YOUR_STRIPE_SECRET_KEY>    |
|STRIPE_WH_SECRET               |<YOUR_STRIPE_WH_SECRET>     |
|USE_AWS                        |<YOUR_USE_AWS>              |


13. ``pip3 install gunicorn``

14. Again freeze requirements.

15. Create a Procfile with the terminal command 

``echo web: python app.py > Procfile``

web: gunicorn appname.wsgi:application

16. Then log into Heroku from terminal.

``heroku login -i``

17. Next run.

``heroku config:set DISABLE_COLLECTSTATIC=1 --app appname``

This will prevent Heroku from collecting static files when we deploy.

18. Next add the hostname of our app to allowed hosts in settings.py.

``ALLOWED_HOSTS = ['fitness-2020-milestonefour.herokuapp.com', 'localhost']``

Add local host so GitPod will still work.

19. git add and git commit the new requirements and Procfile and then git push the project 
to GitHub 

20. Then connect to Heroku.

``heroku git:remote -a appname``

``git push heroku master``

21. Next set up to automatically deploy when we push to GitHub. Go to app in Heroku deploy tab
set to GitHub and search for you repository and then click connect.

7. In the heroku dashboard for the application, click on settings tab and then click on the 
Reveal config vars button to configure environmental variables.

Set the following config vars:

                 

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