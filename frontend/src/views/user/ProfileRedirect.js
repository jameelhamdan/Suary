import React from "react";
import {connect} from "react-redux";
import {Redirect} from "react-router-dom"


class UserProfileRedirect extends React.Component {

  render() {
    if(this.props.userState.logged_in){
      const new_url = `/profile/${this.props.userState.userData.username}`;
      this.props.history.push(new_url);
      return (<Redirect to={new_url}/>)
    } else {
      return null;
    }
  }
}

const mapStateToProps = state => ({
  ...state
});

export default connect(mapStateToProps)(UserProfileRedirect);
