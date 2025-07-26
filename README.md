# Django CRM

A simple Customer Relationship Management (CRM) web application built with Django. This project allows users to register, log in, and manage customer records with a user-friendly interface. It supports Microsoft SQL Server as the backend database and uses Bootstrap for styling.

## Features

- User registration and authentication
- Add, view, update, and delete customer records
- Secure login/logout functionality
- Responsive UI with Bootstrap 5
- Admin interface for managing records

## Data Model

The main model is `Record`, which stores:
- First name
- Last name
- Email
- Phone
- Address
- City
- State
- Zipcode
- Created at (timestamp)

## Screenshots

*(Add screenshots of the UI here if desired)*

## Requirements

- Python 3.8+
- Django (see `requirements.txt`)
- Microsoft SQL Server (or compatible, see below)
- ODBC Driver 18 for SQL Server
- Bootstrap 5 (via CDN)

Install dependencies:
```
pip install -r requirements.txt
```

## Database Setup

1. **Create the database:**
   - You can use the provided SQL script:
     ```sql
     CREATE DATABASE DCRM
     ```
   - Or run the included `SQLQuery1.sql` file in your SQL Server.

2. **Configure the database connection:**
   - The default settings in `DjangoCrm/settings.py` use:
     - ENGINE: `mssql`
     - NAME: `DCRM`
     - HOST: `LAPTOP-APLJD65M\MSSQLSERVER01`
     - DRIVER: `ODBC Driver 18 for SQL Server`
     - Extra params: `TrustServerCertificate=yes;Encrypt=yes;`
   - Update these settings as needed for your environment.

3. **(Optional) Use `mydb.py` to ensure the Customers table exists:**
   - This script connects to SQL Server and creates a simple `Customers` table if it doesn't exist.
   - You can also use Django migrations (recommended):
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

## Running the Project

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```
   *(Default superuser: Username: MB23CRM, Password: admin)*
4. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
5. **Access the app:**
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
   - Admin interface: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Usage

- **Register:** Create a new user account.
- **Login:** Access the dashboard to view all customer records.
- **Add Record:** Add a new customer record.
- **View Record:** Click a record ID to view details.
- **Update/Delete:** Update or delete records from the detail view.
- **Logout:** Securely log out of your account.

## Project Structure

```
Django_CRM/
├── DjangoCrm/           # Project settings and URLs
├── Web/                 # Main CRM app (models, views, templates)
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
├── SQLQuery1.sql        # SQL script to create the database
├── mydb.py              # Optional DB utility script
```

## Dependencies

See `requirements.txt` for all Python dependencies:
- django
- mysql
- mysql-connector-python
- mysql-connector
- mssql-django
- django-mssql-backend
- pyodbc

## Notes

- The UI uses Bootstrap 5 via CDN (no local installation needed).
- The project is configured for Microsoft SQL Server by default. You may adapt it for other databases by updating `settings.py` and dependencies.
- For any issues, check your database connection and ODBC driver installation.


