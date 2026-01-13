SmartNotes 📓
A Secure & Dynamic Personal Note-Taking Application

🚀 Overview
SmartNotes is a full-featured web application built using Django and Bootstrap. It allows users to securely manage their personal thoughts, tasks, and ideas. As an Arts and Science student passionate about software development, I built this project to master professional backend standards, database management, and responsive UI design.

✨ Unique Features
User Ownership & Security: Implemented restricted data access where users can only view, edit, or delete their own notes. This ensures privacy and prevents unauthorized data access between users.

Pinned Notes (Priority Sorting) 📌: Built a custom pinning logic that keeps important notes at the top of the dashboard. This uses Django's Meta class ordering for seamless data organization.

Global Search Functionality: Integrated a powerful real-time search bar using Django Q objects to filter through note titles and content simultaneously.

Clean Template Inheritance: Managed the project with a professional DRY (Don't Repeat Yourself) structure, utilizing a base.html master template for consistent navigation and styling.

Dynamic Bootstrap UI: Designed a modern, responsive grid-based interface with custom cards, interactive buttons, and auto-generated timestamps for every note.

🛠️ Tech Stack
Backend: Python, Django 
Frontend: Bootstrap 5 (Local Setup), HTML5, CSS3
Database: SQLite3
Tools: VS Code, Git/GitHub, Python Virtual Environments

📂 How to Run Locally
Clone the repository:
Bash
git clone [your-repo-link]

Setup Virtual Environment:
python -m venv venv
.\venv\Scripts\activate

Install Dependencies:
pip install django

Apply Database Migrations:
python manage.py makemigrations
python manage.py migrate

Start the Server:
python manage.py runserver

👤Author
Saravanan
