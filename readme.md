```markdown
# Django Authentication App

A simple Django web application with user authentication and role-based dashboards.

## Features

- **User Registration**: Custom signup functionality
- **User Authentication**: Login/logout system
- **Role-based Dashboards**: Separate dashboards for patients and doctors
- **Clean Redirects**: Logout redirects to home page

## URL Structure

- `/` - Login page (home)
- `/signup/` - User registration
- `/logout/` - Logout (redirects to home)
- `/patient-dashboard/` - Patient dashboard
- `/doctor-dashboard/` - Doctor dashboard

## Setup

1. Install Django:
   ```bash
   pip install django
   ```

2. Run migrations:
   ```bash
   python manage.py migrate
   ```

3. Start the development server:
   ```bash
   python manage.py runserver
   ```

4. Access the app at `http://127.0.0.1:8000`

## Usage

1. Create an account using the signup page
2. Login with your credentials
3. Access your respective dashboard (patient/doctor)
4. Logout returns you to the login page

## Files

- `urls.py` - URL routing configuration
- `views.py` - View functions and classes (not included)
- Templates and static files (as per your Django project structure)
```