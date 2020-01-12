const createError = require('http-errors');
const express = require('express');
const cookieParser = require('cookie-parser');
const logger = require('morgan');
const cors = require('cors');
const { spawnSync } = require('child_process');
const MongoClient = require('mongodb').MongoClient;
const app = express();

const skills = [
  /\bc\b/,
  /\bc\++\b/,
  /\bc#\b/,
  /\bf\b/,
  /\bf#\b/,
  /\bswift\b/,
  /\bkotlin\b/,
  /\bjava\b/,
  /\bjavascript\b/,
  /\bhtml\b/,
  /\bcss\b/,
  /\bnode\b/,
  /\bnpm\b/,
  /\breact\b/,
  /\bangular\b/,
  /\bruby\b/,
  /\bpython\b/,
  /\bdjango\b/,
  /\bexpress\b/,
  /\bdart\b/,
  /\bgolang\b/,
  /\bcobol\b/,
  /\bada\b/,
  /\bperl\b/,
  /\blisp\b/,
  /\br\b/,
  /\bsql\b/,
  /\brust\b/
];

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
    db = client.db("job-analyser").collection('jobs');
  }
);

/* GET home page. */
app.get('/', (req, res, err) => {
  res.send('API is working properly');
});

app.get('/jobs', (req, res, err) => {
  db.find().toArray((err, docs) => {
    if (err) throw err;
    for (let doc in docs) {
      console.log(doc);
    }
    res.send(docs);
  });
});

app.get('/jobs/state/:state', (req, res, err) => {
  db.find(
    { state: { $eq: req.params.state } }
  ).toArray(async (err, docs) => {
    if (err) throw err;
    for (let doc of docs) {
      if (doc.skills === null) {
        let description = doc.description
          .toLowerCase()
          .replace(",", " ")
          .replace("/", " ");
        let skillsArray = [];
        skills.forEach(s => {
          if (s.test(description))
            skillsArray.push(s.source.replace(/\\b/g, "").replace("\\", ""));
        });
        // const result = spawnSync('python', ['./python/parse_skills.py', doc.description]);
        // let output = result.output.toString();
        // let skills = output.substr(1, output.length - 4).split('\r\n');
        doc.skills = skillsArray;
        db.update(
          { state: { $eq: req.params.state } },
          { $set: { skills: skillsArray, description: '' } }
        );
      }
    }
    res.send(docs);
  });
});

app.get('/states', (req, res, err) => {
  db.distinct('state', (err, docs) => {
    console.log(docs);
    if (err) throw err;
    res.send(docs);
  });
});

app.get('/cities', (req, res, err) => {
  db.distinct('city', (err, docs) => {
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
