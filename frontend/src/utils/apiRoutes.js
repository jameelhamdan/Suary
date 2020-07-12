const app = document.getElementById("app");

class staticRoutes {
  static Media(media_uuid) {
    //TODO: find a better way to do this
    let root_url = app.getAttribute("api-root-url");
    let arr = root_url.split("/");
    root_url = arr[0] + "//" + arr[2];
    return `${root_url}/media/${media_uuid}`;
  }
}

class apiRoutes {

  //Authentication
  static Root() {
    return app.getAttribute("api-root-url");
  }

  static Register() {
    return "auth/register";
  }

  static Login() {
    return "auth/login";
  }

  static refreshToken() {
    return "auth/token/refresh";
  }

  // User Routes
  static userDetail(username) {
    return `users/detail/${username}`;
  }

  static userFollow() {
    return `users/follow`;
  }

  static userUpdateAvatar() {
    return `users/avatar`;
  }

  // Post Routes
  static userPostsList(username, cursor = null) {
    if (cursor !== null) {
      return `main/user/${username}/posts?cursor=${cursor}`;
    }
    return `main/user/${username}/posts`
  }

  static getPost(id) {
    return `main/post/${id}`
  }

  static addPost() {
    return `main/post`;
  }

  static listComments(post_id, cursor = null) {
      if (cursor !== null) {
      return `main/post/${post_id}/comments?cursor=${cursor}`;
    }
    return `main/post/${post_id}/comments`;
  }

  static addComment(post_id) {
    return `main/post/${post_id}/comments/add`;
  }

  static likePost(post_id) {
    return `main/post/${post_id}/likes/add`;
  }
}

module.exports = {
  staticRoutes: staticRoutes,
  apiRoutes: apiRoutes,
};
