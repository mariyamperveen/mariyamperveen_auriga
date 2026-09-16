×

dde732cc-fbe0-423c-83ca-520208ce146d.png

Perfect. 👍 This tells us:

T001 — urgent, deadline 17:11 → not overdue

T002 — normal, deadline 15:08 → overdue if the current time is after 15:08

T003 — urgent, deadline 12:00 → overdue

Now let's test your automatic escalation.

1. Don't change anything in Workbench
Leave T002 as:

T002 | Aman | normal
2. Restart your FastAPI server
In the terminal:

CTRL + C
Then:

uvicorn backend:app --reload
Your escalate_overdue_tickets() will run automatically when FastAPI starts.

3. Check Workbench again
Run:

SELECT id, customer, priority, deadline
FROM tickets;
Expected result
T002 should become:

T002 | Aman | high
because:

normal
   ↓
overdue
   ↓
high
T003 is already urgent, so it stays:

T003 | Sneha | urgent
That's exactly what the requirement says: one priority level per run, maximum.

Send me the new table after restarting FastAPI.


CREATE DATABASE helpdesk_db;

USE helpdesk_db;

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

INSERT INTO tickets
(id, customer, issue, priority, assigned_to, created_at, deadline, status)
VALUES
(
    'T001',
    'Rahul',
    'Laptop not booting',
    'urgent',
    'Priya',
    NOW(),
    DATE_ADD(NOW(), INTERVAL 2 HOUR),
    'open'
),
(
    'T002',
    'Aman',
    'Need a bigger monitor',
    'normal',
    'Arjun',
    '2026-09-16 10:00:00',
    '2026-09-16 11:00:00',
    'open'
),
(
    'T003',
    'Sneha',
    'Email not working',
    'urgent',
    'Priya',
    '2026-09-16 10:00:00',
    '2026-09-16 12:00:00',
    'open'
);

UPDATE tickets
SET deadline = NOW() - INTERVAL 1 HOUR
WHERE id = 'T002';

SELECT id, customer, priority, deadline
FROM tickets;

SELECT * FROM tickets;

Yes — this is your complete MySQL setup script. It is mostly correct, but there is one important point for our escalation test.

Your current script does this:

Creates helpdesk_db

Creates tickets

Inserts T001, T002, T003

Makes T002 overdue

Displays the tickets

For your current project, keep this SQL
CREATE DATABASE helpdesk_db;

USE helpdesk_db;

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

INSERT INTO tickets
(id, customer, issue, priority, assigned_to, created_at, deadline, status)
VALUES
(
    'T001',
    'Rahul',
    'Laptop not booting',
    'urgent',
    'Priya',
    NOW(),
    DATE_ADD(NOW(), INTERVAL 2 HOUR),
    'open'
),
(
    'T002',
    'Aman',
    'Need a bigger monitor',
    'normal',
    'Arjun',
    '2026-09-16 10:00:00',
    '2026-09-16 11:00:00',
    'open'
),
(
    'T003',
    'Sneha',
    'Email not working',
    'urgent',
    'Priya',
    '2026-09-16 10:00:00',
    '2026-09-16 12:00:00',
    'open'
);

UPDATE tickets
SET deadline = NOW() - INTERVAL 1 HOUR
WHERE id = 'T002';

SELECT id, customer, priority, deadline
FROM tickets;

SELECT * FROM tickets;
What we are testing
After this SQL runs, T002 should be:

T002 | Aman | normal | overdue
Then when your FastAPI starts and executes:

escalate_overdue_tickets()
it should automatically become:

T002 | Aman | high
while T003 remains:

T003 | Sneha | urgent
because urgent cannot be escalated further.

One important warning
Don't run the entire CREATE DATABASE + CREATE TABLE script again after you've already created the database/table, because you'll get errors such as:

Database 'helpdesk_db' already exists
and:

Table 'tickets' already exists
For now, your existing database is enough.

