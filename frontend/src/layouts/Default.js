import React from "react";
import PropTypes from "prop-types";
import { Container, Row, Col } from "shards-react";

import MainNavbar from "components/layout/MainNavbar/MainNavbar";
import MainFooter from "components/layout/MainFooter";

const DefaultLayout = ({ children, history, noNavbar, noFooter }) => (
  <Container fluid>
    <Row>
      <Col className="main-content p-0" lg="12" md="12" sm="12" tag="main">
        {!noNavbar && <MainNavbar history={history}/>}
        {children}
        {!noFooter && <MainFooter />}
      </Col>
    </Row>
  </Container>
);

DefaultLayout.propTypes = {
  noNavbar: PropTypes.bool,
  noFooter: PropTypes.bool,
  history: PropTypes.object
};

DefaultLayout.defaultProps = {
  noNavbar: false,
  noFooter: true
};

export default DefaultLayout;
