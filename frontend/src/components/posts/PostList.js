import React from 'react'
import PropTypes from "prop-types";
import InfiniteScroll from 'react-infinite-scroller';
import Post from "components/posts/Post"
import Loading from "components/common/Loading"
import {CardText} from "shards-react"


export default class PostList extends React.Component {
  constructor(props) {
    super(props);
    this.emptyMessage = this.props.emptyMessage;
    this.loadMoreFunc = this.props.loadMoreFunc;
    this.enableComments = this.props.enableComments;
    this.enableFollowButton = this.props.enableFollowButton;
    this.state = {
      list: [],
      cursor: null,
    };
  }

  componentDidMount() {
    this.loadMore(0);
  }

  loadMore = (page) => {
    this.loadMoreFunc(this.state.cursor).then((data) => {
      this.setState(state => ({
        list: [...state.list, ...data.list],
        cursor: data.next
      }))
    }).catch(error => {
      this.setState({error})
    });
  };

  render() {
    const EmptyMessage = <CardText>{this.emptyMessage}</CardText>;
    if (this.state.list.length === 0) {
      return EmptyMessage;
    }

    return (
      <div>
        <InfiniteScroll
          initialLoad={false}
          loadMore={this.loadMore.bind(this)}
          hasMore={!!this.state.cursor}
          loader={null}>
          {this.state.list.map((item, index) => (
            <Post key={index} postDetails={item} enableComments={this.enableComments}
                  enableFollowButton={this.enableFollowButton}/>
          ))}
        </InfiniteScroll>
      </div>
    )
  }

  static propTypes = {
    loadMoreFunc: PropTypes.func.isRequired,
    emptyMessage: PropTypes.string,
    enableFollowButton: PropTypes.bool,
    enableComments: PropTypes.bool,
  };

  static defaultProps = {
    emptyMessage: 'Nothing has been posted anything yet :(',
    loadMoreFunc: null,
    enableFollowButton: false,
    enableComments: false,
  }
}
