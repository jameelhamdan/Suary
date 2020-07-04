import FormData from 'form-data';
import {ajax, apiRoutes} from "utils/ajax";

const uploadConfig = {
  headers: {
    'content-type': 'multipart/form-data'
  }
};

const jsonConfig = {
  headers: {
    'content-type': 'application/json'
  }
};

export const postService = {
  getUserPosts: async (username, cursor = null) => {
    return ajax.get(apiRoutes.userPostsList(username, cursor)).then(res => {
      return res.data['result'];
    });
  },
  getPost: async (id) => {
    return ajax.get(apiRoutes.getPost(id)).then(res => {
      return res.data['result'];
    });
  },
  addPost: async (content, imageFile) => {
    let payload = new FormData();

    payload.set('content', content);
    payload.append('media_list', imageFile, imageFile.fileName);
    return ajax({
      method: 'post',
      url: apiRoutes.addPost(),
      data: payload,
      headers: uploadConfig
    }).then(res => {
      return res;
    });
  },
  getPostComments: async (post_id, cursor = null) => {
    return ajax({
      method: 'get',
      url: apiRoutes.ListComments(post_id, cursor),
      headers: jsonConfig,
    }).then(res => {
      return res.data['result'];
    });
  },
  addPostComment: async (post_id, content) => {
    const payload = {
      content: content
    };
    return ajax({
      method: 'post',
      url: apiRoutes.AddComment(post_id),
      data: payload
    }).then(res => {
      return res.data['result'];
    });
  }
};
