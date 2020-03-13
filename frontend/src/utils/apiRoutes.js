class staticRoutes {
  static Media(media_uuid) {
    return `/media/${media_uuid}.webm`;
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

  static userUpdateAvatar(user_id) {
    return `users/avatar/${user_id}`;
  }

  // Post Routes
  static userPostsList(username, cursor=null){
    if(cursor !== null){
      return `main/user/${username}/posts?cursor=${cursor}`;
    }
    return `main/user/${username}/posts`
  }
}

module.exports = {
  staticRoutes: staticRoutes,
  apiRoutes: apiRoutes,
};
