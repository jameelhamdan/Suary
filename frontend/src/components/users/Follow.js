import React from "react";
import {Button, Tooltip} from "shards-react";
import PropTypes from "prop-types";
import {userService} from "services/userService";

export default class FollowButton extends React.Component {
	constructor(props) {
		super(props);
		this.user_id = this.props.user_id;
		this.switchFollow = this.switchFollow.bind(this);

		this.state = {
			loading: false,
			is_followed: this.props.is_followed,
			follow_count: this.props.follow_count
		}
	}

	switchFollow() {
		if (this.state.loading) return;
		let service = this.state.is_followed ? userService.unfollowUser : userService.followUser;
		this.setState((state) => {
			state.loading = true;
			return state;
		});

		service(this.user_id).then((result) => {
			const new_is_followed = result['state'];
			this.setState((state) => {
				state.loading = false;
				state.is_followed = new_is_followed;
				state.follow_count += new_is_followed ? 1 : -1;
				return state;
			});
		}).catch(error => {
			console.error(error);
		});
	}

	render() {
		let buttonText = this.state.is_followed ? 'Unfollow' : 'Follow';
		return (
			<>
				<Button pill outline={!this.state.is_followed}
								size={this.props.size}
								className={this.props.className}
								onClick={this.switchFollow}
								onMouseEnter={() => this.tooltipToggle(true)}
        				onMouseLeave={() => this.tooltipToggle(false)}
								disabled={this.state.loading}>
					{buttonText}
				</Button>
			</>
		)
	}

	static propTypes = {
		user_id: PropTypes.string.isRequired,
		follow_count: PropTypes.number.isRequired,
		is_followed: PropTypes.bool.isRequired,
	};
}