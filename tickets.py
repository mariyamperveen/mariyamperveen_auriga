from database import get_connection


def get_all_tickets():
    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tickets")

    tickets = cursor.fetchall()

    cursor.close()
    connection.close()

    return tickets