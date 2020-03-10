/* eslint jsx-a11y/anchor-is-valid: 0 */

import React from "react";
import {userService} from "../../services/userService";
import {logoutAction} from "./../../actions/userAction";
import {connect} from "react-redux";
import {Redirect} from "react-router-dom";

class Logout extends React.Component {
  render() {
      this.props.logoutAction(null);
      userService.logout();

      return (
        <Redirect to="/" />
      )
  }
}


const mapStateToProps = state => ({
  ...state
});
const mapDispatchToProps = dispatch => ({
  logoutAction: (payload) => dispatch(logoutAction(payload)),
});
export default connect(mapStateToProps, mapDispatchToProps)(Logout);