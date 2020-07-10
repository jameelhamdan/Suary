// import React from "react";
// import {NavLink} from "shards-react";
// import PropTypes from "prop-types";
//
// export default class LikeButton extends React.Component {
//   constructor(props) {
//     super(props);
//     this.post_id = this.props.post_id;
//     this.likes_count = this.props.likes_count;
//
//     this.state = {
//       loading: false,
//       is_liked: this.props.is_liked,
//     }
//   }
//
//   switchLike() {
//     console.log('CLICKED LIKE BUTTON');
//   }
//
//   render() {
//     return (
//       <NavLink onClick={this.switchLike} disabled={this.state.loading}>{this.likes_count}</NavLink>
//     )
//   }
//
//   static propTypes = {
//     post_id: PropTypes.string.isRequired,
//     likes_count: PropTypes.number.isRequired,
//     is_liked: PropTypes.bool.isRequired,
//   };
// }