import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

const App = () => {
  const [state, setState] = useState({
    apiResponse: ''
  });

  const callAPI = () => {
    fetch('http://localhost:9000/test')
      .then(res => res.text())
      .then(res => setState({ apiResponse: res }));
  };

  useEffect(() => {
    callAPI();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          {state.apiResponse}
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
