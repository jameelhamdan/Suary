import FormData from 'form-data';
import {ajax, apiRoutes} from "utils/ajax";

const uploadConfig = {
  headers: {
    'content-type': 'multipart/form-data'
  }
};

export const postService = {
  getUserPosts: async (username, cursor=null) => {
    return ajax.get(apiRoutes.userPostsList(username, cursor)).then(res => {
      return res.data['result'];
    });
  },
};
