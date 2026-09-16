from tickets import get_all_tickets
from queue_logic import sort_tickets
from filters import get_overdue_tickets, get_my_tickets
from search import search_by_customer
from pagination import paginate


# Get tickets from MySQL
tickets = get_all_tickets()

# Arrange tickets according to priority rules
ordered_tickets = sort_tickets(tickets)


print("\n--- MAIN QUEUE ---")

for ticket in ordered_tickets:
    print(
        ticket["id"],
        "|", ticket["customer"],
        "|", ticket["priority"],
        "|", ticket["assigned_to"]
    )


print("\n--- OVERDUE TICKETS ---")

overdue = get_overdue_tickets(tickets)

for ticket in overdue:
    print(ticket["id"], "|", ticket["customer"])


print("\n--- PRIYA'S TICKETS ---")

my_tickets = get_my_tickets(tickets, "Priya")

for ticket in my_tickets:
    print(ticket["id"], "|", ticket["customer"])


print("\n--- SEARCH: RAHUL ---")

results = search_by_customer(tickets, "Rahul")

for ticket in results:
    print(ticket["id"], "|", ticket["customer"])


print("\n--- PAGE 1 ---")

page = paginate(ordered_tickets, page=1, per_page=2)

for ticket in page:
    print(ticket["id"], "|", ticket["customer"])