const loginAction = (payload) => {
  return {
    type: "login",
    payload
  }
};
const logoutAction = (payload = {}) => {
  return {
    type: "logout",
    payload
  }
};

export {
  loginAction,
  logoutAction
};