import {ajax, apiRoutes} from "utils/ajax";
import UserStorage from "utils/storage";


export const userService = {
  register: async (userData) => {
    return ajax.post(apiRoutes.Register(), userData).then(res => {
      return res;
    })
  },
  login: async (userData) => {
    return ajax.post(apiRoutes.Login(), userData).then(res => {
      const data = res.data["result"];
      UserStorage.clear();
      UserStorage.storeToken(data["auth_token"]);
      UserStorage.storeRefreshToken(data["refresh_token"]);

      const user_data = {
        "uuid": data["uuid"],
        "username": data["username"],
        "full_name": data["full_name"],
        "avatar_uuid": data["avatar_uuid"],
        "logged_in": true
      };

      UserStorage.storeUserData(user_data);

      return user_data;
    })
  },
  logout: () => {
    UserStorage.clear();
  }
};
