import React from "react";
import {connect} from "react-redux";
import Feed from "./Feed";
import Search from "./Search";


class Home extends React.Component {
  constructor(props) {
    super(props);
    const params = new URLSearchParams(this.props.location.search);
    this.state = {
      search_query: params.get('search') || null
    }
  }

  render() {
    if (this.state.search_query && this.state.search_query !== ''){
      return <Search search={this.state.search_query} />
    } else {
      return <Feed />
    }
  }
}

const mapStateToProps = state => ({
  ...state
});

export default connect(mapStateToProps)(Home)