const app = document.getElementById("app");

class staticRoutes {
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

  // Feed Routes
  static feedList(cursor = null) {
    if (cursor !== null) {
      return `feed/?cursor=${cursor}`;
    }
    return `feed/`
  }

  static searchList(query, cursor = null) {
    if (cursor !== null) {
      return `feed/search?q=${query}&cursor=${cursor}`;
    }
    return `feed/search?q=${query}`
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
