import React from "react";
import { Link } from "react-router-dom";
import { connect } from "react-redux";
import Img from 'react-image'
import {
  Dropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem,
  Collapse,
  NavItem,
  NavLink
} from "shards-react";
import {staticRoutes} from "../../../../utils/apiRoutes"

class UserActions extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      visible: false,
    };

    this.toggleUserActions = this.toggleUserActions.bind(this);
    this.get_avatar_url = this.get_avatar_url.bind(this);
  }

  toggleUserActions() {
    this.setState({
      visible: !this.state.visible
    });
  }

  get_avatar_url(){
    if(this.props.userState.userData != null && this.props.userState.userData.avatar_uuid !== null && this.props.userState.userData.avatar_uuid !== undefined && this.props.userState.userData.avatar_uuid.length > 0){
      return staticRoutes.Media(this.props.userState.userData.avatar_uuid);
    } else {
      return require("./../../../../images/avatars/1.jpg")
    }
  }

  get_username(){
    if(this.props.userState.userData != null){
      return this.props.userState.userData.username
    } else {
      return 'Login'
    }
  }

  render() {
    return (
      <NavItem tag={Dropdown} caret toggle={this.toggleUserActions}>
        <DropdownToggle caret tag={NavLink} className="text-nowrap px-3">
          <Img
            decode={false}
            className="user-avatar rounded-circle mr-2"
            src={this.get_avatar_url()}
            alt="Avatar"
          />
          <span className="d-none d-md-inline-block">{this.get_username()}</span>
        </DropdownToggle>
        <Collapse tag={DropdownMenu} right small open={this.state.visible}>
          <DropdownItem tag={Link} to="user-profile-lite">
            <i className="material-icons">&#xE7FD;</i> Profile
          </DropdownItem>
          <DropdownItem tag={Link} to="edit-user-profile">
            <i className="material-icons">&#xE8B8;</i> Edit Profile
          </DropdownItem>
          <DropdownItem tag={Link} to="file-manager-list">
            <i className="material-icons">&#xE2C7;</i> Files
          </DropdownItem>
          <DropdownItem tag={Link} to="transaction-history">
            <i className="material-icons">&#xE896;</i> Transactions
          </DropdownItem>
          <DropdownItem divider />
          <DropdownItem tag={Link} to="/" className="text-danger">
            <i className="material-icons text-danger">&#xE879;</i> Logout
          </DropdownItem>
        </Collapse>
      </NavItem>
    );
  }
}
const mapStateToProps = state => ({
  ...state
});

export default connect(mapStateToProps)(UserActions);