import FormData from 'form-data';
import {ajax, apiRoutes} from "utils/ajax";

const uploadConfig = {
  headers: {
    'content-type': 'multipart/form-data'
  }
};

export const postService = {
  getUserPosts: async (username, cursor = null) => {
    return ajax.get(apiRoutes.userPostsList(username, cursor)).then(res => {
      return res.data['result'];
    });
  },
  addPost: async (content, imageFile) => {
    let requestData = new FormData();

    requestData.set('content', content);
    requestData.append('media_list', imageFile, imageFile.fileName);
    return ajax({
      method: 'post',
      url: apiRoutes.addPost(),
      data: requestData,
      headers: uploadConfig
    }).then(res => {
      return res;
    });
  },
};
