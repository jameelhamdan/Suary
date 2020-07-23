import Img from "react-image";
import ReactPlayer from "react-player"
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

  get_image_url() {
    const url = this.props.image_url;
    const fallback = this.props.fallback;
    return url ? url : (this.props.fallback ? fallback : null);
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

  static propTypes = {
    image_url: PropTypes.string,
    fallback: PropTypes.string,
    placeholder: PropTypes.node,
  }
}

export class LargeAvatar extends Avatar {
  avatarPlaceholder() {
    if (this.props.placeholder != null) {
      return this.props.placeholder
    } else {
      return <span className="rounded-circle vertical-align-middle" style={{width: 110}}></span>;
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
        style={{width: 110}}
        loader={defaultComponent}
        unloader={defaultComponent}
      />
    )
  }
}

export class PostMedia extends React.Component {
  imagePlaceholder() {
    if (this.props.placeholder != null) {
      return this.props.placeholder
    } else {
      return null;
    }
  }

  get_media_url() {
    return this.props.media_url;
  }

  get_content_type() {
    const content_type = this.props.content_type;
    if (content_type != null) {
      return this.props.content_type
    } else {
      return 'image/webp';
    }
  }

  render() {
    const defaultComponent = this.imagePlaceholder();
    const content_type = this.get_content_type();

    if (content_type.startsWith('video')) {
      return (
        <ReactPlayer
          className="card-img-bottom card-video-bottom"
          url={this.get_media_url()}
          width="100%"
          height="100%"
          controls
        />
      )
    } else {
      return (
        <Img
          decode={false}
          className="card-img-bottom"
          src={this.get_media_url()}
          alt={this.props.alt || "post image"}
          loader={defaultComponent}
          unloader={defaultComponent}
        />
      )
    }
  }

  static propTypes = {
    media_url: PropTypes.string.isRequired,
    content_type: PropTypes.string,
    placeholder: PropTypes.node,
  };
}


export class CommentMedia extends React.Component {
  get_media_url() {
    return this.props.media_url;
  }

  get_content_type() {
    const content_type = this.props.content_type;
    if (content_type != null) {
      return this.props.content_type
    } else {
      return 'image/webp';
    }
  }

  render() {
    const defaultComponent = null;
    const content_type = this.get_content_type();

    if (content_type.startsWith('video')) {
      return (
        <ReactPlayer
          className="card-img-bottom card-video-bottom"
          url={this.get_media_url()}
          width="100%"
          height="100%"
          controls
        />
      )
    } else {
      return (
        <Img
          decode={false}
          className="img-responsive"
          src={this.get_media_url()}
          alt={this.props.alt || "comment image"}
          loader={defaultComponent}
          unloader={defaultComponent}
        />
      )
    }

  }
}
