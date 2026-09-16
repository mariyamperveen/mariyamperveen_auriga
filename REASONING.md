# Reasoning Behind the Solution

## 1. Understanding the Problem

The main requirement is to build a helpdesk ticket system where the most pressing ticket is always easy to identify.

Each ticket contains:

- Ticket ID
- Customer
- Issue
- Priority
- Assigned employee
- Creation time
- Response deadline
- Status

The ordering of the ticket queue is the central part of the solution.

## 2. Queue Ordering

The first important condition is whether a ticket is overdue.

A ticket is overdue when its deadline has already passed.

Overdue tickets must be brought to the front because the agreed response time has already been breached.

After considering overdue status, the ticket priority is considered.

The priority levels are:

```text
urgent
high
normal

Earlier deadlines are also considered when tickets have otherwise similar priority.

3. Overdue Tickets

A separate overdue filter is provided so that the helpdesk can quickly identify tickets whose response deadline has been breached.

The system compares the ticket deadline with the current time.

4. Employee Assignment

The system needs to support the question:

Which tickets are assigned to me?

The employee filter searches the assigned_to field.

The comparison is case-insensitive so that names such as Priya and priya are treated consistently.

5. Customer Search

The system supports searching tickets by customer name.

For example:

/tickets/search/Rahul

returns matching tickets.

Partial customer names are supported because the search checks whether the search text occurs inside the customer's name.

6. Pagination

A real helpdesk can contain a large number of tickets.

Displaying the complete list at once is not practical.

The pagination module therefore divides the tickets into smaller pages.

The basic calculation is:

start = (page - 1) × items_per_page
end = start + items_per_page

Only the required section of the ticket list is returned.

7. Automatic Escalation

The additional requirement introduces automatic escalation for overdue tickets.

The rules are:

normal → high
high → urgent
urgent → urgent

The important constraint is that a ticket can increase by only one level during one execution.

Therefore, a normal ticket cannot directly become urgent in a single run.

For example:

Run 1:
normal → high

Run 2:
high → urgent

This satisfies the one-level-per-run requirement.

8. Database

MySQL is used for persistent ticket storage.

The main ticket table contains:

id
customer
issue
priority
assigned_to
created_at
deadline
status

Using a database means the ticket information remains available after restarting the application.

9. Backend Structure

FastAPI is used to provide REST API endpoints.

The application is separated into modules so that each module has a clear responsibility.

database.py       → database connection
tickets.py        → ticket retrieval
queue_logic.py    → queue ordering
filters.py        → ticket filtering
search.py         → customer search
pagination.py     → pagination
escalation.py     → priority escalation
backend.py        → FastAPI application

This separation makes the code easier to test and debug.

10. Frontend

The frontend uses HTML, CSS, and JavaScript.

JavaScript communicates with the FastAPI backend using HTTP requests.

The interface provides:

All Tickets
Overdue
My Tickets
Search

Ticket information is displayed as individual ticket cards.

11. API Design

The backend provides separate endpoints for different operations.

GET /
GET /tickets
GET /tickets/overdue
GET /tickets/my/{employee_name}
GET /tickets/search/{customer_name}

This keeps the API simple and makes each operation easy to test independently.

12. AI-Assisted Development

AI assistance was used during development to:

Understand the problem statement
Break the problem into smaller modules
Design the application structure
Generate implementation ideas
Debug errors
Understand FastAPI and GitHub Codespaces
Test and improve the implementation

AI-generated suggestions were reviewed and adapted to the actual project requirements.

The final solution was tested using the project environment and database.

13. Testing Strategy

The following cases were considered.

Case 1: Normal Ticket

A normal ticket that has not breached its deadline should remain normal.

Case 2: Overdue Normal Ticket

An overdue normal ticket should become high after one escalation run.

Case 3: Overdue High Ticket

An overdue high ticket should become urgent after one escalation run.

Case 4: Overdue Urgent Ticket

An overdue urgent ticket should remain urgent.

Case 5: Queue Ordering

Overdue tickets should appear before tickets that have not breached their deadlines.

Case 6: Employee Filter

The employee filter should return tickets assigned to the requested employee.

Case 7: Customer Search

Customer search should return matching tickets.

Case 8: Pagination

Large ticket lists should be divided into smaller pages.

14. Design Approach

The solution focuses on:

Correct queue ordering
Simple modular code
Persistent database storage
Automatic escalation
Easy API testing
Easy debugging
A simple browser interface

The implementation is designed to be reusable for a general helpdesk rather than being specific to one person or one set of tickets.


**That's it for these two.** `README.md` = replace/update existing content; `REASONING.md` = create new a