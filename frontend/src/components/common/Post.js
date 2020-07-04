import React from "react";
import Avatar, {PostMedia} from "components/common/Image"
import {Card, CardBody, CardTitle, DropdownItem, Modal, Nav, NavItem, NavLink} from "shards-react";
import PropTypes from "prop-types";
import placeholderImage from "images/avatars/placeholder.png"
import {Link} from "react-router-dom";

export default class Post extends React.Component {
  constructor(props) {
    super(props);
    this.data = this.props.postDetails;
  }

  render() {
    return (
      <Card key={this.data.id} small className="mb-4 pt-3">
        <CardBody>
          <CardTitle>
            <Avatar image_uuid={this.data.created_by.avatar_uuid} fallback={placeholderImage}/>
            <span className="d-none d-md-inline-block">{this.data.created_by.username}</span>
          </CardTitle>

          <p>{this.data.content}</p>
        </CardBody>

        {this.data.media_list.length > 0 &&
        <PostMedia onClick={this.toggle} media_uuid={this.data.media_list[0].hash} content_type={this.data.media_list[0].content_type}/>
        }
        <CardBody>
          <Nav justified>
            <NavItem>
              <NavLink tag={Link} to={'/post/' + this.data.id}>{this.data.likes_count} Likes</NavLink>
            </NavItem>
            <NavItem>
              <NavLink tag={Link} to={'/post/' + this.data.id} onClick={this.toggle}>{this.data.comments_count} Comments</NavLink>
            </NavItem>
          </Nav>
        </CardBody>
      </Card>
    );
  }

  static propTypes = {
    /**
     * The post details object.
     */
    key: PropTypes.string,
    postDetails: PropTypes.shape({
      id: PropTypes.string.isRequired,
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
    postDetails: {
      id: null,
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
