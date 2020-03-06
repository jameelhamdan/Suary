import axios from 'axios';
import "./interceptor"

const api_root_url = document.getElementById("app").getAttribute('api-root-url');
const headers = {

};

let Ajax = axios.create({
  baseURL: api_root_url,
  timeout: 10000,
  headers: headers
});

export default Ajax
