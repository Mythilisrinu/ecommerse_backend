# E-commerce Backend

This repository contains the Django backend for an e-commerce application.

## Features

- Django REST Framework API
- JWT authentication via `djangorestframework-simplejwt`
- CORS support
- SQLite database for development

## Setup

1. Activate the virtual environment:

   ```powershell
   .\myenv\Scripts\Activate.ps1
   ```

2. Install dependencies if needed:

   ```powershell
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```powershell
   python myenv\ecomproject\manage.py migrate
   ```

4. Run the development server:

   ```powershell
   python myenv\ecomproject\manage.py runserver
   ```

## Notes

- The project settings use SQLite by default.
- `CORS_ALLOWED_ORIGINS` is currently empty; add origins or enable `CORS_ALLOW_ALL_ORIGINS` for local testing if needed.
- JWT settings are configured in `myenv\ecomproject\ecomproject\settings.py`.

## Useful commands

- Create a superuser:
  ```powershell
  python myenv\ecomproject\manage.py createsuperuser
  ```
- Run tests:
  ```powershell
  python myenv\ecomproject\manage.py test
  ```
