import React from "react";
import {FormInput, InputGroup, InputGroupText, InputGroupAddon, Row, Col, ListGroupItem, Button} from "shards-react";
import PropTypes from "prop-types";
import {Image as ImageIcon, Send as SendIcon} from "@material-ui/icons";
import {postService} from "services/postService";


export default class AddComment extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: false,
      file: null,
      content: null
    };

    this.post_id = this.props.post_id;
    this.handler = this.props.handler;
    this.fileRef = React.createRef();
    this.inputRef = React.createRef();
    this.Submit = this.Submit.bind(this);
    this.onChangeFile = this.onChangeFile.bind(this);
    this.onChangeInput = this.onChangeInput.bind(this);
    this.handleFileClick = this.handleFileClick.bind(this);
    this._handleKeyDown = this._handleKeyDown.bind(this);
  }

  handleFileClick(e) {
    this.fileRef.current.click();
  };

  _handleKeyDown(e) {
    if (e.key === 'Enter') {
      this.Submit();
    }
  }

  onChangeFile(e) {
    const file = e.target.files[0];
    this.setState((state) => {
        state.file = file;
        return state;
      }
    );
  }

  onChangeInput(e) {
    const content = e.target.value;
    this.setState((state) => {
        state.content = content;
        return state
      }
    );
  }

  Submit() {
    if (this.state.loading) return;

    const content = this.state.content;
    const file = this.state.file;
    if (!content && !file) return;

    this.setState((state) => {
      state.loading = true;
      return state
    });

    postService.addPostComment(this.post_id, content, file).then((result) => {
      this.inputRef.current.value = '';
      this.fileRef.current.value = null;
      this.handler(result);
    }).catch(error => {
      if(!error.response){
        console.error(error);
      }
      if (error.response.status === 400) {
        // TODO: Handle error here
      }
    });

    this.setState((state) => {
      state.loading = false;
      state.file = null;
      state.content = null;
      return state
    });
  };

  render() {
    return (
      <ListGroupItem key={'add_form'}>
        <Row>
          <Col lg={12}>
            <InputGroup seamless>
              <InputGroupAddon type="append">
                <InputGroupText>
                  <Button theme="transparent" onClick={this.handleFileClick} style={{marginRight: 4}} disabled={this.state.loading}>
                    <ImageIcon></ImageIcon>
                  </Button>
                  <Button theme="transparent" onClick={this.Submit} disabled={this.state.loading}>
                    <SendIcon></SendIcon>
                  </Button>
                </InputGroupText>
              </InputGroupAddon>
              <input type="file" accept="image/*" ref={this.fileRef} onChange={this.onChangeFile} style={{display: 'none'}}/>
              <FormInput onKeyDown={this._handleKeyDown} ref={this.inputRef} placeholder="Write a comment" onChange={this.onChangeInput} disabled={this.state.loading} />
            </InputGroup>
          </Col>
        </Row>
      </ListGroupItem>
    );
  }

  static propTypes = {
    post_id: PropTypes.string.isRequired,
    handler: PropTypes.func.isRequired,
  };
}
