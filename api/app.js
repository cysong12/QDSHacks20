const createError = require('http-errors');
const express = require('express');
const cookieParser = require('cookie-parser');
const logger = require('morgan');
const cors = require('cors');
const MongoClient = require('mongodb').MongoClient;
const app = express();
let db;

app.use(cors());
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

MongoClient.connect(
  "mongodb://admin:admin123@ds052408.mlab.com:52408/job-analyser",
  (err, client) => {
    if (err) throw err;
    db = client.db("job-analyser");
  }
);

/* GET home page. */
app.get('/', (req, res, err) => {
  res.send('API is working properly');
});

app.get('/jobs', (req, res, err) => {
  db.collection('jobs').find().toArray((err, docs) => {
    if (err) throw err;
    res.send(docs);
  });
});

app.get('/jobs/state/:state', (req, res, err) => {
  db.collection('jobs').find({ state: { $eq: req.params.state } }).toArray((err, docs) => {
    if (err) throw err;
    res.send(docs);
  });
});

app.get('/states', (req, res, err) => {
  db.collection('jobs').distinct('state', (err, docs) => {
    console.log(docs);
    if (err) throw err;
    res.send(docs);
  });
});

app.get("/cities", (req, res, err) => {
  db.collection("jobs").distinct("city", (err, docs) => {
    console.log(docs);
    if (err) throw err;
    res.send(docs);
  });
});

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.send(err.message);
});

module.exports = app;
