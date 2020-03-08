import axios from 'axios';
import "./interceptor"
import apiRoutes from "../apiRoutes";

const api_root_url = document.getElementById("app").getAttribute('api-root-url');
const headers = {

};

let Ajax = axios.create({
  baseURL: api_root_url,
  timeout: 10000,
  headers: headers
});

export {
  Ajax as ajax,
  apiRoutes as apiRoutes
};

