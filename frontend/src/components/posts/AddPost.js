/* eslint jsx-a11y/anchor-is-valid: 0 */

import React from "react";
import {
  Card,
  CardBody,
  ListGroupItem,
  Button,
  Form
} from "shards-react";
import {useForm} from "react-hook-form";
import {get_errors} from "utils/ajax"
import {postService} from "services/postService";
import history from "utils/history"


export default class AddPostWidget extends React.Component {
  validate_file(file){
    let {setError} = useForm();
    if(file === null || file.length === 0){
      setError('Image is required!');
      return false
    } else {
      return true
    }
  }
  constructor(props) {

    super(props);
    this.state = {
      loading: false,
      file: null,
      errors: [],
    };
    this.onSubmit = this.onSubmit.bind(this);
    this.AddPostForm = this.AddPostForm.bind(this);
    this.onChange = this.onChange.bind(this);
  }

  onChange(e) {
    const new_file = e.target.files[0];
    if(true){
        this.setState({file: new_file});
    } else {
      this.setState({file: null});
    }
  }

  onSubmit(data) {
    this.setState((state) => {
      state.loading = true;
      return state
    });

    postService.addPost(data['content'], this.state.file).then((result) => {
      history.push('profile/')
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

  AddPostForm() {
    const {register, errors, handleSubmit} = useForm();

    return (
      <Form onSubmit={handleSubmit(this.onSubmit)}>
        <input className="mb-3 form-control form-control-lg" name="content" placeholder="Write a new story..." type="text" ref={
          register({
            required: true,
            maxLength: 100
          })
        }/>

        {errors.content && errors.content.message}

        <input onChange= {this.onChange} className="mb-3 form-control form-control-lg" name="image_file" placeholder="Image" type="file" ref={
          register({
            required: true
          })
        }/>
        {errors.image_file && errors.image_file.message}

        <ListGroupItem className="d-flex px-3 border-0">
          <Button type="submit" theme="accent" size="sm" className="ml-auto" disabled={this.state.loading}>
            <i className="material-icons">done</i> Post!
          </Button>
        </ListGroupItem>
      </Form>

    );
  }

  render() {
    return (
      <Card small className="mb-4">
        <CardBody>
          {this.state.errors.map((error) => {
            return <p key={error.i} className="text-danger">{error.message}</p>
          })}
          <this.AddPostForm/>
        </CardBody>
      </Card>
    )
  }
}
