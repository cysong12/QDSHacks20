import React, { useState, useEffect } from 'react';
import { Grid, Paper, AppBar, Container, Typography, Toolbar, Box, ThemeProvider } from '@material-ui/core';
import SearchForm from './components/SearchForm';
import ResultsList from './components/ResultsList';
import MyResponsiveLine from './components/MyResponisveLine';
import useMediaQuery from '@material-ui/core/useMediaQuery';
import { createMuiTheme } from '@material-ui/core/styles';
import moment from 'moment';
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

const compare = (a, b) => {
  return b.count - a.count;
};

const containsSkill = (skills, skill) => {
  for (let i = 0; i < skills.length; i++) {
    if (skills[i].skill === skill)
      return i;
  }
  return -1;
};  

const generateDates = (dateFrom, dateTo) => {
  let dates = [];
  let from = moment(dateFrom);
  let to = moment(dateTo);
  while (from <= to) {
    dates.push(moment(from).format('YYYY-MM'));
    from = moment(from).add(1, 'months');
  }
  console.log(dates);
  return dates;
};

const getSkills = data => {
  let skills = [];
  for (let d of data) {
    for (let s of d.skills) {
      let index = containsSkill(skills, s);
      if (index === -1) {
        skills.push({
          skill: s,
          count: 1,
          dates: [d.date]
        });
      } else {
        skills[index].count++;
        skills[index].dates.push(d.date);
      }
    }
  }
  return skills.sort(compare);
};

const App = () => {
  const [state, setState] = useState({
    state: '',
    dateFrom: new Date('2018-09-01'),
    dateTo: new Date('2019-09-30'),
    data: null,
    lineData: [],
    loading: false
  });

  const matches = useMediaQuery('(min-width: 960px)');

  const getLineData = data => {
    let lineData = [];
    let dates = generateDates(state.dateFrom, state.dateTo);
    data.forEach(d => {
      let obj = {
        id: d.skill,
        color: "hsl(139, 70%, 50%)",
        data: []
      };
      dates.forEach(date => {
        let label = moment(date).format('YYYY-MM');
        let count = d.dates.filter(dt => label === moment(dt).format('YYYY-MM')).length;
        obj.data.push({
          x: label,
          y: count
        });
      });
      lineData.push(obj);
    });
    console.log(lineData);
    return lineData;
  };

  const handleStateChange = (event, value) => {
    let res = fetch('http://localhost:9000/jobs/state/' + value.abbreviation)
      .then(res => res.json())
      .then(data => {
        const skills = getSkills(data);
        const lineData = getLineData(skills);
        setState({
          ...state,
          data: skills,
          lineData: lineData,
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
    const lineData = getLineData(state.data);
    setState({
      ...state, 
      dateFrom: date,
      lineData: lineData
    });
  };

  const handleDateToChange = date => {
    const lineData = getLineData(state.data);
    setState({
      ...state,
      dateTo: date,
      lineData: lineData
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
            <Box clone order={{ xs: 2, md: 1 }}>
              <Grid item xs={12} md={5}>
                <SearchForm
                  state={state}
                  onStateChange={handleStateChange}
                  onDateFromChange={handleDateFromChange}
                  onDateToChange={handleDateToChange}
                />
                <ResultsList data={state.data} loading={state.loading} />
              </Grid>
            </Box>
            <Box clone order={{ xs: 1, md: 2 }}>
              <Grid item xs={12} md={7}>
                <Paper>
                  <div style={{ height: matches ? 700 : 500 }}>
                    <MyResponsiveLine data={state.lineData} />
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
