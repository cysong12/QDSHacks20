import React from 'react';
import { css } from '@emotion/core';
import BarLoader from 'react-spinners/BarLoader';
import { Card, CardContent, Typography, Box } from "@material-ui/core";
import '../App.css';

const ResultsList = props => {
  return (
    <React.Fragment>
      <Box display="flex" justifyContent="center">
        <BarLoader className="loader" height={4} width={400} loading={props.loading} />
      </Box>
      {props.data && !props.loading && (
        <div>
          {props.data.map((d, i) => (
            <Card className="card" key={i}>
              <CardContent>
                <Typography gutterBottom variant="h6">
                  {d.jobTitle}
                </Typography>
                <Typography variant="body1">{d.companyName}</Typography>
              </CardContent>
            </Card>
          ))}
        </div>
      )}
    </React.Fragment>
  );
};

export default ResultsList;
