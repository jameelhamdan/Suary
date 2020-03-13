import FormData from 'form-data';
import {ajax, apiRoutes} from "utils/ajax";
import UserStorage from "utils/storage";

const uploadConfig = {
  headers: {
    'content-type': 'multipart/form-data'
  }
};

export const userService = {
  getUser: async (username) => {
    return ajax.get(apiRoutes.userDetail(username)).then(res => {
      return res.data['result'];
    });
  },

  register: async (userData) => {
    return ajax.post(apiRoutes.Register(), userData).then(res => {
      return res.data['result'];
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
  updateAvatar: async (imageFile) => {
    let requestData = new FormData();

    requestData.append('avatar', imageFile, imageFile.fileName);
    return ajax.put(apiRoutes.userUpdateAvatar(), requestData, uploadConfig).then(res => {
      return res;
    });
  },
  logout: () => {
    UserStorage.clear();
  }
};
