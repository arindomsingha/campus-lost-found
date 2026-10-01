# CampusLost AI --- College Lost & Found

A full-stack college Lost & Found application where students can report
lost items, report items they have found, and search reports by keyword,
category, and location.

> **Current project scope:** The application currently includes a
> FastAPI backend, PostgreSQL database access through SQLAlchemy ORM,
> and a plain HTML/CSS/JavaScript frontend. Authentication, photo
> uploads, AI-based matching, notifications, and private contact
> workflows are future enhancements.

## Features

-   Create, view, update, and delete lost-item reports.
-   Create, view, update, and delete found-item reports.
-   Search lost and found reports together or separately.
-   Filter search results by keyword, category, and location.
-   Validate API input with Pydantic schemas.
-   Store reports in PostgreSQL using SQLAlchemy ORM.
-   Explore and test endpoints through FastAPI Swagger UI.
-   Use a responsive frontend built with HTML, CSS, and JavaScript.

## Tech Stack

| Technology     | Purpose                       |
| -------------- | ----------------------------- |
| Python         | Backend programming language  |
| FastAPI        | REST API development          |
| Pydantic       | Data validation               |
| SQLAlchemy ORM | Database operations           |
| PostgreSQL     | Relational database           |
| Swagger UI     | API documentation and testing |

## Project Structure

```text
CampusLostAI/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
└── frontend/
    ├── index.html
    ├── style.css
    └── script.js
```

Your exact structure may differ slightly depending on how you organized
the project.

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd CampusLostAI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

The main dependencies are:

* fastapi
* uvicorn
* sqlalchemy
* psycopg[binary]
* pydantic

### 4. Set up PostgreSQL

Create a database named:

```sql
CREATE DATABASE campus_lost_found;
```

### 5. Configure the database connection

Update the `DATABASE_URL` in `database.py` with your PostgreSQL credentials.

Example:

```python
DATABASE_URL = (
    "postgresql+psycopg://postgres:YOUR_PASSWORD"
    "@localhost:5432/campus_lost_found"
)
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

### 6. Start the FastAPI backend

From the project root, run:

```bash
uvicorn main:app --reload
```

The backend should be available at:

```text
http://127.0.0.1:8000
```

### 7. API Documentation

FastAPI automatically generates interactive API documentation.

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

Use Swagger UI to test the API endpoints without needing a separate frontend.

The project uses SQLAlchemy's `Base.metadata.create_all()` to create tables that do not exist yet. It does **not** automatically migrate changes to existing tables. Use Alembic for schema migrations as the project grows.

### 8. Start the frontend

Open a second terminal:

```bash
cd frontend
python -m http.server 5500
```

Then open:

```text
http://localhost:5500
```

Make sure the `API_URL` in `frontend/script.js` points to the backend:

```javascript
const API_URL = "http://127.0.0.1:8000";
```

### 9. Check CORS

If the browser reports a CORS error, make sure the FastAPI CORS configuration allows the frontend origin you are using:

```python
allow_origins=[
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]
```

The origin must match the host and port used in your browser.

## API Endpoints

### Lost Items

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/lost-items` | Create a lost-item report |
| `GET` | `/lost-items` | Retrieve all lost items |
| `GET` | `/lost-items/{item_id}` | Retrieve a lost item by ID |
| `PATCH` | `/lost-items/{item_id}` | Update a lost-item report |
| `DELETE` | `/lost-items/{item_id}` | Delete a lost-item report |

### Found Items

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/found-items` | Create a found-item report |
| `GET` | `/found-items` | Retrieve all found items |
| `GET` | `/found-items/{item_id}` | Retrieve a found item by ID |
| `PATCH` | `/found-items/{item_id}` | Update a found-item report |
| `DELETE` | `/found-items/{item_id}` | Delete a found-item report |

### Search

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/search` | Search lost and found reports |

Supported query parameters:

| Parameter | Values / Example | Purpose |
|---|---|---|
| `keyword` | `wallet` | Matches item name or description |
| `category` | `Electronics` | Filters by category |
| `location` | `Library` | Filters by location |
| `item_type` | `lost`, `found`, `all` | Selects which report types to search |

Examples:

```text
GET /search?keyword=wallet&item_type=all
GET /search?location=Library&item_type=found
GET /search?category=Electronics&item_type=lost
```

Search matching is based on the implementation in `main.py`. The current PostgreSQL search uses case-insensitive partial matching (`ILIKE`).

## Example Requests

### Create a lost-item report

`POST /lost-items`

```json
{
  "item_name": "Identity Card (ID)",
  "description": "College ID card belonging to a student",
  "category": "Accessories",
  "location": "Academic Block",
  "date_lost": "2026-09-26"
}
```

### Create a found-item report

`POST /found-items`

```json
{
  "item_name": "Blue Water Bottle",
  "description": "Blue metal bottle with a black cap",
  "category": "Bottle",
  "location": "College Canteen",
  "date_found": "2026-09-29"
}
```

## How It Works

1. A client sends an HTTP request to a FastAPI endpoint.
2. FastAPI receives and validates the request data using Pydantic.
3. SQLAlchemy ORM performs the required database operation.
4. PostgreSQL stores or retrieves the requested information.
5. FastAPI returns the result as a JSON response.

## Learning Objectives

This project demonstrates:

* Building REST APIs using FastAPI.
* Understanding HTTP methods and API endpoints.
* Validating data using Pydantic models.
* Performing CRUD operations using SQLAlchemy ORM.
* Connecting Python applications to PostgreSQL.
* Implementing search and filtering functionality.
* Testing APIs using Swagger UI.

## Future Enhancements

* User registration and authentication.
* Image uploads for lost and found items.
* AI-based matching of lost and found reports.
* Contact details and secure communication between students.
* Notifications when a potential match is found.
* Item-claim verification and return tracking.

## License

This project was developed for educational purposes as a college project.
