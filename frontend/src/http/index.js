import axios, { withCredentials } from "axios";
import { getCookie } from "../_helpers";
// import { history } from '../_helpers';
// import { getCSRFToken } from 'components/utils';

export const API_URL = "http://localhost:5000/api/v1/";


const $api = axios.create({
    baseURL: API_URL,
    withCredentials: true,
    origin: "http://localhost:3000",
    headers: {
      "Access-Control-Allow-Origin": "*"
      }
})

$api.interceptors.request.use((config) => {
    const token = getCookie('csrf_access_token');
    if (token){
        config.headers.common['X-CSRF-TOKEN-ACCESS'] = token;
    }
    return config;
})

export default $api;