# Me-API-Playground

A full-stack API playground for managing user profiles, projects, and skills. Built with FastAPI and Flask (backend) and a simple HTML frontend. Includes SQL schema for database initialization.

## Architecture

```
[Frontend: https://gentlsnek.github.io/]
				|
				v
[Backend: https://me-api-playground-backend-df3c.onrender.com]
				|
				v
[Database: sql12.freesqldatabase.com]
```
- Frontend (static HTML/JS) interacts with backend via REST API.
- Backend (FastAPI/Flask) connects to MySQL database.

## Setup

### Local

1. Clone repo and enter folder.
2. Create/activate virtualenv:
	 ```bash
	 cd backend
	 source provenv/bin/activate
	 ```
3. Install dependencies:
	 ```bash
	 pip install -r requirements.txt
	 ```
4. Setup database:
	 - Create a MySQL database (e.g. locally or on freesqldatabase.com).
	 - Run `sql schema/initialization.sql` and `sql schema/data_input.sql` in your DB.
	 - Update DB connection info in `db.py`.
5. Start backend:
	 ```bash
	 uvicorn main:app --reload
	 ```
6. Open `frontend/index.html` or use the hosted frontend.

### Production

- Frontend: Hosted at [https://gentlsnek.github.io/](https://gentlsnek.github.io/)
- Backend: Hosted at [https://me-api-playground-backend-df3c.onrender.com](https://me-api-playground-backend-df3c.onrender.com)
- Database: Hosted at [sql12.freesqldatabase.com](https://sql12.freesqldatabase.com)

## Database Schema (Main Tables)

```sql
CREATE TABLE profile (
		id INT AUTO_INCREMENT PRIMARY KEY,
		name VARCHAR(100),
		email VARCHAR(100),
		github VARCHAR(200),
		linkedin VARCHAR(200)
);

CREATE TABLE education (
		id INT AUTO_INCREMENT PRIMARY KEY,
		profile_id INT,
		tenth_marks DECIMAL(5,2),
		twelfth_marks DECIMAL(5,2),
		cgpa DECIMAL(5,2),
		FOREIGN KEY (profile_id) REFERENCES profile(id) ON DELETE CASCADE
);

CREATE TABLE skills(
		id INT AUTO_INCREMENT PRIMARY KEY,
		profile_id INT,
		name VARCHAR(50),
		FOREIGN KEY (profile_id) REFERENCES profile(id) ON DELETE CASCADE
);

CREATE TABLE projects(
		id INT AUTO_INCREMENT PRIMARY KEY,
		profile_id INT,
		project_name VARCHAR(100),
		project_description TEXT,
		project_skill1 VARCHAR(20),
		project_skill2 VARCHAR(20),
		project_skill3 VARCHAR(20),
		github_link VARCHAR(100),
		FOREIGN KEY (profile_id) REFERENCES profile(id) ON DELETE CASCADE
);
```

## Sample Requests

- Get profile:
	```bash
	curl https://me-api-playground-backend-df3c.onrender.com/profile
	```
- Update profile:
	```bash
	curl "https://me-api-playground-backend-df3c.onrender.com/profile/update?category=name&subject=NewName"
	```
- Get projects:
	```bash
	curl https://me-api-playground-backend-df3c.onrender.com/projects/get
	```
- Get projects by skill:
	```bash
	curl https://me-api-playground-backend-df3c.onrender.com/projects/byskills/get/python
	```
- Get top skills:
	```bash
	curl https://me-api-playground-backend-df3c.onrender.com/skills/top
	```

## Known Limitations

- Only supports a single profile (id=1).
- No authentication or authorization.
- Database connection info must be manually set in `db.py`.
- No pagination for project/skill lists.
- No file upload or image support.
- Limited error handling.

## Live Frontend

The frontend is hosted at: [https://gentlsnek.github.io/](https://gentlsnek.github.io/)

## Live Backend

The backend is hosted at: [https://me-api-playground-backend-df3c.onrender.com](https://me-api-playground-backend-df3c.onrender.com)

## Live Database

The database is hosted at: [sql12.freesqldatabase.com](https://sql12.freesqldatabase.com)

## Features

- RESTful API for user profiles, projects, and skills
- FastAPI and Flask support
- Dockerfile for containerization
- SQL scripts for database setup
- Simple HTML frontend

## Folder Structure

```
backend/
  db.py
  Dockerfile
  main.py
  models.py
  requirements.txt
  routes/
	 profile.py
	 projects.py
	 skills.py
frontend/
  index.html
sql schema/
  data_input.sql
  initialization.sql
```

## Getting Started

### Prerequisites

- Python 3.12+
- pip
- Docker (optional)

### Setup

1. Create and activate a virtual environment:
	```bash
	cd backend
	source provenv/bin/activate
	```

2. Install dependencies:
	```bash
	pip install -r requirements.txt
	```

3. Initialize the database:
	```bash
	# Run SQL scripts in your database
	```

4. Run the backend server:
	```bash
	uvicorn main:app --reload
	```

5. Open `frontend/index.html` in your browser.


- FastAPI
- Flask
- SQL (PostgreSQL/MySQL compatible)
- Docker

## API Endpoints

- `/profile` - Manage user profiles
- `/projects` - Manage projects
- `/skills` - Manage skills

## Resume

[My Resume (PDF)](https://drive.google.com/file/d/1zzPE0_M5s5VmK8MrFFCDYfgVjyb90T5j/view?usp=sharing)
