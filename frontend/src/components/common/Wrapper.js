import React from "react";
import {Col, Container, Row} from "shards-react";


class BaseWrapper extends React.Component {
  render() {
    return (
      <Container fluid className="main-content-container px-4">
        {this.props.children}
      </Container>
    )
  }
}

class Wrapper extends React.Component {
  render() {
    return (
      <Container fluid className="main-content-container px-4">
        <Row className="mt-5">
          <Col md={{size: 8, offset: 2}} sm="12">
            {this.props.children}
          </Col>
        </Row>
      </Container>
    )
  }
}

export {
  BaseWrapper,
  Wrapper
};
