# 🚀 Personal Portfolio Web Application

A dynamic and modern Personal Portfolio web application built using **Python**, **Django**, and **Bootstrap**. This project allows developers or professionals to showcase their skills, projects, work experience, and educational background dynamically, with a secure admin dashboard to manage all content.

---

## 🛠️ Step-by-Step Project Overview & Implementation

### Step 1: Project Setup & Environment
- Created a clean virtual environment and installed Django framework.
- Initialized a brand new Django project following strict naming conventions (`Name_ID_Portfolio`).
- Created a core application inside the project named `PortfolioApp` to handle all portfolio modules.

### Step 2: Relational Database Architecture (`models.py`)
Designed and implemented modular database tables to store information dynamically:
- **PersonalInfoModel:** Holds personal data (Name, Bio, Email, Phone, Social Links). Optimized to handle requests flawlessly even when a user is logged out (`AnonymousUser`) by serving public query fallbacks.
- **SkillModel:** Stores skill tags along with integer values to render technical proficiency.
- **ProjectModel:** Manages project metadata, display images, tech stack tags, and repository/live links.
- **ExperienceModel & EducationModel:** Captures employment timelines and academic history to build a dynamic resume.
- **ContactModel:** Stores validated messages received from the public visitor's contact form.

### Step 3: Frontend Interface & BootStrap Integration
- Formatted the workspace using a responsive and modern layout.
- Designed an automated **Skills & Proficiency Section** that pulls integers from the database and displays them using native Bootstrap animated progress bars (`style="width: {{ skill.proficiency }}%"`).
- Rendered the **Projects Gallery** and timeline components using Bootstrap Grid.

### Step 4: URL Routing & View Logic (`views.py`)
- Created view functions (like `DashboardPage`) to handle query requests and pass contexts to templates seamlessly.
- Fixed `NoReverseMatch` exceptions by ensuring precise primary key (`pdata.id`) binding across dynamic update URLs.
- Handled `POST` requests securely inside the view to process the Contact Form without refreshing the layout.

### Step 5: Authentication & Security Controls
- Standardized the admin portal by registering all created models inside `admin.py`.
- Formulated custom `createsuperuser` profiles with explicit assignment data (`username: admin`, `password: 1234`).
- Wrapped administrative "Update" actions using Django's template tags (`{% if user.is_authenticated %}`) to prevent unauthenticated guests or anonymous users from modifying data.

---

## ⚙️ How to Run This Project Locally

Follow these quick commands to set up the workspace on your local machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name


2. Activate Virtual Environment
Bash
# Windows
python -m venv env
env\Scripts\activate

# macOS/Linux
python3 -m venv env
source env/bin/activate

3. Install Dependencies
Bash
pip install django
4. Apply Migrations
Bash
python manage.py makemigrations
python manage.py migrate
5. Create Admin Superuser
Bash
python manage.py createsuperuser
6. Boot the Server
Bash
python manage.py runserver
Open http://127.0.0.1:8000/ in your browser to view the application!

🔒 Security Features
Fully protected against Cross-Site Request Forgery (CSRF) using Django's built-in tokens in forms.

Safe route handling for anonymous visitors allowing seamless viewing access while restricting management routes to authenticated admins only.

📄 License
This project is open-source and available under the MIT License.

🙋‍♂️ Developed by Mostakim Billah Shamim
