from datetime import datetime


def is_overdue(ticket):
    return datetime.now() > ticket["deadline"]


def priority_value(priority):
    if priority == "urgent":
        return 0
    return 1


def sort_tickets(tickets):
    return sorted(
        tickets,
        key=lambda ticket: (
            not is_overdue(ticket),
            priority_value(ticket["priority"]),
            ticket["deadline"]
        )
    )