import React from "react";
import {Col, Row, Fade} from "shards-react";
import {BaseWrapper} from "components/common/Wrapper";
import {postService} from "services/postService";
import NotFound from "components/common/pages/NotFound"
import Post from 'components/common/Post';
import {connect} from "react-redux";


class UserDetail extends React.Component {
  constructor(props) {
    super(props);
    this.id = this.props.match.params.id;
    this.state = {
      data: {},
      error: null,
      isLoading: true
    };
  }

  componentDidMount() {
    postService.getPost(this.id).then((data) => {
      this.setState({data, isLoading: false});
    }).catch((error) => {
      this.setState({error, isLoading: false});
    });
  }

  render() {
    if (this.state.isLoading) return null;
    if (this.state.error) return (<NotFound/>);

    return (
      <BaseWrapper>
        <Row className="mt-5">
          <Col lg="12" md="12">
            <Fade in={!this.state.isLoading}>
              <Post key={this.state.data.id} postDetails={this.state.data}/>
            </Fade>
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
