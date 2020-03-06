import React, {Component} from 'react';
import {BrowserRouter as Router, Link, Route} from 'react-router-dom';
import Login from './pages/Login';
import Register from './pages/Register';
import Home from './pages/Home';

const routes = [
  {
    path: '/',
    label: 'Home',
    component: Home
  },
  {
    path: '/login/',
    label: 'Login',
    component: Login
  },
  {
    path: '/register/',
    label: 'Register',
    component: Register
  }
];

class App extends Component {
  render() {
    return (
      <div className="container">
        {routes.map((route, index) => {
          return <Route path to={route.path} component={route.component}/>
        })}>
      </div>
    );
  }
}

export default App;
