import React, { useState, useEffect } from 'react';
import { AppBar, Container, Typography, Toolbar, Card, CardContent } from '@material-ui/core';
import SearchForm from './components/SearchForm';
import './App.css';

const App = () => {
  const [state, setState] = useState({
    state: '',
    apiResponse: '',
    data: null
  });

  const callAPI = () => {
    fetch('http://localhost:9000/')
      .then(res => res.text())
      .then(res => setState({ apiResponse: res }));
  };

  useEffect(() => {
    callAPI();
  }, []);

  const onStateChange = (event, value) => {
    console.log(value);
    fetch('http://localhost:9000/jobs/state/' + value.abbreviation)
      .then(res => res.json())
      .then(res => {
        setState({
          ...state,
          data: res
        });
      });
    setState({
      ...state,
      state: value
    });
  };

  return (
    <React.Fragment>
      <AppBar position="relative">
        <Toolbar>
          <Typography variant="h6">Job Analyser</Typography>
        </Toolbar>
      </AppBar>
      <Container maxWidth="md">
        <p>{state.apiResponse}</p>
        <SearchForm
          state={state}
          onStateChange={onStateChange}
        />
        {state.data && (
          <div>
            {state.data.map((d, i) => (
              <Card className="card" key={i}>
                <CardContent>
                  <Typography gutterBottom variant="h5">
                    {d.jobTitle}
                  </Typography>
                  <Typography variant="body1">{d.companyName}</Typography>
                </CardContent>
              </Card>
            ))}
          </div>
        )}
      </Container>
    </React.Fragment>
  );
}

export default App;
