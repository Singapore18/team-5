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

        let cardHireLink = document.createElement("a");
        cardHireLink.appendChild(document.createTextNode("I am interested to hire"));
        cardHireLink.className = "card-link";
        cardHireLink.title = "I am interested to hire";
        cardHireLink.href = "#";
        cardBody.appendChild(cardHireLink);

        let cardLink = document.createElement("a");
        cardLink.appendChild(document.createTextNode("View Profile"));
        cardLink.className = "card-link";
        cardLink.title = "View Profile";
        cardLink.href = `./employee/${candidate.Id}`;
        cardBody.appendChild(cardLink);

        cardDiv.appendChild(cardBody);
        parent.appendChild(cardDiv);
    }
}


async function populateClientList() {
    let parent = document.getElementById("clientTableBody");
    parent.innerHTML = "";

    let listResponse = await fetch("http://54.169.143.230:5000/list/client");
    let jsonResponse = await listResponse.json();

    for(let i = 0; i < jsonResponse.length; i++) {
        const row = jsonResponse[i];

        let tableRow = document.createElement("tr");

        let nameColumnn = document.createElement("td");
        nameColumnn.innerText = row.name;
        tableRow.appendChild(nameColumnn);

        let viewResumeColumn = document.createElement("td");
        let viewResumeLink = document.createElement("a");
        viewResumeLink.appendChild(document.createTextNode("View Client Resume"));
        viewResumeLink.className = "card-link";
        viewResumeLink.title = "View client's resume";
        viewResumeLink.href = `./profile.html?name=${row.id}`;
        viewResumeColumn.appendChild(viewResumeLink);
        tableRow.appendChild(viewResumeColumn);

        let editResumeColumn = document.createElement("td");
        let editResumeLink = document.createElement("a");
        editResumeLink.appendChild(document.createTextNode("Edit Client Resume"));
        editResumeLink.className = "card-link";
        editResumeLink.title = "Edit client resume";
        editResumeLink.href = `./client/edit?name=${row.id}`;
        editResumeColumn.appendChild(editResumeLink)
        tableRow.appendChild(editResumeColumn);

        let ageColumn = document.createElement("td");
        ageColumn.innerText = row.age;
        tableRow.appendChild(ageColumn);

        let addressColumn = document.createElement("td");
        addressColumn.innerText = row.address;
        tableRow.appendChild(addressColumn);

        let interestColumn = document.createElement("td");
        interestColumn.innerText = row.interest;
        tableRow.appendChild(interestColumn);

        parent.appendChild(tableRow)
    }
}


async function populateResumeProfile(clientName) {
    let parent = document.getElementById("profileContent");
    parent.innerHTML = "";

    const profileReponse = await fetch(`http://54.169.143.230:5000/resume/${clientName}`);
    const jsonResponse = await profileReponse.json();

    let headerRow = document.createElement("div");
    headerRow.className = "row";
    let headerDetailsCol = document.createElement("div");
    headerDetailsCol.className = "col-8 flex-column";
    let name = document.createElement("h4");
    name.innerText = jsonResponse.firstName + " " + jsonResponse.familyName
    headerDetailsCol.appendChild(name);
    let subDetails = document.createElement("p");
    subDetails.innerText = jsonResponse.gender + ", " + jsonResponse.nric;
    headerDetailsCol.appendChild(subDetails);
    let careerCoach = document.createElement("h6");
    careerCoach.innerText = "Career Coach: " + jsonResponse.careerCoach;
    headerDetailsCol.appendChild(careerCoach);

    let imageDetailsCol = document.createElement("div");
    imageDetailsCol.className = "col-4 flex-column";
    let image = document.createElement("img");
    image.src = jsonResponse.url;
    imageDetailsCol.appendChild(image);
    let tag = document.createElement("p");
    tag.innerText = jsonResponse.tagline;
    imageDetailsCol.appendChild(tag);

    headerRow.appendChild(headerDetailsCol);
    headerRow.appendChild(imageDetailsCol);
    parent.appendChild(headerRow);


    let interestLocationRow = document.createElement("div");
    interestLocationRow.className = "row";
    let interestsCol = document.createElement("div");
    interestsCol.className = "col-8 flex-column";
    let interestTitle = document.createElement("h4");
    interestTitle.innerText = "Interests";
    interestsCol.appendChild(interestTitle);
    let interests = document.createElement("p");
    interests.innerText = jsonResponse.ind_paragraph;
    interestsCol.appendChild(interests);
    interestLocationRow.appendChild(interestsCol);
    let locationCol = document.createElement("div");
    locationCol.className = "col-4";
    let locationTitle = document.createElement("h4");
    locationTitle.innerText = "Location";
    locationCol.appendChild(locationTitle);
    let location = document.createElement("p");
    location.innerText = jsonResponse.address;
    locationCol.appendChild(location);
    interestLocationRow.appendChild(locationCol);
    parent.appendChild(interestLocationRow);


    let strengthTimingRow = document.createElement("div");
    strengthTimingRow.className = "row";
    let strengthCol = document.createElement("div");
    strengthCol.className = "col-8 flex-column";
    let strengthTitle = document.createElement("h4");
    strengthTitle.innerText = "Strength";
    strengthCol.appendChild(strengthTitle);
    let strength = document.createElement("p");
    strength.innerText = jsonResponse.str_paragraph;
    strengthCol.appendChild(strength);
    strengthTimingRow.appendChild(strengthCol);
    let timingCol = document.createElement("div");
    timingCol.className = "col-4";
    let timingTitle = document.createElement("h4");
    timingTitle.innerText = "Timing";
    timingCol.appendChild(timingTitle);
    let timing = document.createElement("p");
    timing.innerText = jsonResponse.timeAvailability;
    timingCol.appendChild(timing);
    strengthTimingRow.appendChild(timingCol);
    parent.appendChild(strengthTimingRow);


    let experienceAssistanceRow = document.createElement("div");
    experienceAssistanceRow.className = "row";
    let experienceCol = document.createElement("div");
    experienceCol.className = "col-8 flex-column";
    let experienceTitle = document.createElement("h4");
    experienceTitle.innerText = "Experience";
    experienceCol.appendChild(experienceTitle);
    let experience = document.createElement("p");
    experience.innerText = jsonResponse.experience;
    experienceCol.appendChild(experience);
    experienceAssistanceRow.appendChild(experienceCol);
    let assistanceCol = document.createElement("div");
    assistanceCol.className = "col-4";
    let assistanceTitle = document.createElement("h4");
    assistanceTitle.innerText = "Assistance";
    assistanceCol.appendChild(assistanceTitle);
    let assistance = document.createElement("p");
    assistance.innerText = jsonResponse.assistance;
    assistanceCol.appendChild(assistance);
    experienceAssistanceRow.appendChild(assistanceCol);
    parent.appendChild(experienceAssistanceRow);
}