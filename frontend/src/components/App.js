import React, {Component} from "react";
import {render} from "react-dom";
import Ajax from "../components/Api";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    Ajax({
      method: 'GET',
      url: 'TEST/TEST',
    }).then((response) => {
      console.log(response);
      return {
        data: response.data,
        loaded:true,
        placeholder: 'LOADED'
      }
    }).catch((response) => {
      return {
        data: response.data,
        loaded:true,
        placeholder: 'ERROR!'
      }
    });
  }

  render() {
    return 'HELLO WORLD';
  }
}

export default App;

const container = document.getElementById("app");
render(<App/>, container);
