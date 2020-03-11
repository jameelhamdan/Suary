import React from "react";
import {Card, CardBody} from "shards-react";
import Wrapper from "components/common/Wrapper";
import {connect} from "react-redux";


class Home extends React.Component {
  render() {
    return (
      <Wrapper>
        <Card small className="mb-4">
          <CardBody>
            <h5 className="card-title">Hello {this.props.userState.userData != null ? this.props.userState.userData.username : 'Stranger!'}</h5>
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