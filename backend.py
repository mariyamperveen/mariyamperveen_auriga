from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tickets import get_all_tickets
from queue_logic import sort_tickets
from filters import get_overdue_tickets, get_my_tickets
from search import search_by_customer
from escalation import escalate_overdue_tickets

app = FastAPI(title="Helpdesk Ticket System")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
escalate_overdue_tickets()



@app.get("/")
def home():
    return {"message": "Helpdesk API is running"}


@app.get("/tickets")
def get_tickets():
    tickets = get_all_tickets()
    return sort_tickets(tickets)


@app.get("/tickets/overdue")
def overdue_tickets():
    tickets = get_all_tickets()
    return get_overdue_tickets(tickets)


@app.get("/tickets/my/{employee_name}")
def my_tickets(employee_name: str):
    tickets = get_all_tickets()
    return get_my_tickets(tickets, employee_name)


@app.get("/tickets/search/{customer_name}")
def search_tickets(customer_name: str):
    tickets = get_all_tickets()
    return search_by_customer(tickets, customer_name)