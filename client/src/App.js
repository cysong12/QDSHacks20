import React, { useState, useEffect } from 'react';
import { Grid, Paper, AppBar, Container, Typography, Toolbar, Box, ThemeProvider } from '@material-ui/core';
import SearchForm from './components/SearchForm';
import ResultsList from './components/ResultsList';
import MyResponsiveLine from './components/MyResponisveLine';
import useMediaQuery from '@material-ui/core/useMediaQuery';
import { createMuiTheme } from "@material-ui/core/styles";
import "./App.css";

const theme = createMuiTheme({
  breakpoints: {
    values: {
      xs: 0,
      sm: 600,
      md: 960,
      lg: 1580,
      xl: 1920
    }
  }
});

const App = () => {
  const [state, setState] = useState({
    state: '',
    dateFrom: null,
    dateTo: null,
    data: null,
    loading: false
  });

  const matches = useMediaQuery('(min-width: 600px)');

  useEffect(() => {
    console.log('hello world');
    const dateFrom = new Date();
    const dateTo = new Date();
    dateFrom.setMonth(dateTo.getMonth() - 6);
    setState({
      ...state, 
      dateFrom: dateFrom,
      dateTo: dateTo
    });
  }, []);

  const handleStateChange = (event, value) => {
    console.log(value);
    fetch('http://localhost:9000/jobs/state/' + value.abbreviation)
      .then(res => res.json())
      .then(data => {
        setState({
          ...state,
          data: data,
          loading: false
        });
      });
    setState({
      ...state,
      state: value,
      loading: true
    });
  };

  const handleDateFromChange = date => {
    setState({
      ...state, 
      dateFrom: date
    });
  };

  const handleDateToChange = date => {
    setState({
      ...state,
      dateTo: date
    });
  };

  return (
    <React.Fragment>
      <ThemeProvider theme={theme}>
        <AppBar className="appBar" position="relative">
          <Toolbar>
            <Typography variant="h6">Software Jobs Analyser</Typography>
          </Toolbar>
        </AppBar>
        <Container maxWidth="lg">
          <Grid container spacing={3} justify="flex-start">
            <Box clone order={{ xs: 2, sm: 1 }}>
              <Grid item xs={12} md={4}>
                <SearchForm
                  state={state}
                  onStateChange={handleStateChange}
                  onDateFromChange={handleDateFromChange}
                  onDateToChange={handleDateToChange}
                />
                <ResultsList data={state.data} loading={state.loading} />
              </Grid>
            </Box>
            <Box clone order={{ xs: 1, sm: 2 }}>
              <Grid item xs={12} md={8}>
                <Paper>
                  <div style={{ height: matches ? 700 : 400 }}>
                    <MyResponsiveLine />
                  </div>
                </Paper>
              </Grid>
            </Box>
          </Grid>
        </Container>
      </ThemeProvider>
    </React.Fragment>
  );
}

export default App;
