import Img from "react-image";
import React from "react";
import {staticRoutes} from "utils/apiRoutes"
import PropTypes from "prop-types";


export default class Avatar extends React.Component {
  avatarPlaceholder() {
    if (this.props.placeholder != null) {
      return this.props.placeholder
    } else {
      return <span className="user-avatar d-inline-block rounded-circle mr-2 w-2-5 h-2-5 vertical-align-middle"></span>;
    }
  }

  get_image_url(){
    const image_uuid = this.props.image_uuid;
    const fallback = this.props.fallback;
    if(image_uuid !== undefined && image_uuid !== null){
      return staticRoutes.Media(image_uuid);
    } else if (fallback !== undefined && fallback !== null){
      return fallback
    } else {
      return null;
    }
  }

  render() {
    const defaultComponent = this.avatarPlaceholder();
    return (
      <Img
        decode={false}
        className="user-avatar rounded-circle mr-2 w-2-5"
        src={this.get_image_url()}
        alt="Avatar"
        loader={defaultComponent}
        unloader={defaultComponent}
      />
    )
  }
}

export class LargeAvatar extends Avatar {
  avatarPlaceholder() {
    if (this.props.placeholder != null) {
      return this.props.placeholder
    } else {
      return <span className="rounded-circle vertical-align-middle" style={{width:110}}></span>;
    }
  }

  render() {
    const defaultComponent = this.avatarPlaceholder();
    return (
      <Img
        decode={false}
        className="rounded-circle"
        src={this.get_image_url()}
        alt={this.props.alt || "Large Avatar"}
        style={{width:110}}
        loader={defaultComponent}
        unloader={defaultComponent}
      />
    )
  }
}

export class PostImage extends React.Component  {
  avatarPlaceholder() {
    if (this.props.placeholder != null) {
      return this.props.placeholder
    } else {
      return null;
    }
  }

  get_image_url(){
    const image_uuid = this.props.image_uuid;
    if(image_uuid !== undefined && image_uuid !== null){
      return staticRoutes.Media(image_uuid);
    } else {
      return null;
    }
  }

  render() {
    const defaultComponent = this.avatarPlaceholder();
    return (
      <Img
        decode={false}
        className="card-img-bottom"
        src={this.get_image_url()}
        alt={this.props.alt || "post image"}
        loader={defaultComponent}
        unloader={defaultComponent}
      />
    )
  }
}

Avatar.propTypes = {
  image_uuid: PropTypes.string,
  fallback: PropTypes.string,
  placeholder: PropTypes.node,
};

PostImage.propTypes = {
  image_uuid: PropTypes.string.isRequired,
  placeholder: PropTypes.node,
};

