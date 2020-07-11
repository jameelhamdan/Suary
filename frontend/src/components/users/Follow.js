import React from "react";
import {Button, NavLink} from "shards-react";
import PropTypes from "prop-types";
import {userService} from "services/userService";

export default class FollowButton extends React.Component {
  constructor(props) {
    super(props);
    this.user_id = this.props.user_id;
    this.switchFollow = this.switchFollow.bind(this);
    this.state = {
      loading: false,
      is_followed: this.props.is_followed,
      follow_count: this.props.follow_count
    }
  }

  switchFollow() {
    if (this.state.loading) return;
    let service = this.state.is_followed ? userService.unfollowUser : userService.followUser;
    this.setState((state) => {
      state.loading = true;
      return state;
    });

    service(this.user_id).then((result) => {
      const new_is_liked = result['state'];
      this.setState((state) => {
        state.loading = false;
        state.is_followed = new_is_liked;
        state.follow_count += new_is_liked ? 1 : -1;
        return state;
      });
    }).catch(error => {
      console.error(error);
    });
  }

  render() {
    //TODO: add these as css classes for like button
    let buttonProps = this.state.is_followed ? []: ['outline'];
    let buttonText = this.state.is_followed ? 'Unfollow': 'Follow';

    return (
      <NavLink>
        <Button pill {...buttonProps} size="sm" className="mb-2" onClick={this.switchFollow}  disabled={this.state.loading}>
          {buttonText}
        </Button>
      </NavLink>
    )
  }

  static propTypes = {
    user_id: PropTypes.string.isRequired,
    follow_count: PropTypes.number.isRequired,
    is_followed: PropTypes.bool.isRequired,
  };
}