import React from "react";
import { Link } from "react-router-dom";
import {
  Dropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem,
  Collapse,
  NavItem,
  NavLink
} from "shards-react";
import UserStorage from "../../../../utils/storage"
import {staticRoutes} from "../../../../utils/apiRoutes"

export default class UserActions extends React.Component {
  constructor(props) {
    super(props);
    console.log(props);
    this.state = {
      visible: false,
      logged_in: UserStorage.isAuthenticated(),
      user_data: UserStorage.getUserData()
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
    const avatar_uuid = this.state.user_data.avatar_uuid;
    if(this.state.logged_in && avatar_uuid !== null && avatar_uuid !== undefined && avatar_uuid.length > 0){
      return staticRoutes.Media(avatar_uuid);
    } else {
      return require("./../../../../images/avatars/1.jpg")
    }
  }

  get_username(){
    if(this.state.logged_in){
      return this.state.user_data.username
    } else {
      return 'Login'
    }
  }

  render() {
    return (
      <NavItem tag={Dropdown} caret toggle={this.toggleUserActions}>
        <DropdownToggle caret tag={NavLink} className="text-nowrap px-3">
          <img
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
