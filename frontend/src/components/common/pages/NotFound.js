import {StatusCode} from "react-http-status-code";
import React from "react";

export default class NotFound extends React.Component {
  render() {
    return (
      <StatusCode code={404}>
        <div>
          <p>Sorry, page was not found</p>
        </div>
      </StatusCode>
    )
  }
}