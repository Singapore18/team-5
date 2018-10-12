function populateEmployees() {
    let parent = document.getElementById("employees");
    parent.innerHTML = "";

    for(let i = 0; i < 3; i++) {
        let cardDiv = document.createElement("div");
        cardDiv.className = "col-3 card employeeCard";

        let cardBody = document.createElement("div");
        cardBody.className = "card-body";

        let cardTitle = document.createElement("h5");
        cardTitle.className = "card-title";
        cardTitle.innerHTML = "Claus";
        cardBody.appendChild(cardTitle);

        let cardSubtitle = document.createElement("h6");
        cardSubtitle.className = "card-subtitle mb-2 text-muted";
        cardSubtitle.innerHTML = "\"Bringing joy to everyone\"";
        cardBody.appendChild(cardSubtitle);

        let cardBodyText = document.createElement("p");
        cardBodyText.className = "card-text";
        cardBodyText.innerHTML = "Lorem ipsum dollar"
        cardBody.appendChild(cardBodyText);

        let cardLink = document.createElement("a");
        cardLink.appendChild(document.createTextNode("I am interested to hire"));
        cardLink.className = "card-link";
        cardLink.title = "I am interested to hire";
        cardLink.href = "#";
        cardBody.appendChild(cardLink);
        cardDiv.appendChild(cardBody);
        parent.appendChild(cardDiv);
    }
}