import React from "react";
import {
  Router,
  Route,
  Switch
} from "react-router-dom";
import routes from "routes";
import history from "utils/history";
import withTracker from "withTracker";
import {Provider} from "react-redux";
import configureStore from "store";
import "bootstrap/dist/css/bootstrap.min.css";
import "styles/theme.css";
import NotFound from "components/common/pages/NotFound"


export default () => (
  <Provider store={configureStore()}>
    <Router history={history}>
      <Switch>
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
        <Route
          render={({staticContext}) => {
            if (staticContext) {
              staticContext.statusCode = 404
            }
            return <NotFound/>
          }}
        />
      </Switch>
    </Router>
  </Provider>
);
