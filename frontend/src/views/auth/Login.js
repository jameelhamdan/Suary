/* eslint jsx-a11y/anchor-is-valid: 0 */

import React, {useEffect} from "react";
import {
  Container,
  Row,
  Col,
  Card,
  CardBody, ListGroupItem, Button, Form
} from "shards-react";
import {Link} from "react-router-dom";
import {useForm} from "react-hook-form";
import {ajax, apiRoutes} from "../../utils/ajax/ajax"


function LoginForm() {
  const {register, errors, handleSubmit, formState} = useForm({
    mode: "onChange"
  });

  const onSubmit = data => {
    let username = data['username'];
    let password = data['password'];
    ajax.post(apiRoutes.Login(), {
      username: username,
      password: password,
    }).then(res => {
      console.log(res);
    })
  };

  return (
    <Form onSubmit={handleSubmit(onSubmit)}>
      <input className="mb-3 form-control form-control-lg" name="username" placeholder="Username" type="text" ref={
        register({
          required: true,
          maxLength: 100
        })
      }/>
      {errors.username && errors.username.message}

      <input className="mb-3 form-control form-control-lg" name="password" placeholder="Password" type="password" ref={
        register({
          required: true,
          maxLength: 100
        })
      }/>
      {errors.password && errors.password.message}

      <ListGroupItem className="d-flex px-3 border-0">
        <strong>Don't have an account ? <Link className="mr-auto" to="register">Register</Link> now!</strong>
        <Button type="submit" theme="accent" size="sm" className="ml-auto">
          <i className="material-icons">lock</i> Login
        </Button>
      </ListGroupItem>
    </Form>

  );
}


export default class Login extends React.Component {
  render() {
    return (
      <Container fluid className="main-content-container px-4">
        <Row className="mt-5">
          <Col md={{size: 8, offset: 2}} sm="12">
            <Card small className="mb-4">
              <CardBody>
                <h5 className="card-title">Login</h5>
                <p className="card-text text-muted">Login to Suary app!</p>
                <LoginForm/>
              </CardBody>
            </Card>
          </Col>
        </Row>
      </Container>
    )
  }
}
