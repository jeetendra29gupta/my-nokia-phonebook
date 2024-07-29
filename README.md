# My Nokia Phonebook RESTful API

My Nokia Phonebook is a web application that allows users to manage their contacts through a RESTful API. The application provides CRUD operations to add, search, update, and delete contacts, with a user-friendly frontend interface.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)


## Features

- **Add New Contacts**: Add contacts with full name, mobile number, and email ID.
- **Search Contacts**: Search for contacts by name.
- **Update Contacts**: Update existing contact details.
- **Delete Contacts**: Remove contacts from the list.
- **Responsive Design**: User-friendly interface that works on both desktop and mobile devices.

## Tech Stack

- **Backend**: Flask (Python) with SQLAlchemy for ORM
- **Frontend**: HTML, CSS (W3.CSS framework)
- **JavaScript**: Fetch API for asynchronous operations
- **Database**: SQLite for data storage

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jeetendra29gupta/my-nokia-phonebook.git
   cd my-nokia-phonebook
   ```
2. **Set up a virtual environment:**
    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. **Install the required packages:**
    ```bash
   pip install -r requirements.txt
    ```
4. **Run the application:**
    ```bash
    flask run
   ```