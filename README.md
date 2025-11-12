echo "# 🎓 University Portal (Django Project)

A complete University Portal built using **Django**, featuring:
- User Authentication (Register, Login, Logout)
- Course Management
- Assignment Submission System
- Dashboard with role-based access (Admin, Teacher, Student)
- Grading System with feedback
- Django Messages Framework Integration

## 🚀 Features

### 👥 Authentication
- User registration and login using Django’s authentication system.
- Custom login form (\`LoginForm\`) and template (\`login.html\`).
- Logout functionality with session clearing.
- Role-based access: students, professors, and admins can have different views.

### 📚 Courses App
- Create, list, and enroll in courses.
- Each user can view their own enrolled courses.
- Professors can create new courses.
- \`urls.py\` includes:
  '', 'create/', 'my-courses/', '<int:course_id>/', '<int:course_id>/enroll/'

### 📝 Assignments App
- Professors can create assignments for specific courses.
- Students can submit assignments.
- Professors can view submissions and assign grades.
- Grading form includes comments and file downloads.

### 🏠 Dashboard App
- Displays personalized information based on user type.
- Quick access to user’s enrolled courses and submitted assignments.

### 💬 Django Messages
- All forms and views display success/error messages with a dismissable “X” button.
- Implemented using Django’s built-in \`messages\` framework and Bootstrap alerts.

## 🧩 Project Structure
university_portal/
├── accounts/
├── courses/
├── assignments/
├── dashboard/
└── templates/

## ⚙️ Installation
1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/zainchodry/assignment_system_django.git
   cd assignment_system_django
   \`\`\`

2. Create a virtual environment:
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Linux/macOS
   venv\Scripts\activate     # On Windows
   \`\`\`

3. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. Run migrations:
   \`\`\`bash
   python manage.py makemigrations
   python manage.py migrate
   \`\`\`

5. Start the development server:
   \`\`\`bash
   python manage.py runserver
   \`\`\`

6. Open in your browser:
   [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🧠 Tech Stack
- Django 5+
- SQLite3 (Default Database)
- Bootstrap 5 (Frontend)
- Python 3.8+

## 🧑‍💻 Author
**Zain Choudry (@enigmatix)**
" > README.md
