import React from "react";
import {Wrapper} from "components/common/Wrapper";
import PostList from "components/posts/PostList";
import {postService} from "services/postService";
import {CardText} from "shards-react";

export default class Search extends React.Component {
  loadPosts = (page, cursor) => {
    return postService.searchPosts(this.props.search, cursor).then((data) => {
      return data;
    });
  };

  render() {
    return (
      <Wrapper>
        <PostList loadMoreFunc={this.loadPosts}>
          <CardText>We came up empty...</CardText>
        </PostList>
      </Wrapper>
    )
  }
}
