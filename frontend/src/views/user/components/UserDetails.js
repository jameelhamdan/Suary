import React from "react";
import PropTypes from "prop-types";
import {
  Card,
  CardHeader,
} from "shards-react";
import {LargeAvatar} from "components/common/Image";
import FollowButton from "components/users/Follow";


const UserDetails = ({ userDetails }) => (
  <Card small className="mb-4 pt-3">
    <CardHeader className="border-bottom text-center">
      <div className="mb-3 mx-auto">
        <LargeAvatar image_uuid={userDetails.avatar_uuid} fallback={require("images/avatars/placeholder.png")} />
      </div>
      <h4 className="mb-0">{userDetails.username}</h4>
      <span className="text-muted d-block mb-2"></span>
      <FollowButton user_id={userDetails.id} follow_count={userDetails.follow_count} is_followed={userDetails.is_followed} />
    </CardHeader>
  </Card>
);

UserDetails.propTypes = {
  /**
   * The user details object.
   */
  userDetails: PropTypes.object
};

UserDetails.defaultProps = {
  id: null,
  username: null,
  avatar_uuid: null,
  follow_count: 0,
  is_followed: false
};

export default UserDetails;
