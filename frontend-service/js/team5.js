async function populateEmployees() {
    let parent = document.getElementById("employees");
    parent.innerHTML = "";

    let candiatesResponse = await fetch('http://54.169.143.230:5000/client');
    let jsonResponse = await candiatesResponse.json();

    for(let i = 0; i < jsonResponse.length; i++) {
        let candidate = jsonResponse[i];
        let cardDiv = document.createElement("div");
        cardDiv.className = "col-3 card employeeCard";

        let cardBody = document.createElement("div");
        cardBody.className = "card-body";

        let cardTitle = document.createElement("h5");
        cardTitle.className = "card-title";
        cardTitle.innerHTML = candidate.Name;
        cardBody.appendChild(cardTitle);

        let cardSubtitle = document.createElement("h6");
        cardSubtitle.className = "card-subtitle mb-2 text-muted";
        cardSubtitle.innerHTML = candidate.Tagline;
        cardBody.appendChild(cardSubtitle);

        let cardBodyText = document.createElement("p");
        cardBodyText.className = "card-text";
        cardBodyText.innerHTML = candidate.AssistanceDesc;
        cardBody.appendChild(cardBodyText);

        let cardLink = document.createElement("a");
        cardLink.appendChild(document.createTextNode("I am interested to hire"));
        cardLink.className = "card-link";
        cardLink.title = "I am interested to hire";
        cardLink.href = `./employee/${candidate.Id}`;
        cardBody.appendChild(cardLink);
        cardDiv.appendChild(cardBody);
        parent.appendChild(cardDiv);
    }
}