
<!-- TOC ignore:true -->
# Spoonplanner 

![SpoonPlanner](/media/readme/mockup_spoon.png)
<a href='https://spoonplanner.herokuapp.com/'>Spoonplanner</a> is a browser based tool designed specifically for people within the neurodiverse community who may struggle with organizing their day-to-day activities.

 The app provides a user-friendly interface that enables users to create, edit, delete, and view their tasks in an easy and intuitive way. Tasks are organized into two main categories: 'Today's Tasks' and 'All Tasks'. The app also calculates and displays whether there will be a surplus or deficit of energy based on the input energy and the total energy needed for the scheduled tasks. 
 
 <br>

> Note: In the current form the app is provided as an MVP (Minimum Viable Product) version in order to try out the basic functionality. Further development will bring more functions, a more coherent design and easier navigation.

<br>

----
<!-- TOC ignore:true -->
# Index
<!-- TOC -->

- [Features](#features)
    - [Future Features](#future-features)
- [Usage](#usage)
- [Deployment](#deployment)
    - [Deploying to Heroku](#deploying-to-heroku)
- [Development](#development)
    - [Wireframe mockups](#wireframe-mockups)
    - [Technologies used](#technologies-used)
        - [Database](#database)
- [Testing](#testing)
    - [User Stories & Manual Testing](#user-stories--manual-testing)
    - [Lighthouse validation](#lighthouse-validation)
    - [HTML validation](#html-validation)
    - [CSS validation](#css-validation)
    - [Responsiveness testing](#responsiveness-testing)
    - [Additional Manual testing](#additional-manual-testing)
- [Credits](#credits)

<!-- /TOC -->



<br>

----
# Features
What follows is a description of all parts and functions of the app:

<br>

- User accounts to keep schedules safe and private:

![Login](/media/readme/login.png)


<br>

- Create, edit, and delete tasks:

![Create task](/media/readme/create.png)

<br>

- View all tasks or just today's tasks:

![Today's tasks](/media/readme/today.png)

<br>

- Add tasks to today's tasks from the all tasks page:

![Select tasks](/media/readme/add.png)

<br>

- Mark tasks as completed:

![Mark as completed](/media/readme/complete.png)

<br>

- Input daily energy levels:

![Input energy](/media/readme/energy.png)

<br>

- View energy surplus or deficit for the day:

![Surplus energy](/media/readme/surplus.png)

<br>

- Admin accounts for testing and managing users:

![Admin](/media/readme/admin_4.png)

<br>

[Back to Index](#index)

----
## Future Features 
These are features that were considered, but not implemented into the MVP version of this project.
- Keep track of your energy levels over several days

- Auto-fill today's schedule based on today's energy
- Plan days in advance
- Display energy cost in a clearer way (with color coding)

<br>

[Back to Index](#index)

----
# Usage
Here's how to use the basic functions of the app:

1. Navigate to https://spoonplanner.herokuapp.com/ in your web browser

2. Register a new account or log in with an existing one
3. Create tasks by clicking on the 'Add Task' button
4. View tasks on the 'All Tasks' page or the 'Today's Tasks' page
5. Edit or delete tasks as needed
6. Mark tasks as completed by checking the box next to the task (On Today's Tasks)
7. Input your daily energy or update it if needed
8. Add tasks from 'All Tasks' to 'Today's Tasks' by clicking on the 'Add to Today' button
9. View your predicted energy surplus/deficit for today
10. Energy levels and 'Today's Tasks' resets each midnight

<br>

[Back to Index](#index)

----

# Deployment

This project was deployed using GitHub. To deploy your own instance of the project, you can follow these steps:

1. Fork the repository to your own GitHub account.

2. Clone the repository to your local machine using `git clone`.
3. Install the necessary dependencies by running `pip install -r requirements.txt` in the root directory of the project.
4. Set up your environment variables by creating a `.env` file in the root directory of the project. You can use the `.env.example` file as a template.
5. Run the migrations using `python manage.py migrate`.
6. Start the server using `python manage.py runserver`.

## Deploying to Heroku

If you'd like to deploy your project to Heroku, you can follow these additional steps:

1. Create a Heroku account at [https://www.heroku.com/](https://www.heroku.com/) if you haven't already.

2. Install the Heroku CLI by following the instructions at [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli).
3. Log in to your Heroku account using the CLI by running `heroku login` in your terminal and following the prompts.
4. Create a new Heroku app by running `heroku create` in your terminal.
5. Push your code to Heroku by running `git push heroku main`.
6. Set up your environment variables on Heroku using the command `heroku config:set KEY=VALUE` for each variable defined in your `.env` file.
7. Run the migrations on Heroku using `heroku run python manage.py migrate`.
8. Start the server on Heroku using `heroku ps:scale web=1`.
9. Visit your deployed application by running `heroku open` in your terminal.

That's it! With these steps, you should have a live instance of your project running on Heroku.

> Note: These instructions are for deploying a Django application to Heroku specifically. If you choose a different hosting provider, the steps may vary slightly. Please refer to the hosting provider's documentation for more information.


<br>

[Back to Index](#index)

----
# Development

This app was developed using an agile methodology. After an initial brainstorm period, an idea was settled upon. But, in order to fit within the scope of this project, the app was scaled down to an MVP (minimum viable product) containing just the basic functionality.

Next, a series of user stories was written to reflect all the functionality within the app. All User Stories (and the associated tests) can be found further down, under the section [User Stories manual testing](#user-stories-manual-testing).

The User Stories can also be viewed on the app's [Project Board on GitHub](https://github.com/users/knutinator/projects/2).
(Note: some user stories were left unfinished, since they were deemed unneccesary in the MVP stage of the project. These stories will be adressed in future developments of the app.).

Clicking on any of the user stories (in the Project Board) reveals how each of the stories were further broken down into concrete tasks for the development team (which is me).

Developing in this manner proved to be a useful way of keeping control of exactly what needed to be done at each stage of the process.

Lastly, after all neccesary functionality was implemented, the app was styled in an user-friendly and mobile-first design using Bootstrap. The goal at this stage was to achieve a simple, yet functional design which could be improved upon in further development. Below are wireframe mockups that displays how I approached this task.

<br>

[Back to Index](#index)

----
## Wireframe mockups

Wireframes were created using Balsamiq to explore placement of UI elements. Here are the mockups of the different pages (on mobile and desktop):

<br>


**Today's Tasks**

![Today's Tasks Wireframe](/media/readme/wireframe_todays_tasks.png)

<br>

**All Tasks**

![All Tasks Wireframe](/media/readme/wireframe_all_tasks.png)

<br>

**Edit/Create Task** (Same layout for both)

![Edit/Create Tasks Wireframe](/media/readme/wireframe_edit_tasks.png)

<br>
<br>

[Back to Index](#index)

----
## Technologies used

- Django framework

- PostgreSQL database (ElephantSQL)
- HTML/CSS (Bootstrap)
- GitHub/Heroku (For deployment)

<br>

### Database

Here is the database schema (in plain text format):

![Schema](/media/readme/schema.png)

<br>

[Back to Index](#index)

----
# Testing

## User Stories & Manual Testing

Automated testing was considered, but eventually I chose manual testing, since the scope of this project is quite small at the moment. Here follows a description of  the 20 User Stories and the tests I defined for each of them:
<br>
- [User Story 1: Account Creation](#user-story-1-br)
- [User Story 2: Task Creation](#user-story-2-br)
- [User Story 3: Task Editing](#user-story-3-br)
- [User Story 4: Task List Display](#user-story-4-br)
- [User Story 5: Task Deletion](#user-story-5-br)
- [User Story 6: Task Completion](#user-story-6-br)
- [User Story 7: Page Navigation](#user-story-7-br)
- [User Story 8: Task Scheduling](#user-story-8-br)
- [User Story 9: Clear Today's Tasks](#user-story-9-br)
- [User Story 10: Energy Input](#user-story-10-br)
- [User Story 11: Energy Calculation](#user-story-11-br)
- [User Story 12: Daily Energy Reset](#user-story-12-br)
- [User Story 13: Daily Task Reset](#user-story-13-br)
- [User Story 14: Login Validation](#user-story-14-br)
- [User Story 15: Admin User Account List](#user-story-15-br)
- [User Story 16: Admin User Account Creation](#user-story-16-br)
- [User Story 17: Admin User Account Deletion](#user-story-17-br)
- [User Story 18: Admin Task Creation](#user-story-18-br)
- [User Story 19: Admin Task List](#user-story-19-br)
- [User Story 20: Admin Task Deletion](#user-story-20-br)

<br>

---


<!-- TOC ignore:true -->
### **USER STORY 1:** <br>
As a user, I want to be able to create an account, including username and password, so I can securely log in and create my own schedule.

**Test Scenario: Account Creation**
1. Try to log in by clicking the 'Log In' button with empty input fields.
2. Click the 'Create New User' button to access the registration page.
3. Enter a unique username and a strong password(twice).
4. Click on the 'Sign Up' button.
5. Attempt to log in with the newly created username and password.
6. Verify that the login is successful, and the user is redirected to their schedule page.

<br>

**Test Result:** <br>
Functioning as intended.

<br>

---
<br>

<!-- TOC ignore:true -->
### **USER STORY 2:** <br>
As a user, I want to be able to create a new task with a name, description, and 'energy needed' value so that I can remember what I need to do.

**Test Scenario: Task Creation**

1. Log in to the application using valid credentials.
2. Navigate to the 'All Tasks' page by clicking the 'Add Tasks' or 'View all Tasks' button.
3. Click the 'Create New Task' button.
4. Fill in the required fields: task name, description, completion and energy needed.
5. Click on the 'Create Task' button.
6. Verify that the new task is successfully created and displayed in the task list.


<br>

**Test Result:** <br>
Functioning as intended.

<br>

---
<br>

<!-- TOC ignore:true -->
### **USER STORY 3:** <br>
As a user, I want to be able to edit the task I have created so that I can make changes to my schedule.

**Test Scenario: Task Editing**

1. Log in to the application using valid credentials.
2. Navigate to the 'All Tasks' page by clicking the 'Add Tasks' or 'View all Tasks' button.
3. If there are any tasks in the list, click the 'Edit' button on a task.
4. Modify the task name, description, completion or energy needed value.
5. Click on the 'Save Changes' button.
6. Verify that the task is successfully updated with the new information.


<br>

**Test Result:** <br>
Functioning as intended.

<br>


---
<br>

<!-- TOC ignore:true -->
### **USER STORY 4:** <br>
As a user, I want to be able to view a list of all my tasks so that I can see what needs to be done.

**Test Scenario: Task List Display**

1. Log in to the application using valid credentials.
2. Navigate to the 'All Tasks' page by clicking the 'Add Tasks' or 'View all Tasks' button.
3. Verify that all tasks associated with the user are displayed correctly, including their names, descriptions, and energy needed values.


<br>

**Test Result:** <br>
Functioning as intended.

<br>

---
<br>

<!-- TOC ignore:true -->
### **USER STORY 5:** <br>
As a user, I want to be able to delete a task so that I can remove it from my schedule.

**Test Scenario: Task Deletion**

1. Log in to the application using valid credentials.
2. Navigate to the 'All Tasks' page by clicking the 'Add Tasks' or 'View all Tasks' button.
3. If there are any tasks in the list, click the 'Delete' button on a task.
4. Confirm the deletion by pressing 'Delete' again.
5. Verify that the task is successfully deleted and no longer appears in the task list.


<br>

**Test Result:** <br>
Functioning as intended.

<br>

---
<br>

<!-- TOC ignore:true -->
### **USER STORY 6:** <br>
As a user, I want to be able to mark tasks as completed so that I can keep track of my progress.

**Test Scenario: Task Completion**

1. Log in to the application using valid credentials.
2. Navigate to the 'Today's Tasks' page, using button on top right.
3. If there are any tasks in the list, click the 'Completed' checkbox on a task.
4. Verify that the task status is updated to 'completed'.


<br>

**Test Result:** <br>
Functioning as intended.

<br>

---
<br>

<!-- TOC ignore:true -->
### **USER STORY 7:** <br>
As a user, I want to be able to switch between the 'All Tasks' and 'Today's Tasks' pages so I can prioritize more easily.

**Test Scenario: Page Navigation**

1. Log in to the application using valid credentials.
2. Navigate to the 'All Tasks' page.
3. Verify that the 'All Tasks' page displays all tasks.
4. Navigate to the 'Today's Tasks' page.
5. Verify that the 'Today's Tasks' page only displays tasks scheduled for the current day (if any).


<br>

**Test Result:** <br>
Functioning as intended.

<br>

---
<br>

<!-- TOC ignore:true -->
### **USER STORY 8:** <br>
As a user, I want to be able to add tasks from the 'All Tasks' page to display on the 'Today's Tasks' page in order to schedule them.

**Test Scenario: Task Scheduling**

1. Log in to the application using valid credentials.
2. Navigate to the 'All Tasks' page.
3. Click on the 'Add to Schedule' button on any task.
4. Verify that the task is successfully added to the 'Today's Tasks' page.


<br>

**Test Result:** <br>
Functioning as intended.

<br>

---
<br>

<!-- TOC ignore:true -->
### **USER STORY 9:** <br>
As a user, I want to be able to manually clear the view in 'Today's Tasks' so that I can start over and schedule a new set of tasks for the day.

**Test Scenario: Clear Today's Tasks**

1. Log in to the application using valid credentials.
2. Navigate to the 'Today's Tasks' page.
3. Click on the 'Clear Schedule' button.
4. Verify that the 'Today's Tasks' list is empty.


<br>

**Test Result:** <br>
Functioning as intended.

<br>

---
<br>

<!-- TOC ignore:true -->
### **USER STORY 10:** <br>
As a user, I want to be prompted to input my available energy for the day so that the app can calculate if I have enough energy to complete my scheduled tasks in 'Today's Tasks'.

**Test Scenario: Energy Input**

1. Log in to the application using valid credentials.
2. Navigate to the 'Today's Tasks' page.
3. Click the 'Input Energy' button.
4. Enter the available energy value for the day into the field.
5. Verify that the energy input is successfully saved and stored on the top of 'Today's Tasks.


<br>

**Test Result:** <br>
Functioning as intended.

<br>

---
<br>

<!-- TOC ignore:true -->
### **USER STORY 11:** <br>
As a user, I want the app to calculate and display whether I will have a surplus or deficit of energy (in spoons) based on my scheduled tasks and available energy so that I can plan my day accordingly.

**Test Scenario: Energy Calculation**

1. Log in to the application using valid credentials.
2. Navigate to the 'Today's Tasks' page.
3. Ensure that tasks are added and available energy is provided.
4. Verify that the app accurately calculates and displays the energy surplus or deficit.


<br>

**Test Result:** <br>
Functioning as intended.

<br>

---
<br>

<!-- TOC ignore:true -->
### **USER STORY 12:** <br>
As a user, I wish that my daily energy is reset each night so I can begin each day by inputting my current energy level.

**Test Scenario: Daily Energy Reset**

1. Log in to the application using valid credentials.
2. Navigate to the 'Today's Tasks' page.
3. Click the 'Input Energy' button and input your daily energy.
4. Verify that the energy value is displayed on 'Today's Tasks'.
5. Wait 24 hours.
6. Log in again and verify that the energy value has been reset to zero.


<br>

**Test Result:** <br>
Functioning as intended.

<br>

---
<br>

<!-- TOC ignore:true -->
### **USER STORY 13:** <br>
As a user, I want yesterday's scheduled tasks to be reset at midnight so I can begin each day with a fresh schedule.

**Test Scenario: Daily Task Reset**

1. Log in to the application using valid credentials.
2. Navigate to the 'All Tasks' page.
3. Schedule tasks to 'Today's Tasks'.
4. Verify that the tasks are scheduled.
5. Wait 24 hours.
6. Log in again and verify that yesterday's scheduled tasks are reset at midnight, and the 'Today's Tasks' list is empty.


<br>

**Test Result:** <br>
Functioning as intended.

<br>

---
<br>

<!-- TOC ignore:true -->
### **USER STORY 14:** <br>
As a user, I wish that buttons and functions that require login are hidden while I'm not logged in to avoid confusion over what functions can be used.

**Test Scenario: Login Validation**

1. Open the application without logging in.
2. Navigate through the different pages and verify that buttons, pages and functions requiring login are hidden or disabled.


<br>

**Test Result:** <br>
Functioning as intended.

<br>

---
<br>

<!-- TOC ignore:true -->
### **USER STORY 15:** <br>
As an admin, I want to be able to view a list of all user accounts so that I can manage the users.

**Test Scenario: Admin User Account List**

1. Log in to the application as an admin, using https://spoonplanner.herokuapp.com/admin/
2. Navigate to the user management section, by clicking 'Users'.
3. Verify that a list of all user accounts is displayed, including usernames and other details.


<br>

**Test Result:** <br>
Functioning as intended.

<br>

---
<br>

<!-- TOC ignore:true -->
### **USER STORY 16:** <br>
As an admin, I wish to be able to create user accounts so that I can test the functionality of the app.

**Test Scenario: Admin User Account Creation**

1. Log in to the application as an admin.
2. Navigate to the user management section.
3. Click on the 'Add User' or '+ Add' button.
4. Fill in the necessary details (username, password) for a new user account.
5. Verify that the user account is successfully created and added to the user account list.


<br>

**Test Result:** <br>
Functioning as intended.

<br>

---
<br>

<!-- TOC ignore:true -->
### **USER STORY 17:** <br>
As an admin, I want to be able to delete a user account so that I can remove it from the system.

**Test Scenario: Admin User Account Deletion**

1. Log in to the application as an admin.
2. Navigate to the user management section.
3. Select a user account from the list.
4. Click on the 'Delete' button.
5. Verify that the user account is successfully deleted and removed from the user account list.


<br>

**Test Result:** <br>
Functioning as intended.

<br>

---
<br>

<!-- TOC ignore:true -->
### **USER STORY 18:** <br>
As an admin, I wish to be able to create tasks so that I can test the functionality of the app.

**Test Scenario: Admin Task Creation**

1. Log in to the application as an admin.
2. Navigate to the task management section.
3. Click on the 'Add Task' or '+ Add' button.
4. Fill in the necessary details (name, description, energy needed, etc.) for a new task.
5. Verify that the task is successfully created and added to the task list.


<br>

**Test Result:** <br>
Functioning as intended.

<br>

---
<br>

<!-- TOC ignore:true -->
### **USER STORY 19:** <br>
As an admin, I want to be able to view a list of all tasks so that I can manage the tasks.

**Test Scenario: Admin Task List**

1. Log in to the application as an admin.
2. Navigate to the task management section by clicking 'Tasks'.
3. Verify that a list of all tasks is displayed, including task names and other relevant details.


<br>

**Test Result:** <br>
Functioning as intended.

<br>

---
<br>

<!-- TOC ignore:true -->
### **USER STORY 20:** <br>
As an admin, I want to be able to delete a task so that I can remove it from the system.

**Test Scenario: Admin Task Deletion**

1. Log in to the application as an admin.
2. Navigate to the task management section.
3. Select a task from the list.
4. Click on the 'Delete' button.
5. Verify that the task is successfully deleted and removed from the task list.


<br>

**Test Result:** <br>
Functioning as intended.

<br>



<br>

[Back to Index](#index)

---
<br>





## Lighthouse validation

 The site has been run through the Lighthouse tester in Google Chrome DevTools and recieved excellent scores:

![Lighthouse](/media/readme/lighthouse.png)

<br>

## HTML validation

HTML was tested using the official W3C validator, which the site passed without any errors:
![W3C](/media/readme/w3c.png)

<br>

## CSS validation

CSS did not have to be tested, since the site only uses unmodified Bootstrap styling.

<br>

## Responsiveness testing

The app was tested using a variety of resolutions in Chrome DevTools, as well as on an Android Phone. Since it was developed with mobiles in mind, the app scales witout any problems.

<br>

## Additional Manual testing

Apart from the User Story testing described above, the following manual tests were performed:


- While logged out, I tried accessing all of the separate URL:s in the app, to make sure that a user cannot use any of the functions unless logged in.

- I created several test user accounts in order to test that users have complete CRUD functionality, and that one user cannot access the data of another. All functions worked as intended.
- I left the 'user energy' and 'selected tasks' fields populated overnight, and checked them the next day to see if they were auto-reset. This worked as intended.

<br>

[Back to Index](#index)

----
# Credits
- Coded by Jonatan Knut von Sydow as a student of Code Institute

- Login page inspiration: https://learndjango.com/tutorials/django-login-and-logout-tutorial

- Mockup phone app image from <a href='https://www.freepik.com/free-psd/premium-mobile-phone-screen-mockup-template_3891016.htm'>rawpixel.com</a> on Freepik

- Read more about the [Spoon Theory](https://en.wikipedia.org/wiki/Spoon_theory), which inspired this app.
