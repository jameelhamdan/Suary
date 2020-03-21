import React from 'react'
import PropTypes from "prop-types";
import {postService} from "services/postService";
import InfiniteScroll from 'react-infinite-scroller';
import Post from "components/common/Post"
import Loading from "components/common/Loading"
import {CardText} from "shards-react"


export default class UserPosts extends React.Component {
  constructor(props) {
    super(props);
    this.username = this.props.username;
    this.state = {
      list: [],
      cursor: null,
    };
  }
  componentDidMount() {
    this.loadMore(0);
  }

  loadMore = (page) => {
    postService.getUserPosts(this.username, this.state.cursor).then((data) => {
      this.setState(state => ({
        list: [...state.list, ...data.list],
        cursor: data.next
      }))
    }).catch(error => {
      this.setState({error})
    });
  };

  render() {
    const EmptyMessage = <CardText>This user hasn't posted anything yet :(</CardText>;
    if(this.state.list.length === 0){
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
            <Post key={index} postDetails={item}/>
          ))}
        </InfiniteScroll>
      </div>
    )
  }

  static
  propTypes = {
    username: PropTypes.string.isRequired
  };

}
