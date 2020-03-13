import React from "react";
import PropTypes from "prop-types";
import {
  Card,
  CardHeader,
  Button,
} from "shards-react";
import {LargeAvatar} from "components/common/Image";


const UserDetails = ({ userDetails }) => (
  <Card small className="mb-4 pt-3">
    <CardHeader className="border-bottom text-center">
      <div className="mb-3 mx-auto">
        <LargeAvatar image_uuid={userDetails.avatar_uuid} fallback={require("images/avatars/placeholder.png")} />
      </div>
      <h4 className="mb-0">{userDetails.username}</h4>
      <span className="text-muted d-block mb-2"></span>
      <Button pill outline size="sm" className="mb-2">
        <i className="material-icons mr-1">person_add</i> Follow
      </Button>
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
  username: null,
  avatar_uuid: null,
};

export default UserDetails;
