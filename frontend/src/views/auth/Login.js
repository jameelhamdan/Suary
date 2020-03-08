/* eslint jsx-a11y/anchor-is-valid: 0 */

import React from "react";
import {
  Container,
  Row,
  Col,
  Card,
  CardBody,
  Button, FormInput, Form, ListGroupItem
} from "shards-react";
import {Link} from "react-router-dom";

class Login extends React.Component {

  render() {
    return (
      <Container fluid className="main-content-container px-4">
        <Row className="mt-5">
          <Col md={{size: 8, offset: 2}} sm="12">
            <Card small className="card-post mb-4">
              <CardBody>
                <h5 className="card-title">Login</h5>
                <p className="card-text text-muted">Login to suary app!</p>
                <Form className="add-new-post">
                  <FormInput size="lg" className="mb-3" placeholder="Username"/>
                  <FormInput size="lg" className="mb-3" placeholder="Password" type="password"/>
                  <ListGroupItem className="d-flex px-3 border-0">
                    <strong>Don't have an account ? <Link className="mr-auto" tag={Link} to="register">Register</Link> now!</strong>
                    <Button theme="accent" size="sm" className="ml-auto">
                      <i className="material-icons">lock</i> Login
                    </Button>
                  </ListGroupItem>
                </Form>
              </CardBody>
            </Card>
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Login;
