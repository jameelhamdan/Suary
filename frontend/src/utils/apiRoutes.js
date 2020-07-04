class staticRoutes {
  static Media(media_uuid) {
    return `/media/${media_uuid}`;
  }
}

class apiRoutes {

  //Authentication
  static Root() {
    return document.getElementById("app").getAttribute("api-root-url");
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

  static postComment() {
    return `main/comment`;
  }
}

module.exports = {
  staticRoutes: staticRoutes,
  apiRoutes: apiRoutes,
};
