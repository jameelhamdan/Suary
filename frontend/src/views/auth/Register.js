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


function RegisterForm() {
  const {register, errors, handleSubmit, formState} = useForm({
    mode: "onChange"
  });

  const onSubmit = data => {
    let username = data['username'];
    let email = data['email'];
    let birth_date = data['birth_date'];
    let password = data['password'];
    let password_confirm = data['password_confirm'];

    ajax.post(apiRoutes.Register(), {
      username: username,
      full_name: username,
      email: email,
      birth_date: birth_date,
      password: password,
      password_confirm: password_confirm
    }).then(res => {
      console.log(res);
    })
  };

  return (
    <Form onSubmit={handleSubmit(onSubmit)}>
      <input size="lg" className="mb-3 form-control form-control-lg" placeholder="Username" name="username" ref={
        register({
          required: true,
          maxLength: 100
        })
      }/>
      {errors.username && errors.username.message}


      <input size="lg" className="mb-3 form-control form-control-lg" placeholder="Email" name="email" ref={
        register({
          required: true,
          maxLength: 100,
          pattern: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        })
      }/>
      {errors.email && errors.email.message}

      <input size="lg" className="mb-3 form-control form-control-lg" placeholder="Date of Birth" type="date" name="birth_date" ref={
        register({
          required: true,
          maxLength: 100
        })
      }/>
      {errors.birth_date && errors.birth_date.message}

      <input size="lg" className="mb-3 form-control form-control-lg" placeholder="Password" type="password" name="password" ref={
        register({
          required: true,
          maxLength: 100
        })
      }/>
      {errors.password && errors.password.message}


      <input size="lg" className="mb-3 form-control form-control-lg" placeholder="Confirm Password" type="password" name="password_confirm" ref={
        register({
          required: true,
          maxLength: 100
        })
      }/>
      {errors.password_confirm && errors.password_confirm.message}

      <ListGroupItem className="d-flex px-3 border-0">
        <strong>Already have an account ? <Link className="mr-auto" to="login">Login</Link> now!</strong>
        <Button theme="accent" size="sm" className="ml-auto">
          <i className="material-icons">lock</i> Register
        </Button>
      </ListGroupItem>
    </Form>

  );
}


export default class Register extends React.Component {
  render() {
    return (
      <Container fluid className="main-content-container px-4">
        <Row className="mt-5">
          <Col md={{size: 8, offset: 2}} sm="12">
            <Card small className="mb-4">
              <CardBody>
                <h5 className="card-title">Register</h5>
                <p className="card-text text-muted">Register a new account!</p>
                <RegisterForm/>
              </CardBody>
            </Card>
          </Col>
        </Row>
      </Container>
    )
  }
}
