import React from "react";
import PropTypes from "prop-types";
import classNames from "classnames";
import {Container, Navbar} from "shards-react";

import NavbarSearch from "./NavbarSearch";
import NavbarNav from "./NavbarNav/NavbarNav";
import NavbarToggle from "./NavbarToggle";

export default class MainNavbar extends React.Component {
  constructor(props) {
    super(props);
    this.classes = classNames(
      "main-navbar",
      "bg-white",
      this.props.stickyTop && "sticky-top"
    );
    this.layout = this.props.layout;
  }

  render() {
    return (
      <div className={this.classes}>
        <Container className="p-0">
          <Navbar type="light" className="align-items-stretch flex-md-nowrap p-0">
            <NavbarSearch history={this.props.history}/>
            <NavbarNav/>
            <NavbarToggle/>
          </Navbar>
        </Container>
      </div>
    );
  }

  static propTypes = {
    layout: PropTypes.string,
    stickyTop: PropTypes.bool,
    history: PropTypes.object
  };

  static  defaultProps = {
    stickyTop: true
  };
};
