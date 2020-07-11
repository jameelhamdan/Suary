import React from "react";
import {Button, NavLink} from "shards-react";
import PropTypes from "prop-types";
import ArrowUpward from "@material-ui/icons/ArrowUpward";
import {postService} from "services/postService";

export default class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.post_id = this.props.post_id;
    this.switchLike = this.switchLike.bind(this);
    this.state = {
      loading: false,
      is_liked: this.props.is_liked,
      likes_count: this.props.likes_count
    }
  }

  switchLike() {
    if (this.state.loading) return;
    let service = this.state.is_liked ? postService.unlikePost: postService.likePost;
    this.setState((state) => {
      state.loading = true;
      return state;
    });

    service(this.post_id).then((result) => {
      const new_is_liked = result['state'];
      this.setState((state) => {
        state.loading = false;
        state.is_liked = new_is_liked;
        state.likes_count += new_is_liked? 1: -1;
        return state;
      });
    }).catch(error => {
      console.error(error);
    });
  }

  render() {
    //TODO: add these as css classes for like button
    let iconColor = this.state.is_liked ? '#007bff' : '#212529';

    return (
      <NavLink>
        <Button theme="transparent" className={'py-0'} onClick={this.switchLike} disabled={this.state.loading}>
          <ArrowUpward style={{ color: iconColor }}></ArrowUpward>
        </Button>
        {this.state.likes_count}
      </NavLink>
    )
  }

  static propTypes = {
    post_id: PropTypes.string.isRequired,
    likes_count: PropTypes.number.isRequired,
    is_liked: PropTypes.bool.isRequired,
  };
}