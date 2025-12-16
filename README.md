# 📝 Django Blog Management System

A role-based blog management system built using **Django**, featuring content creation, moderation workflows, media uploads, and custom dashboards.

---

## 📌 Project Overview

This project is a multi-user blogging platform with granular permissions and role-based access control. It allows different user roles to manage blog posts, categories, comments, and media efficiently.

---

## ✨ Features

- Multi-role system (Admin / Manager / Editor / Author)
- Create, Read, Update, Delete (CRUD) for posts & categories
- Unique slug generation with auto-prepopulation
- Media (image) upload and configuration
- Comment system (authenticated users only)
- Manager & Editor dashboards with counts and tables
- Granular permission checks using Django Groups & Permissions
- Search feature with retained search term
- Pagination for post listings
- Featured and recent posts

---

## 🧩 Models

- **Blog / Post**
- **Category**
- **Comment**
- **User Relationships**
- **Slug Handling**
- **Media Handling**

---

## 📝 Forms

- Create / Edit Post Form
- User Registration Form
- Comment Form

---

## 🔐 Authentication & Authorization

- User login & logout
- Django Groups & Permissions
- Custom permission checks
- Role-based access decorators

---

## 🛠 Admin Customization

- Customized Django Admin interface
- Enhanced listings for posts, categories, and users

---

## 📊 Dashboards

### Manager Dashboard

- Post & category counts
- Content overview tables

### Editor Dashboard

- Assigned post management
- Status-based filtering

> Dashboard access is controlled by user roles.

---

## 📁 Media & Static Files

- Image uploads for blog posts
- Media and static file configuration
- Template-based UI rendering

---

## 🧪 Tech Stack

- **Backend:** Django
- **Frontend:** Django Templates (HTML, CSS, Bootstrap)
- **Database:** PostgreSQL
- **Authentication:** Django Auth System

---

## ⚙️ Setup Instructions

```bash
git clone <repository-url>
cd project-name
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
