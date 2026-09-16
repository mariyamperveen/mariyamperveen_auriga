1. README.md
# Helpdesk Ticket System

A helpdesk ticket management system that helps support teams manage, prioritize, search, filter, and escalate support tickets.

## Problem

A helpdesk receives many tickets with different priorities and response deadlines.

The system must always help the support team identify the most pressing ticket. Tickets that have passed their promised response time must be treated as overdue.

The system also supports filtering, searching, assignment, pagination, and automatic priority escalation.

## Features

- View all tickets
- Prioritize tickets based on urgency
- Identify overdue tickets
- View tickets assigned to a particular employee
- Search tickets by customer name
- Pagination support
- Automatic escalation of overdue tickets
- REST API using FastAPI
- MySQL database
- Browser-based frontend
- GitHub Codespaces compatible

## Priority Escalation

Overdue tickets are automatically escalated by one level per run:

```text
normal → high
high → urgent
urgent → urgent

A ticket can increase by only one priority level during a single escalation run.

Technologies Used
Python
FastAPI
MySQL
MySQL Connector/Python
HTML
CSS
JavaScript
GitHub Codespaces
Project Structure
helpdesk-ticket-system/
│
├── backend.py
├── database.py
├── tickets.py
├── queue_logic.py
├── filters.py
├── search.py
├── pagination.py
├── escalation.py
├── requirements.txt
├── README.md
├── REASONING.md
├── AI_LOGS.md
│
└── frontend/
    ├── index.html
    ├── style.css
    └── script.js
Database Setup

Create the database:

CREATE DATABASE helpdesk_db;

USE helpdesk_db;

Create the tickets table:

CREATE TABLE tickets (
    id VARCHAR(20) PRIMARY KEY,
    customer VARCHAR(100) NOT NULL,
    issue TEXT NOT NULL,
    priority VARCHAR(20) NOT NULL,
    assigned_to VARCHAR(100),
    created_at DATETIME NOT NULL,
    deadline DATETIME NOT NULL,
    status VARCHAR(20) DEFAULT 'open'
);

Create the application user:

CREATE USER 'helpdesk_user'@'localhost' IDENTIFIED BY 'YOUR_PASSWORD';

GRANT ALL PRIVILEGES ON helpdesk_db.* 
TO 'helpdesk_user'@'localhost';

FLUSH PRIVILEGES;

Update the password in database.py.

Installation

Install the required Python packages:

pip install -r requirements.txt

Or:

pip install fastapi uvicorn mysql-connector-python
Run the Backend

Start FastAPI:

uvicorn backend:app --reload

The backend runs on port 8000.

API Endpoints
Home
GET /
All Tickets
GET /tickets
Overdue Tickets
GET /tickets/overdue
Tickets Assigned to an Employee
GET /tickets/my/{employee_name}

Example:

GET /tickets/my/Priya
Search by Customer
GET /tickets/search/{customer_name}

Example:

GET /tickets/search/Rahul
Run the Frontend

Open another terminal:

cd frontend
python3 -m http.server 5500

Open the frontend using the Codespaces port 5500 URL.

Queue Logic

The queue considers:

Whether the ticket is overdue.
Ticket priority.
Ticket deadline.

Overdue tickets are placed at the front of the queue so that breached response-time commitments are handled first.

Automatic Escalation

The escalation process checks tickets whose deadline has passed.

For every overdue ticket:

normal → high
high → urgent
urgent → no change

Only one level is increased during one execution.

Debugging
Backend does not start

Check whether port 8000 is already in use.

lsof -i :8000

If the server is already running, do not start another instance.

Frontend port is already in use

Check port 5500:

lsof -i :5500

If a frontend server is already running, use the existing server.

Database connection problem

Check:

MySQL is running.
Database name is correct.
Username is correct.
Password is correct.
database.py has the correct connection details.
Test the backend

Open:

/tickets

If ticket JSON is returned, the backend and database are communicating correctly.

Testing

The system can be tested using the following cases:

Normal ticket within deadline
Overdue normal ticket
Overdue high ticket
Overdue urgent ticket
Queue ordering
Overdue filtering
Employee filtering
Customer search
Pagination
API responses
Database connection
Author

Mariyam Perveen

B.Tech Artificial Intelligence and Data Science
Poornima University