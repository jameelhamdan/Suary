import React from "react";
import {CardText, Row, Col, ListGroupItem} from "shards-react";
import PropTypes from "prop-types";
import Avatar, {CommentMedia} from "components/common/Image"
import placeholderImage from "images/avatars/placeholder.png"
import {Link} from "react-router-dom";
import TimeAgo from "react-timeago";


export default class Post extends React.Component {
  constructor(props) {
    super(props);
    this.data = this.props.commentDetails;
  }

  render() {
    return (
      <ListGroupItem key={this.data.id}>
        <Row>
          <Col lg={12}>
            <Avatar image_uuid={this.data.created_by.avatar_uuid} fallback={placeholderImage}/>
            <Link tag={Link} to={"/profile/" + this.data.created_by.username} className="d-none d-md-inline-block">{this.data.created_by.username}</Link>
            <TimeAgo component={CardText} className={"float-right"} date={this.data.created_on}/>
          </Col>
          <Col lg={12}>{this.data.content}</Col>
          {this.data.media &&
          <Col sm={6} md={4} lg={3}>
            <CommentMedia media_uuid={this.data.media.hash} content_type={this.data.media.content_type}/>
          </Col>
          }
        </Row>
      </ListGroupItem>
    );
  }

  static propTypes = {
    /**
     * The post details object.
     */
    key: PropTypes.string,
    commentDetails: PropTypes.shape({
      id: PropTypes.string.isRequired,
      post_id: PropTypes.string,
      content: PropTypes.string,
      media: PropTypes.shape({
        content_type: PropTypes.string,
        hash: PropTypes.string,
      }),
      created_on: PropTypes.string,
      created_by: PropTypes.shape({
        id: PropTypes.string,
        username: PropTypes.string,
        avatar_uuid: PropTypes.string,
      })
    })
  };

  static defaultProps = {
    key: '1',
    commentDetails: {
      id: null,
      post_id: null,
      content: null,
      media: null,
      created_by: {
        id: null,
        username: null,
        avatar_uuid: null,
      }
    }
  };
}
