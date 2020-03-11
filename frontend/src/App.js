import React from "react";
import {
  Router,
  Route,
} from "react-router-dom";
import routes from "routes";
import history from "utils/history";
import withTracker from "withTracker";
import {Provider} from "react-redux";
import configureStore from "store";
import "bootstrap/dist/css/bootstrap.min.css";
import "styles/theme.css";

export default () => (
  <Provider store={configureStore()}>
    <Router history={history}>
      <div>
        {routes.map((route, index) => {
          return (
            <Route
              key={index}
              path={route.path}
              exact={route.exact}
              component={withTracker(props => {
                return (
                  <route.layout {...props}>
                    <route.component {...props} />
                  </route.layout>
                );
              })}
            />
          );
        })}
        <Route path="*" target='_self'>
          <NoMatch />
        </Route>
      </div>
    </Router>
  </Provider>
);


function NoMatch() {
  return (
    <div>
      <h3>
        Page not found 404
      </h3>
    </div>
  );
}