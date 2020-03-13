import React from "react";
import {Card, CardBody, Col, Row, Fade} from "shards-react";
import {BaseWrapper} from "components/common/Wrapper";
import {userService} from "services/userService";
import UserDetails from './components/UserDetails';
import NotFound from "components/common/pages/NotFound"


export default class UserDetail extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      data: {},
      error: null,
      isLoading: true
    };
  }

  async componentDidMount() {
    const username = this.props.match.params.username;
    try {
      const data = await userService.getUser(username);
      this.setState({data, isLoading: false});
    } catch(error){
      this.setState({error, isLoading: false});
    }
  }

  render() {
    if (this.state.isLoading) return null;
    if (this.state.error) return (<NotFound/>);

    return (
      <BaseWrapper>
        <Row className="mt-5">
          <Col lg="3" md="4">
            <Fade in={!this.state.isLoading}>
              <UserDetails userDetails={this.state.data}/>
            </Fade>
          </Col>
          <Col lg="9" md="8">
            <Card small className="mb-4">
              <CardBody>
                <h5 className="card-title">USER POSTS GO HERE</h5>
              </CardBody>
            </Card>
          </Col>
        </Row>
      </BaseWrapper>
    );
  }
}