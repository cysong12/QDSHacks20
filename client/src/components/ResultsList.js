import React from 'react';
import { Card, CardContent, Typography } from "@material-ui/core";
import '../App.css';

const ResultsList = props => {

  return (
    <React.Fragment>
      {props.data && (
        <div>
          {props.data.map((d, i) => (
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
    </React.Fragment>
  );
};

export default ResultsList;
