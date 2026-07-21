# E-commerce Backend

This repository contains the Django backend for an e-commerce application.

## Features

- Django REST Framework API
- JWT authentication via `djangorestframework-simplejwt`
- CORS support
- SQLite database for development

## Clone and setup

1. Clone the repository:

   ```powershell
   git clone <your-repo-url>
   cd ecommerse_backend
   ```

2. Create a virtual environment:

   ```powershell
   py -m venv myenv
   ```

3. Activate the virtual environment:

   ```powershell
   .\myenv\Scripts\Activate.ps1
   ```

4. Install the project dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

5. Apply the database migrations:

   ```powershell
   python myenv\ecomproject\manage.py migrate
   ```

6. Start the development server:

   ```powershell
   python myenv\ecomproject\manage.py runserver
   ```

## Useful commands

- Create a superuser:
  ```powershell
  python myenv\ecomproject\manage.py createsuperuser
  ```
- Run tests:
  ```powershell
  python myenv\ecomproject\manage.py test
  ```

## Notes

- The project settings use SQLite by default.
- `CORS_ALLOWED_ORIGINS` is currently empty; add origins or enable `CORS_ALLOW_ALL_ORIGINS` for local testing if needed.
- JWT settings are configured in `myenv\ecomproject\ecomproject\settings.py`.

