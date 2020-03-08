export default class apiRoutes {
  //Authentication
  static Register() {
     return 'auth/login';
  }
  static Login() {
     return 'auth/login';
  }
  static refreshToken() {
     return 'auth/token/refresh';
  }
}
