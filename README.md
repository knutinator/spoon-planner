# Spoonplanner

The Spoonplanner App is a tool designed specifically for people within the neurodiverse community who may struggle with organizing their day-to-day activities. The app provides a user-friendly interface that enables users to create, edit, delete, and view their tasks in an easy and intuitive way. Tasks are organized into two main categories: "Today's Tasks" and "All Tasks". The app also calculates and displays whether there will be a surplus or deficit of energy based on the input energy and the total energy needed for the scheduled tasks.

## Features

- User accounts to keep schedules safe and private
- Create, edit, and delete tasks
- View all tasks or just today's tasks
- Add tasks to today's tasks from the all tasks page
- Mark tasks as completed
- Input and track daily energy levels
- View energy surplus or deficit for the day
- Admin accounts for testing and managing users

## Future Features

## Getting Started

### Prerequisites

- Python 3
- Django

### Installing

1. Clone the repository: git clone https://github.com/yourusername/spoonplanner.git
2. Navigate into the project directory: cd spoonplanner
3. Create a virtual environment: python -m venv env
4. Activate the virtual environment: source env/bin/activate (on Windows, use env\Scripts\activate)
5. Install the required packages: pip install -r requirements.txt
6. Create the database: python manage.py migrate
7. Run the development server: python manage.py runserver

## Usage

1. Navigate to http://localhost:8000/ in your web browser
2. Register a new account or log in with an existing one
3. Create tasks by clicking on the "Add Task" button
4. View tasks on the "All Tasks" page or the "Today's Tasks" page
5. Edit or delete tasks as needed
6. Mark tasks as completed by checking the box next to the task
7. Input your daily energy or update it if needed
8. Add tasks from "All Tasks" to "Today's Tasks" by clicking on the "Add to Today" button
9. Energy levels and "Today's Tasks" resets each midnight

## Development

## Testing

## Built With

- Django framework
- PostgreSQL database
- HTML/CSS/JavaScript
- Bootstrap front-end framework

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Authors

- Jonatan Knut von Sydow

## Acknowledgments

- Thank you to the Spoon Theory for inspiring the creation of this app.
