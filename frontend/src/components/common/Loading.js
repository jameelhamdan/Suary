import React from "react";
import MoonLoader from "react-spinners/MoonLoader";


export default class Loading extends React.Component {
  render() {
    return (
      <MoonLoader
        loading={true}
      />
    )
  }
}
