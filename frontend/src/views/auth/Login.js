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


export default class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: false,
      errors: [],
    };
    this.onSubmit = this.onSubmit.bind(this);
    this.LoginForm = this.LoginForm.bind(this);

  }

  onSubmit(data) {
    let username = data['username'];
    let password = data['password'];
    this.setState((state) => {
      state.loading = true;
      return state
    });
    ajax.post(apiRoutes.Login(), {
      username: username,
      password: password,
    }).then(res => {
      console.log(res);
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

  LoginForm() {
    const {register, errors, handleSubmit} = useForm();

    return (
      <Form onSubmit={handleSubmit(this.onSubmit)}>
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
          <Button type="submit" theme="accent" size="sm" className="ml-auto" disabled={this.state.loading}>
            <i className="material-icons">lock</i> Login
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
                <h5 className="card-title">Login</h5>
                <p className="card-text text-muted">Login to Suary!</p>
                {this.state.errors.map((error) => {
                  return <p key={error.i} className="text-danger">{error.message}</p>
                })}
                <this.LoginForm/>
              </CardBody>
            </Card>
          </Col>
        </Row>
      </Container>
    )
  }
}
