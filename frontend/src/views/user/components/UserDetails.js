import React from "react";
import PropTypes from "prop-types";
import {
	Card,
	CardHeader
} from "shards-react";
import {LargeAvatar} from "components/common/Image";
import placeholderImage from "images/avatars/placeholder.png";
import FollowButton from "components/users/Follow";


export default class UserDetails extends React.Component {
	constructor(props) {
		super(props);
		this.data = this.props.data;
	}

	render() {
		let followerText = `${this.data.follow_count} Followers`;
		return (
			<Card small className="mb-4 pt-3">
				<CardHeader className="border-bottom text-center">
					<div className="mb-3 mx-auto">
						<LargeAvatar image_url={this.data.avatar_url} fallback={placeholderImage}/>
					</div>
					<h4 className="mb-0">{this.data.username}</h4>
					<span className="text-muted d-block mb-2">{followerText}</span>
					<FollowButton size="mb-2" user_id={this.data.id} follow_count={this.data.follow_count} is_followed={this.data.is_followed}/>
				</CardHeader>
			</Card>
		)
	}

	static propTypes = {
		userDetails: PropTypes.object
	};

	static defaultProps = {
		id: null,
		username: null,
		avatar_url: null,
		follow_count: 0,
		is_followed: false
	};
};
