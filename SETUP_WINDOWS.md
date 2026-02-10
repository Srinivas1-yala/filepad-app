# FilePad Setup Instructions for Windows

## Quick Setup (5 Steps)

### Step 1: Install Dependencies
Open Command Prompt or PowerShell in the project folder and run:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Step 2: Create Database
```bash
python manage.py makemigrations filepad
python manage.py migrate
```

### Step 3: Create Media Directory
```bash
mkdir media
```

### Step 4: Start Django Server
```bash
python manage.py runserver
```

Keep this terminal running!

### Step 5: Open FilePad
- Open `templates\index.html` in your web browser
- OR use Live Server extension in VS Code

---

## That's It!

You should now be able to:
1. Enter a password to login/create your space
2. Upload files (drag & drop or click)
3. Download files
4. Delete files

---

## Troubleshooting

### "No module named django"
Make sure virtual environment is activated:
```bash
venv\Scripts\activate
```

### "Port already in use"
```bash
python manage.py runserver 8080
```
Then update `index.html` line 343 to use port 8080

### Upload fails
Check terminal for errors. The fix is already applied in this version!

---

## Optional: Create Admin User

```bash
python manage.py createsuperuser
```

Then visit: http://127.0.0.1:8000/admin/
