const todo = document.querySelector('#todo')
const requestURL = 'https://jsonplaceholder.typicode.com/users'

async function getUsers(requestURL) {
    const response = await fetch(requestURL)
    const result = await response.json()

    let list = document.querySelector('.block-principles .content')

    let key;
    for (key in result) {
        list.innerHTML += `
        <div class="span_list">
            <span class="spa" contentEditable="true">${result[key].id} ${result[key].email}</span>
            <img style="width: 16px" class="dlt" src="icons/delete.svg" alt="delete">
        </div>
            `
    }

    list.addEventListener('click', function (event) {
        event.target.remove(list);
        span_list.splice(key, 1)
    })

    console.log(result);
}

getUsers(requestURL)






const edit = document.querySelector('.edit')

edit.onclick = (event) => {
    if (event.target.classList.contains('edit-save')) {
        event.target.classList.remove('edit-save')
    } else {
        event.target.classList.add('edit-save')
    }
}

const handleEditClick = () => {
    document.querySelector(".input-list").classList.remove("hide")
}

document.querySelector(".edit").addEventListener("click", handleEditClick)

