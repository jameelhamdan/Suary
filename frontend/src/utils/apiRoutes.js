class staticRoutes {
  static Media(media_uuid) {
    return `media/${media_uuid}.webm`
  }
}

class apiRoutes {

  //Authentication
  static Root() {
    return document.getElementById("app").getAttribute('api-root-url');
  }

  static Register() {
    return 'auth/register';
  }

  static Login() {
    return 'auth/login';
  }

  static refreshToken() {
    return 'auth/token/refresh';
  }

}

module.exports = {
  staticRoutes: staticRoutes,
  apiRoutes: apiRoutes,
};
