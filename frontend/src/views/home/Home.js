import React from "react";
import {Wrapper} from "components/common/Wrapper";
import {connect} from "react-redux";
import AddPostWidget from "components/posts/AddPost";
import PostList from "components/posts/PostList";
import {postService} from "services/postService";

class Home extends React.Component {
	loadPosts = (page, cursor) => {
		return postService.getFeedPosts(cursor).then((data) => {
			return data;
		});
	};

	render() {
		return (
			<Wrapper>
				<AddPostWidget history={this.props.history}/>
				<PostList loadMoreFunc={this.loadPosts}/>
			</Wrapper>
		)
	}
}

const mapStateToProps = state => ({
	...state
});

export default connect(mapStateToProps)(Home)