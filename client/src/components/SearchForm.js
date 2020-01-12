import React from 'react';
import Autocomplete from "@material-ui/lab/Autocomplete";
import { TextField } from "@material-ui/core";
import { states } from "../constants";
import '../App.css';

const SearchForm = props => {
  return (
    <form className="form">
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
    </form>
  );
};

export default SearchForm;
