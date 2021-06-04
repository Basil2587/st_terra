import axios from 'axios';
const API_URL = 'http://localhost:8000';


const getResults = async (urll) => {
    const url = `${API_URL}/api/v1/${urll}`;
    const res = await axios({
        method: 'get',
        url: url,
        // data: params,
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer ' + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI0ODg2MzkwLCJqdGkiOiI3ZTIxZGZmY2YzOGU0YmJlYjNmOWM4NGUxYzYxNWQ2ZCIsInVzZXJfaWQiOjF9._I8CimQyZ2vjcIWwpPfsAZdPfm36_slqDy9fDJ3Cbic'
        },
    });
    return await res.data;
}

const postResults = async (data, urll) => {
    const url = `${API_URL}/api/v1/${urll}`;
    fetch(url, {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json',
        },
        body: data,
    })
        .then(response => response.json())
}

export {
    getResults,
    postResults
};

    // getCustomersByURL(link){
    //     const url = `${API_URL}${link}`;
    //     return axios.get(url).then(response => response.data);
    // }
    // getCustomer(pk) {
    //     const url = `${API_URL}/api/customers/${pk}`;
    //     return axios.get(url).then(response => response.data);
    // }
    // deleteCustomer(customer){
    //     const url = `${API_URL}/api/customers/${customer.pk}`;
    //     return axios.delete(url);
    // }
    // createCustomer(customer){
    //     const url = `${API_URL}/api/customers/`;
    //     return axios.post(url,customer);
    // }
    // updateCustomer(customer){
    //     const url = `${API_URL}/api/customers/${customer.pk}`;
    //     return axios.put(url,customer);
    // }

