import axios from 'axios';
import "./interceptor"
import apiRoutes from "../apiRoutes";

const api_root_url = document.getElementById("app").getAttribute('api-root-url');
const headers = {};

// Should be the raw response data, with the success or not;
const get_errors = function (result) {
  let errors = [];
  let i=1;
  if (result.success === false) {
    for (let [key, value] of Object.entries(result['result'])) {
      if (Array.isArray(value)){
        value.forEach(message => {
          errors.push({i:i, message:message});
          i++;
        });
      } else {
        errors.push({i:i, message:value});
        i++;
      }
    }
  }

  return errors;
};

let Ajax = axios.create({
  baseURL: api_root_url,
  timeout: 10000,
  headers: headers
});

export {
  Ajax as ajax,
  apiRoutes,
  get_errors
};

