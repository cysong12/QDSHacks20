import React, { useState, useEffect } from 'react';
import { Grid, Paper, AppBar, Container, Typography, Toolbar, Box, ThemeProvider } from '@material-ui/core';
import SearchForm from './components/SearchForm';
import ResultsList from './components/ResultsList';
import MyResponsiveLine from './components/MyResponisveLine';
import useMediaQuery from '@material-ui/core/useMediaQuery';
import { data } from "./constants";
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

const containsDate = (dates, date) => {
  for (let i = 0; i < dates.length; i++) {
    if (dates[i].x === date)
      return i;
  }
  return -1;
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
  console.log()
  return skills.sort(compare);
};

const getLineData = data => {
  let lineData = [];
  console.log(data);
  data.forEach(d => {
    let obj = {
      id: d.skill,
      color: "hsl(139, 70%, 50%)",
      data: []
    };
    d.dates.forEach(date => {
      let dateObj = new Date(date);
      let label = dateObj.getFullYear() + "/" + dateObj.getMonth();
      let index = containsDate(d.dates, label);
      if (index === -1) {
        obj.data.push({
          x: label,
          y: 1
        });
      } else {
        obj.data[index].y++;
      }
    });
    lineData.push(obj);
  });
  console.log(lineData);
  return lineData;
};

const App = () => {
  const [state, setState] = useState({
    state: '',
    dateFrom: null,
    dateTo: null,
    data: null,
    lineData: [],
    loading: false
  });

  const matches = useMediaQuery('(min-width: 960px)');

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
