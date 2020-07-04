import React from "react";
import {CardText, ListGroup} from "shards-react";
import PropTypes from "prop-types";
import {postService} from "services/postService";
import Comment from "./Comment";
import InfiniteScroll from "react-infinite-scroller";

export default class Post extends React.Component {
  constructor(props) {
    super(props);
    this.id = this.props.post_id;
    this.state = {
      list: [],
      cursor: null,
    };
  }

  componentDidMount() {
    this.loadMore(0);
  }

  loadMore = (page) => {
    postService.getPostComments(this.id, this.state.cursor).then((data) => {
      this.setState(state => ({
        list: [...state.list, ...data.list],
        cursor: data.next
      }))
    }).catch(error => {
      this.setState({error})
    });
  };

  render() {
    if (this.state.isLoading || this.state.error) return null;
    const EmptyMessage = <CardText>This post doesn't have any comments yet :(</CardText>;

    if(this.state.list.length === 0){
      return EmptyMessage;
    }

    return (
      <ListGroup>
        <InfiniteScroll
          initialLoad={false}
          loadMore={this.loadMore.bind(this)}
          hasMore={!!this.state.cursor}
          loader={null}>
          {this.state.list.map((item, index) => (
          <Comment key={index} commentDetails={item}/>
          ))}
        </InfiniteScroll>
      </ListGroup>
    );
  }

  static propTypes = {
    /**
     * The post details object.
     */
    post_id: PropTypes.string,
  };
}
