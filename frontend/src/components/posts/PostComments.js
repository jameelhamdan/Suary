import React from "react";
import {CardText, ListGroup} from "shards-react";
import PropTypes from "prop-types";
import {postService} from "services/postService";
import Comment from "./Comment";
import AddComment from "./AddComment";
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

  addCommentHandler = (result) => {
    // TODO: fix this to show new comment first
    this.setState({
      list: [],
      cursor: null
    });

    this.loadMore(0);
  };

  render() {
    if (this.state.isLoading || this.state.error) return null;

    return (
      <ListGroup>
        {this.state.list.length > 0 &&
        <InfiniteScroll
          initialLoad={false}
          loadMore={this.loadMore.bind(this)}
          hasMore={!!this.state.cursor}
          loader={null}>
          {this.state.list.map((item, index) => (
            <Comment key={index} commentDetails={item}/>
          ))}
        </InfiniteScroll>
        }
        <AddComment post_id={this.id} handler={this.addCommentHandler}/>
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
