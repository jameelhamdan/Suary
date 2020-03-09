import React from "react";
import {Col, Container, Row} from "shards-react";


export default class Wrapper extends React.Component {
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
