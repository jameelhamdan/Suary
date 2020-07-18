import React from "react";
import {Wrapper} from "components/common/Wrapper";
import PostList from "components/posts/PostList";
import {postService} from "services/postService";
import {
  Form,
  InputGroup,
  InputGroupAddon,
  InputGroupText,
  CardText,
} from "shards-react";
import {useForm} from "react-hook-form";


export default class Search extends React.Component {
  constructor(props) {
    super(props);
    this.onSubmit = this.onSubmit.bind(this);
    this.searchForm = this.searchForm.bind(this);
    this.loadPosts = this.loadPosts.bind(this);
    this.listRef = React.createRef();
    this.state = {
      q: this.props.match.params.q
    };
  }

  searchForm() {
    const {register, errors, handleSubmit} = useForm({
      defaultValues: {
        search: this.state.q
      }
    });

    return (
      <Form onSubmit={handleSubmit(this.onSubmit)}>
        <InputGroup seamless>
          <InputGroupAddon type="prepend">
            <InputGroupText>
              <i className="material-icons">search</i>
            </InputGroupText>
          </InputGroupAddon>
          <input
            name="search"
            placeholder="Search for something..."
            className="form-control"
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

  onSubmit(data) {
    let search_query = data.search;
    if (search_query && search_query !== '' && search_query !== undefined) {
      this.setState({
        q: search_query,
      });
      this.props.history.push(`/search/${search_query}`);
      this.listRef.current.forceUpdate();
    }
  }

  loadPosts = (page, cursor) => {
    return postService.searchPosts(this.state.q, cursor).then((data) => {
      return data;
    });
  };

  render() {
    return (
      <Wrapper>
        <this.searchForm/>
        <div className="mb-2"/>
        <PostList loadMoreFunc={this.loadPosts} ref={this.listRef}>
          <CardText>We came up empty...</CardText>
        </PostList>
      </Wrapper>
    )
  }
}
