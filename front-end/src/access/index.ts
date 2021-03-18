const axios = require('axios');

const BASE_URL = 'http://192.168.1.113:8001';

const headers = {
    'Authorization': 'Basic Og==',
    'Content-Type': 'application/json',
    'accept': '*/*',
    'Access-Control-Allow-Origin': '*'
};

const APIPost = async (url: string, data?: Object) => {
    return await axios({
        method: 'POST',
        url: `${BASE_URL}/${url}`,
        headers: headers,
        data: data
    });
};

export const DataAccess = {
    Post: APIPost,
};