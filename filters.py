from queue_logic import is_overdue


def get_overdue_tickets(tickets):
    return [ticket for ticket in tickets if is_overdue(ticket)]


def get_my_tickets(tickets, employee_name):
    return [
        ticket
        for ticket in tickets
        if ticket["assigned_to"].lower() == employee_name.lower()
    ]