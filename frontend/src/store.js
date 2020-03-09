import { createStore } from "redux";
import rootReducer from "./reducers/rootReducer";


function configureStore(state) {
  return createStore(rootReducer, state);
}
export default configureStore;