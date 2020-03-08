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
import {ajax, apiRoutes, get_errors} from "../../utils/ajax/ajax"
import history from "../../utils/history";


export default class Register extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: false,
      errors: [],
    };
    this.onSubmit = this.onSubmit.bind(this);
    this.RegisterForm = this.RegisterForm.bind(this);

  }

  onSubmit(data) {
    let username = data['username'];
    let email = data['email'];
    let birth_date = data['birth_date'];
    let password = data['password'];
    let password_confirm = data['password_confirm'];

    this.setState((state) => {
      state.loading = true;
      return state
    });

    ajax.post(apiRoutes.Register(), {
      username: username,
      full_name: username,
      email: email,
      birth_date: birth_date,
      password: password,
      password_confirm: password_confirm
    }).then(res => {
      history.push('/login');
    }).catch(error => {
      if (error.response.status === 400) {
        const response_data = error.response.data;
        let errors = get_errors(response_data);
        this.setState((state) => {
          state.errors = errors;
          state.loading = false;
          return state
        });
      }
    })
  };

  RegisterForm() {
    const {register, errors, handleSubmit} = useForm();

    return (
      <Form onSubmit={handleSubmit(this.onSubmit)}>
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
          <Button theme="accent" size="sm" className="ml-auto" disabled={this.state.loading}>
            <i className="material-icons">lock</i> Register
          </Button>
        </ListGroupItem>
      </Form>
    );
  }

  render() {
    return (
      <Container fluid className="main-content-container px-4">
        <Row className="mt-5">
          <Col md={{size: 8, offset: 2}} sm="12">
            <Card small className="mb-4">
              <CardBody>
                <h5 className="card-title">Register</h5>
                <p className="card-text text-muted">Register to Suary!</p>
                {this.state.errors.map((error) => {
                  return <p key={error.i} className="text-danger">{error.message}</p>
                })}
                <this.RegisterForm/>
              </CardBody>
            </Card>
          </Col>
        </Row>
      </Container>
    )
  }
}
