import React from "react";
import {Link} from "react-router-dom";
import {connect} from "react-redux";
import Img from "react-image";
import {
  Dropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem,
  Collapse,
  NavItem,
  NavLink,
  Button,
  ButtonGroup,
} from "shards-react";
import {staticRoutes} from "utils/apiRoutes"

class UserActions extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      visible: false,
      logged_in: this.props.userState.userData != null
    };

    this.toggleUserActions = this.toggleUserActions.bind(this);
    this.get_avatar_url = this.get_avatar_url.bind(this);
  }

  toggleUserActions() {
    this.setState({
      visible: !this.state.visible
    });
  }

  get_avatar_url() {
    let urls = [];
    if (this.state.logged_in && this.props.userState.userData.avatar_uuid !== null && this.props.userState.userData.avatar_uuid !== undefined && this.props.userState.userData.avatar_uuid.length > 0) {
      urls.push(staticRoutes.Media(this.props.userState.userData.avatar_uuid));
    }

    urls.push(require("./../../../../images/avatars/placeholder.png"));
    return urls
  }

  get_username() {
    if (this.state.logged_in) {
      return this.props.userState.userData.username
    } else {
      return 'Login'
    }
  }

  render() {
    if (this.state.logged_in) {
      return (
        <NavItem tag={Dropdown} caret toggle={this.toggleUserActions}>
          <DropdownToggle caret tag={NavLink} className="text-nowrap px-3">
            <Img
              decode={false}
              className="user-avatar rounded-circle mr-2"
              src={this.get_avatar_url()}
              alt="Avatar"
              loader={<span className="user-avatar d-inline-block rounded-circle mr-2 w-2-5 h-2-5 vertical-align-middle"></span>}
            />
            <span className="d-none d-md-inline-block">{this.get_username()}</span>
          </DropdownToggle>
          <Collapse tag={DropdownMenu} right small open={this.state.visible}>
            <DropdownItem tag={Link} to="user-profile">
              <i className="material-icons">&#xE7FD;</i> Profile
            </DropdownItem>
            <DropdownItem divider/>
            <DropdownItem tag={Link} to="/logout" className="text-danger">
              <i className="material-icons text-danger">&#xE879;</i> Logout
            </DropdownItem>
          </Collapse>
        </NavItem>
      );
    } else {
      return (
        <ButtonGroup size="sm" className="p-3">
          <Button tag={Link} to='login' theme="accent">Login</Button>
          <Button tag={Link} to='register' theme="light">Register</Button>
        </ButtonGroup>
      )
    }
  }
}

const mapStateToProps = state => ({
  ...state
});

export default connect(mapStateToProps)(UserActions);