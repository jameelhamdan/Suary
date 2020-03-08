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

class Register extends React.Component {

  render() {
    return (
      <Container fluid className="main-content-container px-4">
        <Row className="mt-5">
          <Col md={{size: 8, offset: 2}} sm="12">
            <Card small className="card-post mb-4">
              <CardBody>
                <h5 className="card-title">Register</h5>
                <p className="card-text text-muted">Register a new account!</p>
                <Form className="add-new-post">
                  <FormInput size="lg" className="mb-3" name="username" placeholder="Username"/>
                  <FormInput size="lg" className="mb-3" name="email" placeholder="Email"/>
                  <FormInput size="lg" className="mb-3" name="birth_date" placeholder="Date of Birth" type="date"/>
                  <FormInput size="lg" className="mb-3" name="password" placeholder="Password" type="password"/>
                  <FormInput size="lg" className="mb-3" name="password_confirm" placeholder="Confirm Password" type="password"/>

                  <ListGroupItem className="d-flex px-3 border-0">
                    <strong>Already have an account ? <Link className="mr-auto" tag={Link} to="login">Login</Link> now!</strong>
                    <Button theme="accent" size="sm" className="ml-auto">
                      <i className="material-icons">lock</i> Register
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

export default Register;
