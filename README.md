# CampusLost AI — College Lost & Found Backend

A simple backend for a college Lost & Found management system built using **Python, FastAPI, SQLAlchemy ORM, and PostgreSQL**.

The application allows students to report lost items, report found items, and search for items using keywords, categories, and locations.

## Features

* Report lost items with details such as name, description, category, location, and date lost.
* Report found items with details such as name, description, category, location, and date found.
* Retrieve all lost and found item reports.
* Retrieve individual reports using their IDs.
* Update existing reports.
* Delete reports.
* Search items by keyword, category, and location.
* Filter search results by lost items, found items, or both.
* Validate request data using Pydantic.
* Store and manage data using PostgreSQL and SQLAlchemy ORM.
* Test API endpoints using Swagger UI.

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
└── requirements.txt
```

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

**Note:** Never upload your actual database password to a public repository.

### 6. Run the application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically generates interactive API documentation.

* **Swagger UI:** http://127.0.0.1:8000/docs
* **ReDoc:** http://127.0.0.1:8000/redoc

Use Swagger UI to test the endpoints without needing a separate frontend.

## API Endpoints

### Lost Items

| Method | Endpoint                | Description                |
| ------ | ----------------------- | -------------------------- |
| POST   | `/lost-items`           | Create a lost-item report  |
| GET    | `/lost-items`           | Retrieve all lost items    |
| GET    | `/lost-items/{item_id}` | Retrieve a lost item by ID |
| PATCH  | `/lost-items/{item_id}` | Update a lost-item report  |
| DELETE | `/lost-items/{item_id}` | Delete a lost-item report  |

### Found Items

| Method | Endpoint                 | Description                 |
| ------ | ------------------------ | --------------------------- |
| POST   | `/found-items`           | Create a found-item report  |
| GET    | `/found-items`           | Retrieve all found items    |
| GET    | `/found-items/{item_id}` | Retrieve a found item by ID |
| PATCH  | `/found-items/{item_id}` | Update a found-item report  |
| DELETE | `/found-items/{item_id}` | Delete a found-item report  |

### Search

| Method | Endpoint  | Description                   |
| ------ | --------- | ----------------------------- |
| GET    | `/search` | Search lost and found reports |

Supported query parameters:

| Parameter   | Description                         |
| ----------- | ----------------------------------- |
| `keyword`   | Search item names and descriptions  |
| `category`  | Filter by item category             |
| `location`  | Filter by location                  |
| `item_type` | Filter by `lost`, `found`, or `all` |

Example requests:

```text
/search?keyword=wallet&item_type=all
/search?location=Library&item_type=found
/search?category=Electronics&item_type=lost
```

## Example Request

Create a lost-item report using `POST /lost-items`:

```json
{
  "item_name": "Identity Card (ID)",
  "description": "ID card of a student",
  "category": "Accessories",
  "location": "Academic Block",
  "date_lost": "2026-09-26"
}
```

Create a found-item report using `POST /found-items`:

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
