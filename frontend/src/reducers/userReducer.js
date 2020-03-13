import UserStorage from "utils/storage";

const initialState = {
  logged_in: UserStorage.isAuthenticated(),
  userData: UserStorage.isAuthenticated() ? UserStorage.getUserData() : null
};

export default (state = initialState , action) => {
  switch (action.type) {
    case "login":
      return {
        ...state,
        logged_in: true,
        userData: action.payload
      };
    case "logout":
      return {
        ...state,
        logged_in: false,
        userData: action.payload
      };
    default:
      return state;
  }
};