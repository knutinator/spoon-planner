# Spoonplanner

![SpoonPlanner](/media/readme/mockup_spoon.png)
<a href="https://spoonplanner.herokuapp.com/">Spoonplanner</a> is a browser based tool designed specifically for people within the neurodiverse community who may struggle with organizing their day-to-day activities.

 The app provides a user-friendly interface that enables users to create, edit, delete, and view their tasks in an easy and intuitive way. Tasks are organized into two main categories: "Today's Tasks" and "All Tasks". The app also calculates and displays whether there will be a surplus or deficit of energy based on the input energy and the total energy needed for the scheduled tasks.

<br>

----

## Index

1. [Features](#features)
2. [Future Features](#future-features)
3. [Usage](#usage)
4. [Deployment](#deployment)
5. [Development](#development)
6. [Wireframe mockups](#wireframe-mockups)
7. [Technologies used](#technologies-used)
8. [Testing](#testing)
   - [Lighthouse](#lighthouse)
   - [HTML](#html)
   - [CSS](#css)
   - [Responsiveness](#responsiveness)
   - [Manual Testing](#manual-testing)
9. [Database Schema](#database-schema)
10. [Credits](#credits)
 
<br>

----
## Features
What follows is a description of all parts and functions of the app:

- User accounts to keep schedules safe and private

![Login](/media/readme/login.png)
- Create, edit, and delete tasks

![Create task](/media/readme/create.png)
- View all tasks or just today's tasks

![Today's tasks](/media/readme/today.png)
- Add tasks to today's tasks from the all tasks page

![Select tasks](/media/readme/add.png)
- Mark tasks as completed

![Mark as completed](/media/readme/complete.png)
- Input daily energy levels

![Input energy](/media/readme/energy.png)
- View energy surplus or deficit for the day

![Surplus energy](/media/readme/surplus.png)
- Admin accounts for testing and managing users

![Admin](/media/readme/admin.png)

<br>

[Back to Index](#index)

----
## Future Features 
These are features that were considered, but not implemented into the MVP of this project.
- Keep track of your energy levels over several days
- Auto-fill today's schedule based on today's energy
- Plan days in advance
- Display energy cost in a clearer way (with colors)

<br>

[Back to Index](#index)

----
## Usage

1. Navigate to https://spoonplanner.herokuapp.com/ in your web browser
2. Register a new account or log in with an existing one
3. Create tasks by clicking on the "Add Task" button
4. View tasks on the "All Tasks" page or the "Today's Tasks" page
5. Edit or delete tasks as needed
6. Mark tasks as completed by checking the box next to the task (On Today's Tasks)
7. Input your daily energy or update it if needed
8. Add tasks from "All Tasks" to "Today's Tasks" by clicking on the "Add to Today" button
9. View your predicted energy surplus/deficit for today
10. Energy levels and "Today's Tasks" resets each midnight

<br>

[Back to Index](#index)

----
## Deployment

This project was deployed using GitHub. To deploy your own instance of the project, you can follow these steps:

1. Fork the repository to your own GitHub account.
2. Clone the repository to your local machine using git clone.
3. Install the necessary dependencies by running pip install -r requirements.txt in the root directory of the project.
4. Set up your environment variables by creating a .env file in the root directory of the project. You can use the .env.example file as a template.
5. Run the migrations using python manage.py migrate.
6. Start the server using python manage.py runserver.

If you'd like to deploy your project to a live server, you can follow these additional steps:

1. Choose a hosting provider that supports Django applications, such as Heroku or PythonAnywhere.
2. Create an account and set up your server environment.
3. Connect your hosting provider to your GitHub account and set up automatic deployments from your repository.
4. Set up your environment variables in your hosting provider's control panel or using a .env file on the server.
5. Run the necessary commands to install dependencies and start the server on your hosting provider. These commands will depend on the hosting provider you choose.

That's it! With these steps, you should have a live instance of your project running on the internet.

<br>

[Back to Index](#index)

----
## Development

This app was developed using an agile methodology. After an initial brainstorm period, an idea was settled upon. But, in order to fit within the scope of this project, the app was scaled down to an MVP (minimum viable product) containing just the basic functionality.

Next, a series of user stories was written to reflect all the functionality within the app. All user stories can be found here: https://github.com/users/knutinator/projects/2/views/1

(Note: some user stories were left unfinished, since they were deemed unneccesary in the MVP stage of the project)

Clicking on any of the user stories reveals how each of the stories were further broken down into concrete tasks for the development team (which is me).

Developing in this manner proved to be a useful way of keeping control of exactly what needed to be done at each stage of the process.

Lastly, after all neccesary functionality was implemented, the app was styled in an user-friendly and mobile-first design using Bootstrap.

<br>

[Back to Index](#index)

----
## Wireframe mockups

Wireframes were created using Balsamiq to explore placement of UI elements. Here are the mockups of the different pages (on mobile and desktop):

**Today's Tasks**

![Today's Tasks Wireframe](/media/readme/wireframe_todays_tasks.png)

**All Tasks**

![All Tasks Wireframe](/media/readme/wireframe_all_tasks.png)

**Edit/Create Task**

![Edit/Create Tasks Wireframe](/media/readme/wireframe_edit_tasks.png)

<br>

[Back to Index](#index)

----
## Technologies used

- Django framework
- PostgreSQL database (ElephantSQL)
- HTML/CSS (Bootstrap)
- GitHub/Heroku (For deployment)

### Database

Here is the database schema (in plain text format):

![Schema](/media/readme/schema.png)

<br>

[Back to Index](#index)

----
## Testing

### LIGHTHOUSE

 The site has been run through the Lighthouse tester in Google Chrome DevTools and recieved excellent scores:

![Lighthouse](/media/readme/lighthouse.png)

### HTML

HTML was tested using the official W3C validator, which the site passed without any errors:
![W3C](/media/readme/w3c.png)

### CSS

CSS did not have to be tested, since the site only uses unmodified Bootstrap styling.

### RESPONSIVENESS

The app was tested using a variety of resolutions in Chrome DevTools, as well as on an Android Phone. Since it was developed with mobiles in mind, the app scales witout any problems.

### MANUAL TESTING

Automated testing was considered, but eventually I chose manual testing, since the size of this project is quite small at the moment.

Manual tests performed:
- While logged out, I tried accessing all of the separate URL:s in the app, to make sure that a user cannot use any of the functions unless logged in.
- In the Admin account, I tested that all built-in Django functions were working properly, like creating, viewing and deleting user accounts and tasks. All functions worked as intended.
- I created several test user accounts in order to test that users have complete CRUD functionality, and that one user cannot access the data of another. All functions worked as intended.
- I left the 'user energy' and 'selected tasks' fields populated overnight, and checked them the next day to see if they were auto-reset. This worked as intended.

<br>

[Back to Index](#index)

----
## Credits
- Coded by Jonatan Knut von Sydow as a student of Code Institute

- Login page inspiration: https://learndjango.com/tutorials/django-login-and-logout-tutorial

- Mockup phone app image from <a href="https://www.freepik.com/free-psd/premium-mobile-phone-screen-mockup-template_3891016.htm#query=app%20mockup&position=3&from_view=keyword&track=ais">rawpixel.com</a> on Freepik

- Read more about the [Spoon Theory](https://en.wikipedia.org/wiki/Spoon_theory), which inspired this app.
