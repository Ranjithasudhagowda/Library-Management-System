# Library-Management-System
Basic CRUD application for a Library Management System using Python and Django with an SQL database.

Features:

Supports basic CRUD operations (Create, Read, Update, Delete) for Library records. Provides a user-friendly interface for managing library records. Validates library data to ensure accuracy and consistency. Implements proper exception handling to handle potential errors.

Setup:

Clone the repository to your local machine. Create a new virtual environment and activate it. Install the required dependencies: pip install -r requirements.txt Create a database for the application: python manage.py migrate Create a superuser account: python manage.py createsuperuser Start the Django development server: python manage.py runserver Running the application: Open a web browser and navigate to http://localhost:8000 to access the application. Log in with the superuser account you created.

Usage:

To view all books records, click on the "book List" button. To add a new books, click on the "Add books" button and enter the book's details. To edit an book's details, click on the "Edit" button next to the book's name. To delete an book's record, click on the "Delete" button next to the book's name.