Next, we should verify that T002 actually changed from normal → high after FastAPI restarted.


Perfect. ✅ Now the most important part: script.js.

Open:

frontend/script.js
Paste this:

const API_URL = "https://friendly-succotash-q7pvpx5j5wjw34r46-8000.app.github.dev";


function displayTickets(tickets) {

    const container = document.getElementById("ticketContainer");

    container.innerHTML = "";

    if (tickets.length === 0) {
        container.innerHTML = "<p>No tickets found.</p>";
        return;
    }

    tickets.forEach(ticket => {

        const ticketCard = document.createElement("div");

        ticketCard.className = "ticket";

        const overdue =
            new Date(ticket.deadline) < new Date();

        if (overdue) {
            ticketCard.classList.add("overdue");
        }

        ticketCard.innerHTML = `
            <h3>${ticket.id} - ${ticket.customer}</h3>

            <p><strong>Issue:</strong> ${ticket.issue}</p>

            <p>
                <strong>Priority:</strong>
                <span class="priority">${ticket.priority}</span>
            </p>

            <p>
                <strong>Assigned To:</strong>
                ${ticket.assigned_to}
            </p>

            <p>
                <strong>Deadline:</strong>
                ${ticket.deadline}
            </p>

            <p>
                <strong>Status:</strong>
                ${ticket.status}
            </p>

            ${overdue ? "<p><strong>⚠ OVERDUE</strong></p>" : ""}
        `;

        container.appendChild(ticketCard);
    });
}


async function loadTickets() {

    const response = await fetch(`${API_URL}/tickets`);

    const tickets = await response.json();

    displayTickets(tickets);
}


async function loadOverdue() {

    const response = await fetch(`${API_URL}/tickets/overdue`);

    const tickets = await response.json();

    displayTickets(tickets);
}


async function loadMyTickets() {

    const response = await fetch(`${API_URL}/tickets/my/Priya`);

    const tickets = await response.json();

    displayTickets(tickets);
}


async function searchTickets() {

    const customerName =
        document.getElementById("searchInput").value;

    if (!customerName) {
        alert("Please enter a customer name.");
        return;
    }

    const response =
        await fetch(`${API_URL}/tickets/search/${customerName}`);

    const tickets = await response.json();

    displayTickets(tickets);
}


loadTickets();
What this JavaScript does
It connects your website to your FastAPI:

HTML
 ↓
JavaScript
 ↓
FastAPI
 ↓
MySQL
And gives you:

All Tickets → /tickets

Overdue → /tickets/overdue

My Tickets → /tickets/my/Priya

Search → /tickets/search/customer

Automatic OVERDUE display

Save it
Press:

Ctrl + S

Then tell me done.

After that, we'll open the frontend and see your actual Helpdesk Ticket System UI.


done  

Perfect. ✅ Now let's open the frontend.

Step 1 — Start a simple frontend server
Keep your FastAPI terminal running.

Open a new terminal in Codespaces and run:

cd frontend
python3 -m http.server 5500
You should see:

Serving HTTP on 0.0.0.0 port 5500
Step 2 — Open port 5500
In Codespaces:

PORTS → 5500 → Open in Browser

You should now see your:

Helpdesk Ticket System

with:

All Tickets

Overdue

My Tickets

Search customer

Ticket cards

⚠️ If the page opens but tickets don't appear
Don't change anything yet. Send me what you see.

If it shows the tickets, we'll then add the escalation button + pagination and make the project closer to the actual Auriga problem requirements.


.

If that . means you’re ready, let's continue. 👍

Step 1: Open a NEW terminal
Keep your FastAPI terminal running.

Run:

cd frontend
Then:

python3 -m http.server 5500
You should see:

Serving HTTP on 0.0.0.0 port 5500
Then go to:

Codespaces → PORTS → 5500 → Open in Browser

Tell me what appears on the webpage.


