import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Grid, Paper, AppBar, Container, Typography, Toolbar, Box } from '@material-ui/core';
import SearchForm from './components/SearchForm';
import ResultsList from './components/ResultsList';
import MyResponsiveLine from './components/MyResponisveLine';
import useMediaQuery from '@material-ui/core/useMediaQuery';
import "./App.css";

const App = () => {
  const [state, setState] = useState({
    state: '',
    apiResponse: '',
    data: null
  });

  const matches = useMediaQuery('(min-width: 600px)');

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
      <Container maxWidth="lg">
        <p>{state.apiResponse}</p>
        <Grid container spacing={3} justify="flex-start">
          <Box clone order={{ sm: 2, md: 1 }}>
            <Grid item sm={12} md={5}>
              <SearchForm state={state} onStateChange={onStateChange} />
              <ResultsList data={state.data} />
            </Grid>
          </Box>
          <Box clone order={{ sm: 1, md: 2 }}>
            <Grid item sm={12} md={7}>
              <Paper>
                <div style={{ height: (matches ? 500 : 300) }}>
                  <MyResponsiveLine />
                </div>
              </Paper>
            </Grid>
          </Box>
        </Grid>
      </Container>
    </React.Fragment>
  );
}

export default App;
