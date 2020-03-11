import UserStorage from "utils/storage";

const initialState = {
  userData: UserStorage.isAuthenticated() ? UserStorage.getUserData() : null
};

export default (state = initialState , action) => {
  switch (action.type) {
    case "login":
      return {
        ...state,
        userData: action.payload
      };
    case "logout":
      return {
        ...state,
        userData: action.payload
      };
    default:
      return state;
  }
};