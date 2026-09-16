def paginate(tickets, page=1, per_page=5):
    start = (page - 1) * per_page
    end = start + per_page

    return tickets[start:end]