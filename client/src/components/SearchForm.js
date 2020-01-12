import React from 'react';
import Autocomplete from '@material-ui/lab/Autocomplete';
import { TextField, Grid } from '@material-ui/core';
import DateFnsUtils from '@date-io/date-fns';
import { MuiPickersUtilsProvider, KeyboardDatePicker } from '@material-ui/pickers';
import { states } from '../constants';
import '../App.css';

const SearchForm = props => {
  return (
    <MuiPickersUtilsProvider utils={DateFnsUtils}>
      <form className="form">
        <Grid container spacing={3}>
          <Grid item xs={12}>
            <Autocomplete
              id="state"
              options={states}
              getOptionLabel={option => option.name}
              onChange={props.onStateChange}
              renderInput={params => (
                <TextField
                  {...params}
                  value={props.state.state}
                  label="State"
                  variant="outlined"
                  fullWidth
                />
              )}
            />
          </Grid>
          <Grid item xs={6}>
            <KeyboardDatePicker
              disableToolbar
              variant="inline"
              format="yyyy-MM-dd"
              margin="normal"
              fullWidth
              id="dateFrom"
              label="Date From"
              value={props.state.dateFrom}
              onChange={props.onDateFromChange}
            />
          </Grid>
          <Grid item xs={6}>
            <KeyboardDatePicker
              disableToolbar
              variant="inline"
              format="yyyy-MM-dd"
              margin="normal"
              fullWidth
              id="dateTo"
              label="Date To"
              value={props.state.dateTo}
              onChange={props.onDateToChange}
            />
          </Grid>
        </Grid>
      </form>
    </MuiPickersUtilsProvider>
  );
};

export default SearchForm;
