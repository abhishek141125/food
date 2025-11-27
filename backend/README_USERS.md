Creating sample users

This repository includes a management command to create sample users from `backend/data/users.csv`.

How to run:

1. Activate your virtual environment and install dependencies:

```powershell
cd backend
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
```

2. Run the management command:

```powershell
cd backend
python manage.py create_sample_users
```

This will create users listed in `backend/data/users.csv` using Django's `create_user()` (passwords are hashed). If a username already exists it will be skipped.

Security note: The `users.csv` file contains plaintext passwords for convenience in local development only. Do NOT use these passwords in production and remove the file before publishing.
