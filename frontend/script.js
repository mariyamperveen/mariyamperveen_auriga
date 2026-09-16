const API_URL = "https://friendly-succotash-q7pvpx5j5wjw34r46-8000.app.github.dev";

function displayTickets(tickets) {
    const container = document.getElementById("ticketContainer");

    if (!tickets || tickets.length === 0) {
        container.innerHTML = "<p>No tickets found.</p>";
        return;
    }

    container.innerHTML = "";

    tickets.forEach(ticket => {
        const card = document.createElement("div");
        card.className = "ticket";

        const overdue = new Date(ticket.deadline) < new Date();

        if (overdue) {
            card.classList.add("overdue");
        }

        card.innerHTML = `
            <h3>${ticket.id} - ${ticket.customer}</h3>
            <p><strong>Issue:</strong> ${ticket.issue}</p>
            <p><strong>Priority:</strong> ${ticket.priority}</p>
            <p><strong>Assigned To:</strong> ${ticket.assigned_to}</p>
            <p><strong>Deadline:</strong> ${ticket.deadline}</p>
            <p><strong>Status:</strong> ${ticket.status}</p>
            ${overdue ? "<p><strong>⚠ OVERDUE</strong></p>" : ""}
        `;

        container.appendChild(card);
    });
}

async function loadTickets() {
    try {
        const response = await fetch(`${API_URL}/tickets`);

        if (!response.ok) {
            throw new Error("Could not load tickets");
        }

        const tickets = await response.json();
        displayTickets(tickets);

    } catch (error) {
        console.error(error);
        document.getElementById("ticketContainer").innerHTML =
            "<p>Data Loading...</p>";
    }
}

async function loadOverdue() {
    try {
        const response = await fetch(`${API_URL}/tickets/overdue`);
        const tickets = await response.json();
        displayTickets(tickets);
    } catch (error) {
        console.error(error);
    }
}

async function loadMyTickets() {
    try {
        const response = await fetch(`${API_URL}/tickets/my/Priya`);
        const tickets = await response.json();
        displayTickets(tickets);
    } catch (error) {
        console.error(error);
    }
}

async function searchTickets() {
    const name = document.getElementById("searchInput").value.trim();

    if (!name) {
        alert("Please enter a customer name.");
        return;
    }

    try {
        const response =
            await fetch(`${API_URL}/tickets/search/${encodeURIComponent(name)}`);

        const tickets = await response.json();
        displayTickets(tickets);
    } catch (error) {
        console.error(error);
    }
}

loadTickets();