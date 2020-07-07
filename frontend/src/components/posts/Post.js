import React from "react";
import {Link} from "react-router-dom";
import {Card, CardBody, CardTitle, Nav, NavItem, NavLink} from "shards-react";
import PropTypes from "prop-types";
import Avatar, {PostMedia} from "components/common/Image"
import PostComments from "./PostComments"
import placeholderImage from "images/avatars/placeholder.png"


export default class Post extends React.Component {
  constructor(props) {
    super(props);
    this.data = this.props.postDetails;
    this.enableComments = this.props.enableComments;
  }

  render() {
    return (
      <div key={this.props.key}>
        <Card small className="mb-4">
          <CardBody>
            <CardTitle>
              <Avatar image_uuid={this.data.created_by.avatar_uuid} fallback={placeholderImage}/>
              <span className="d-none d-md-inline-block">{this.data.created_by.username}</span>
            </CardTitle>

            <p>{this.data.content}</p>
          </CardBody>

          {this.data.media_list.length > 0 &&
          <PostMedia media_uuid={this.data.media_list[0].hash} content_type={this.data.media_list[0].content_type}/>
          }
          <CardBody>
            <Nav justified>
              <NavItem>
                <NavLink tag={Link} to={'/post/' + this.data.id}>{this.data.likes_count} Likes</NavLink>
              </NavItem>
              <NavItem>
                <NavLink tag={Link} to={'/post/' + this.data.id}>{this.data.comments_count} Comments</NavLink>
              </NavItem>
            </Nav>
          </CardBody>
        </Card>
        {this.enableComments === true &&
        <Card small className="mb-4">
          <PostComments post_id={this.data.id}/>
        </Card>
        }
      </div>
    );
  }

  static propTypes = {
    /**
     * The post details object.
     */
    key: PropTypes.string,
    enableComments: PropTypes.bool,
    postDetails: PropTypes.shape({
      id: PropTypes.string.isRequired,
      is_liked: PropTypes.bool,
      content: PropTypes.string,
      media_list: PropTypes.array,
      created_by: PropTypes.shape({
        id: PropTypes.string,
        username: PropTypes.string,
        avatar_uuid: PropTypes.string,
      }),
      likes_count: PropTypes.string,
      comments_count: PropTypes.string,
    })
  };

  static defaultProps = {
    key: '1',
    enableComments: false,
    postDetails: {
      id: null,
      is_liked: false,
      content: null,
      media_list: [],
      created_by: {
        id: null,
        username: null,
        avatar_uuid: null,
      },
      likes_count: '0',
      comments_count: '0',
    }
  };
}
