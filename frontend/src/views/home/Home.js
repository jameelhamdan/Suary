import React from "react";
import {Card, CardBody} from "shards-react";
import {Wrapper} from "components/common/Wrapper";
import {connect} from "react-redux";
import AddPostWidget from "components/posts/AddPost"

class Home extends React.Component {
  render() {
    return (
      <Wrapper>
        {this.props.userState.logged_in &&
          <AddPostWidget history={this.props.history}/>
        }
        <Card small className="mb-4">
          <CardBody>
            <h5 className="card-title">Hello {this.props.userState.logged_in ? this.props.userState.userData.username : 'Stranger!'}</h5>
          </CardBody>
        </Card>
      </Wrapper>
    )
  }
}

const mapStateToProps = state => ({
  ...state
});

export default connect(mapStateToProps)(Home)