import React from "react";
import {Col, Row, Fade} from "shards-react";
import {BaseWrapper} from "components/common/Wrapper";
import {userService} from "services/userService";
import NotFound from "components/common/pages/NotFound"
import UserDetails from './components/UserDetails';
import PostList from "components/posts/PostList";
import {connect} from "react-redux";
import {postService} from "services/postService";


class UserDetail extends React.Component {
  constructor(props) {
    super(props);
    this.username = this.props.match.params.username;
    this.state = {
      data: {},
      error: null,
      isLoading: true
    };

  }

  componentDidMount() {
    userService.getUser(this.username).then((data) => {
      this.setState({data, isLoading: false});
    }).catch((error) => {
      this.setState({error, isLoading: false});
    });
  }

  loadPosts = (page, cursor) => {
    return postService.getUserPosts(this.username, cursor).then((data) => {
      return data;
    });
  };

  render() {
    if (this.state.isLoading) return null;
    if (this.state.error) return (<NotFound/>);

    return (
      <BaseWrapper>
        <Row className="mt-5">
          <Col lg="3" md="4">
            <Fade in={!this.state.isLoading}>
              <UserDetails data={this.state.data}/>
            </Fade>
          </Col>
          <Col lg="9" md="8">
            <PostList loadMoreFunc={this.loadPosts}/>
          </Col>
        </Row>
      </BaseWrapper>
    );
  }
}

const mapStateToProps = state => ({
  ...state
});

export default connect(mapStateToProps)(UserDetail);
