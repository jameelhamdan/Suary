import React from "react";
import {
  //Router,
  Route,
  Switch
} from "react-router";
import {BrowserRouter as Router} from "react-router-dom";
import routes from "routes";
import withTracker from "withTracker";
import {connect} from "react-redux";
import "bootstrap/dist/css/bootstrap.min.css";
import "styles/theme.css";
import NotFound from "components/common/pages/NotFound"


class App extends React.Component {
  constructor(props) {
    super(props);
    this.get_routes = this.get_routes.bind(this);
  }

  get_routes() {
    let route_list = [];
    for (let i = 0; i < routes.length; i++) {
      const route = routes[i];
      if (!this.props.userState.logged_in && route.logged_in_only) continue;
      route_list.push(route);
    }
    return route_list;
  }

  render() {
    return (
      <Router>
        <Switch>
          {this.get_routes().map((route, index) => {
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
    )
  }
}

const mapStateToProps = state => ({
  ...state
});
export default connect(mapStateToProps)(App);
