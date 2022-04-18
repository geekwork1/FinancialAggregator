import React from 'react';
import './App.css';
import SnippetList from "./components/Snippet";
import axios from "axios";

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'snippets': []
    }
  }

  componentDidMount() {
    const snippets = [
        axios.get('http://127.0.0.1:8000/api/snippet')
            .then(
                response => {
                  const snippets = response.data
                    console.log('С сервера  data: ', snippets)
                  this.setState({'snippets': snippets.results })
                },

            ).catch(error => console.log(error))
    ]

    this.setState(
        {
          'snippets': snippets
        }
    )

  }

  render() {
    return (
        <div>
          <SnippetList snippets={this.state.snippets}/>
        </div>
    )
  }
}

export default App;
