import React from "react";
import {Link} from "react-router-dom";
import {connect} from "react-redux";
import Avatar from "components/common/Image";
import placeholderImage from "images/avatars/placeholder.png"

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

class UserActions extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      visible: false,
    };

    this.toggleUserActions = this.toggleUserActions.bind(this);
  }

  toggleUserActions() {
    this.setState({
      visible: !this.state.visible
    });
  }

  render() {
    if (this.props.userState.logged_in) {
      return (
        <NavItem tag={Dropdown} caret toggle={this.toggleUserActions}>
          <DropdownToggle caret tag={NavLink} className="text-nowrap px-3">
            <Avatar image_uuid={this.props.userState.userData.avatar_uuid} fallback={placeholderImage}/>
            <span className="d-none d-md-inline-block">{this.props.userState.userData.username}</span>
          </DropdownToggle>
          <Collapse tag={DropdownMenu} right small open={this.state.visible}>
            <DropdownItem tag={Link} to={"/profile/" + this.props.userState.userData.username}>
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
          <Button tag={Link} to='/login' theme="accent">Login</Button>
          <Button tag={Link} to='/register' theme="light">Register</Button>
        </ButtonGroup>
      )
    }
  }
}

const mapStateToProps = state => ({
  ...state
});

export default connect(mapStateToProps)(UserActions);