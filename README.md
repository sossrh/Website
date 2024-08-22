# Swigge Lite

Swigge Lite is an e-commerce website built with Django framework, enabling user registration, login, order management, and a dynamic menu system.

## Features

- User Registration and Login
- Add and Remove Orders
- Dynamic Menu System
- Admin Dashboard for Management
- Secure Forms with CSRF Protection

## Technologies Used

- Django Framework
- Bootstrap
- JavaScript
- MySQL
- Django Admin (for database management)

## Prerequisites

- Python 3.x
- pip (Python package manager)
- MySQL

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/swigge-lite.git
   cd swigge-lite
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the MySQL database and update the `DATABASES` configuration in `settings.py`.

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser for the Django admin:
   ```
   python manage.py createsuperuser
   ```

## Running the Application

To run the Swigge Lite website:

1. Navigate to the project directory:
   ```
   cd C:\Users\Sagnik Dey\Desktop\SEM IV\Website\Website
   ```

2. Start the Django development server:
   ```
   python manage.py runserver
   ```

3. Open a web browser and go to `http://127.0.0.1:8000/` to view the website.

4. To access the admin panel, go to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

## Security

- CSRF tokens are implemented in all forms for enhanced security.
- Always use HTTPS in production environments.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
