def search_by_customer(tickets, customer_name):
    return [
        ticket
        for ticket in tickets
        if customer_name.lower() in ticket["customer"].lower()
    ]