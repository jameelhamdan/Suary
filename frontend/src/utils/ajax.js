import axios from "axios";
import {apiRoutes} from "utils/apiRoutes";
import UserStorage from "utils/storage";

const headers = {};
const refresh_token_url = apiRoutes.Root() + '/' + apiRoutes.refreshToken();

// Should be the raw response data, with the success or not;
const get_errors = function (result) {
  let errors = [];
  let i = 1;
  if (result.success === false) {
    for (let [key, value] of Object.entries(result["result"])) {
      if (Array.isArray(value)) {
        value.forEach(message => {
          errors.push({i: i, message: message});
          i++;
        });
      } else {
        errors.push({i: i, message: value});
        i++;
      }
    }
  }

  return errors;
};


let Ajax = axios.create({
  baseURL: apiRoutes.Root(),
  timeout: 27000,
  headers: headers,
});

let rawAjax = axios.create({
  baseURL: apiRoutes.Root(),
  timeout: 27000,
});

Ajax.interceptors.request.use(
  config => {
    const token = UserStorage.getToken();
    if (token) {
      config.headers["Authorization"] = "Bearer " + token;
    }
    return config;
  },
  error => {
    Promise.reject(error)
  });

Ajax.interceptors.response.use((response) => {
    return response
  }, function (error) {
    const originalRequest = error.config;
    console.log(originalRequest);
    if (error.response.status === 401 && originalRequest.url === refresh_token_url) {
      UserStorage.clear();
      window.location = "/login";
      return Promise.reject(error);
    }

    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      const refreshToken = UserStorage.getRefreshToken();
      const payload = {
        refresh_token: refreshToken
      }

      return rawAjax({
        method: 'post',
        url: apiRoutes.refreshToken(),
        data: payload
      }).then((res) => {
        if (res.status === 200) {
          const result = res.data['result'];
          UserStorage.storeRefreshToken(result["refresh_token"]);
          UserStorage.storeToken(result["token"]);
          Ajax.defaults.headers.common["Authorization"] = "Bearer " + UserStorage.getToken();
          return Ajax(originalRequest);
        }
      })
    }
    return Promise.reject(error);
  }
);


export {
  Ajax as ajax,
  apiRoutes,
  get_errors
};

