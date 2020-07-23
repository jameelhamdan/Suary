import React from "react";
import {
  Form,
  InputGroup,
  InputGroupAddon,
  InputGroupText,
} from "shards-react";
import {useForm} from "react-hook-form";

export default class NavbarSearch extends React.Component {
  constructor(props) {
    super(props);
    this.onSubmit = this.onSubmit.bind(this);
    this.searchForm = this.searchForm.bind(this);
  }

  onSubmit(data) {
    let search_query = data.search;
    if (search_query && search_query !== '' && search_query !== undefined) {
      this.props.history.push(`/search/${search_query}`);
    }
  }

  searchForm() {
    const {register, errors, handleSubmit} = useForm();

    return (
      <Form onSubmit={handleSubmit(this.onSubmit)} className="main-navbar__search w-100 d-none d-md-flex d-lg-flex">
        <InputGroup seamless className="ml-3">
          <InputGroupAddon type="prepend">
            <InputGroupText>
              <i className="material-icons">search</i>
            </InputGroupText>
          </InputGroupAddon>
          <input
            name="search"
            placeholder="Search for something..."
            className="navbar-search form-control"
            ref={
              register({
                required: true,
              })
            }
          />
        </InputGroup>
      </Form>
    );
  }

  render() {
    return (
      <this.searchForm/>
    )
  }
}
