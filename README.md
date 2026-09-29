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

  Layer                       Technology
  --------------------------- -----------------------
  Frontend                    HTML, CSS, JavaScript
  Backend                     Python, FastAPI
  Validation                  Pydantic
  ORM                         SQLAlchemy
  Database                    PostgreSQL
  API documentation/testing   Swagger UI

## Project Structure

``` text
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

## Requirements

Install the following before running the project:

-   Python 3.10 or newer
-   PostgreSQL
-   pip
-   A browser

## Setup

### 1. Clone or download the project

Open a terminal in the project directory.

### 2. Create and activate a virtual environment (recommended)

``` bash
python -m venv .venv
```

Windows PowerShell:

``` powershell
.\.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

``` bat
.venv\Scripts\activate
```

macOS/Linux:

``` bash
source .venv/bin/activate
```

### 3. Install Python dependencies

Make sure `requirements.txt` includes the packages used by your backend.
For example:

``` text
fastapi
uvicorn[standard]
sqlalchemy
psycopg[binary]
pydantic
```

Install them:

``` bash
pip install -r requirements.txt
```

### 4. Create the PostgreSQL database

In pgAdmin or `psql`, run:

``` sql
CREATE DATABASE campus_lost_found;
```

If the database already exists, do not create it again.

### 5. Configure the database connection

In `database.py`, set `DATABASE_URL` to match your PostgreSQL username,
password, host, port, and database name.

Example:

``` python
DATABASE_URL = (
    "postgresql+psycopg://postgres:YOUR_PASSWORD"
    "@localhost:5432/campus_lost_found"
)
```

Replace `YOUR_PASSWORD` with your local PostgreSQL password. Do not
commit real passwords or other secrets to a public repository. For a
deployed application, load the connection string from an environment
variable.

### 6. Start the FastAPI backend

From the project root, run:

``` bash
uvicorn main:app --reload
```

The backend should be available at:

-   API base: `http://127.0.0.1:8000`
-   Swagger UI: `http://127.0.0.1:8000/docs`
-   ReDoc: `http://127.0.0.1:8000/redoc`

The project uses SQLAlchemy's `Base.metadata.create_all()` to create
tables that do not exist yet. It does **not** automatically migrate
changes to existing tables; use Alembic for schema migrations as the
project grows.

### 7. Start the frontend

Open a second terminal:

``` bash
cd frontend
python -m http.server 5500
```

Then open:

`http://localhost:5500`

Make sure the `API_URL` in `frontend/script.js` points to the backend:

``` javascript
const API_URL = "http://127.0.0.1:8000";
```

### 8. Check CORS

If the browser reports a CORS error, make sure the FastAPI CORS
configuration allows the frontend origin you are using, such as:

``` python
allow_origins=[
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]
```

The origin must match the host and port in your browser.

## API Endpoints

### Lost items

  Method     Endpoint                  Purpose
  ---------- ------------------------- ----------------------------
  `POST`     `/lost-items`             Create a lost-item report
  `GET`      `/lost-items`             List all lost-item reports
  `GET`      `/lost-items/{item_id}`   Get one lost-item report
  `PATCH`    `/lost-items/{item_id}`   Update selected fields
  `DELETE`   `/lost-items/{item_id}`   Delete a lost-item report

### Found items

  Method     Endpoint                   Purpose
  ---------- -------------------------- -----------------------------
  `POST`     `/found-items`             Create a found-item report
  `GET`      `/found-items`             List all found-item reports
  `GET`      `/found-items/{item_id}`   Get one found-item report
  `PATCH`    `/found-items/{item_id}`   Update selected fields
  `DELETE`   `/found-items/{item_id}`   Delete a found-item report

### Search

  Method   Endpoint    Purpose
  -------- ----------- ----------------------------------
  `GET`    `/search`   Search lost and/or found reports

Supported query parameters:

  -----------------------------------------------------------------------
  Parameter               Values / example        Purpose
  ----------------------- ----------------------- -----------------------
  `keyword`               `wallet`                Matches item name or
                                                  description

  `category`              `Electronics`           Filters by category

  `location`              `Library`               Filters by location

  `item_type`             `lost`, `found`, `all`  Selects which report
                                                  types to search
  -----------------------------------------------------------------------

Examples:

``` text
GET /search?keyword=wallet&item_type=all
GET /search?location=Library&item_type=found
GET /search?category=Electronics&item_type=lost
```

Search matching is based on the implementation in `main.py`; the current
PostgreSQL search uses case-insensitive partial matching (`ILIKE`).

## Example Requests

### Create a lost-item report

`POST /lost-items`

``` json
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

``` json
{
  "item_name": "Blue Water Bottle",
  "description": "Blue metal bottle with a black cap",
  "category": "Bottle",
  "location": "College Canteen",
  "date_found": "2026-09-29"
}
```

Use Swagger UI at `/docs` to try these requests.

## How It Works

1.  A user submits a form or search from the frontend.
2.  JavaScript uses `fetch()` to send an HTTP request to FastAPI.
3.  FastAPI validates incoming data with Pydantic.
4.  The endpoint uses SQLAlchemy ORM to query or update PostgreSQL.
5.  FastAPI returns a JSON response.
6.  JavaScript displays the response on the page.

## Current Limitations

-   There is no user registration or login yet.
-   Reports are not yet tied to an authenticated owner.
-   Photo uploads are not implemented.
-   AI-based text/image matching is not implemented.
-   Notifications and item-collection tracking are not implemented.
-   Contact details and private messaging are not implemented.
-   The current CRUD endpoints should not be exposed publicly without
    authentication and authorization.

## Planned Improvements

1.  Add user registration and secure password hashing.
2.  Associate each report with its creator.
3.  Add authorization so users can edit or delete only their own
    reports.
4.  Add image upload and safe image storage.
5.  Add a contact-request flow that protects personal phone numbers.
6.  Add rule-based matching, followed by text and image similarity.
7.  Add notifications and item-return status.
8.  Add database migrations with Alembic.
9.  Add automated tests and deployment configuration.

## Security Notes

-   Never publish database credentials, API secrets, or student phone
    numbers in source control.
-   Before real campus use, add authentication, authorization, input
    limits, upload validation, and appropriate privacy controls.
-   Do not rely on a possible match alone to prove ownership. Use a safe
    item-claim verification process.

## Learning Goals

This project demonstrates:

-   REST API design with FastAPI
-   HTTP methods and endpoint routing
-   Pydantic request/response validation
-   SQLAlchemy ORM models and CRUD operations
-   PostgreSQL persistence
-   Frontend-to-backend communication with JavaScript `fetch()`
-   Basic search and filtering

## License

Add a license here if you plan to publish or distribute this project.
