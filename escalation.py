from datetime import datetime
from database import get_connection


def escalate_overdue_tickets():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, priority, deadline
        FROM tickets
        WHERE deadline < NOW()
    """)

    tickets = cursor.fetchall()

    for ticket in tickets:

        if ticket["priority"] == "normal":
            new_priority = "high"

        elif ticket["priority"] == "high":
            new_priority = "urgent"

        else:
            continue

        cursor.execute("""
            UPDATE tickets
            SET priority = %s
            WHERE id = %s
        """, (new_priority, ticket["id"]))

    connection.commit()

    cursor.close()
    connection.close()