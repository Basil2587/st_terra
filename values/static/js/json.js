//import axios from 'axios';
const API_URL = 'http://localhost:8000';

let suka = []
async function getResults() {
    const url = `${API_URL}/api/v1/results/`;
    const res = await axios({
        method: 'get',
        url: url,
        // data: params,
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer ' + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI0ODg2MzkwLCJqdGkiOiI3ZTIxZGZmY2YzOGU0YmJlYjNmOWM4NGUxYzYxNWQ2ZCIsInVzZXJfaWQiOjF9._I8CimQyZ2vjcIWwpPfsAZdPfm36_slqDy9fDJ3Cbic'
        },
    });
    suka.push(res.data)

}

getResults()
console.log(suka)

// let suka = null

// let result = getResults().then((res)=>{
//     suka.push(res.data)
// });


json.myValues.forEach((item) => {
    document.getElementById("my-values").insertAdjacentHTML(
        "beforeend",
        `
            <span>${item.id}. ${item.data}</span>
        `
    );
});

json.myPrinciples.forEach((item) => {
    document.getElementById("my-principles").insertAdjacentHTML(
        "beforeend",
        `
            <span>${item.id}. ${item.data}</span>
        `
    );
});

json.myQuotes.forEach((item) => {
    document.getElementById("my-quotes").insertAdjacentHTML(
        "beforeend",
        `
            <li><span>${item.data}</span></li>
        `
    );
});

json.myAlgorithmsBusiness.forEach((item) => {
    document.getElementById("content-business").insertAdjacentHTML(
        "beforeend",
        `
        <div class="notes">
            <span contentEditable="true">${item.id}. ${item.data}</span>
        </div>
        `
    );
});

json.myAlgorithmsRelationships.forEach((item) => {
    document.getElementById("content-relationships").insertAdjacentHTML(
        "beforeend",
        `
        <div class="notes">
            <span contentEditable="true">${item.id}. ${item.data}</span>
        </div>
        `
    );
});
