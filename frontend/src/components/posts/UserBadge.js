import React from "react";
import Avatar from "components/common/Image";
import placeholderImage from "images/avatars/placeholder.png";
import FollowButton from "components/users/Follow";
import PropTypes from "prop-types";
import TimeAgo from "react-timeago";
import {CardText, Col, Row} from "shards-react";


export default class UserBadge extends React.Component {
	constructor(props) {
		super(props);
		this.data = this.props.data;
		this.enableFollowButton = this.props.enableFollowButton;
		this.postCreatedOn = this.props.postCreatedOn;
	}

	render() {
		return (
			<Row>
				<Col lg={9}>
					<Avatar className="d-inline-block" image_uuid={this.data.avatar_uuid} fallback={placeholderImage}/>
					<span className="d-inline-block">{this.data.username}</span>
					{this.enableFollowButton &&
						<FollowButton className="ml-2 d-inline-block" size="sm" user_id={this.data.id} follow_count={this.data.follow_count} is_followed={this.data.is_followed}/>
					}
				</Col>
				<Col lg={3}>
					<TimeAgo component={CardText} className={"float-right mb-0"} date={this.postCreatedOn}/>
				</Col>
			</Row>
		)
	};

	static propTypes = {
		data: PropTypes.shape({
			id: PropTypes.string,
			username: PropTypes.string,
			avatar_uuid: PropTypes.string,
			follow_count: PropTypes.number,
			is_followed: PropTypes.bool
		}).isRequired,
		postCreatedOn: PropTypes.string,
		showFollowButton: PropTypes.bool
	};

	static defaultProps = {
		data: {},
		postCreatedOn: null,
		showFollowButton: true
	}
}
