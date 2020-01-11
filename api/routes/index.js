var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', (req, res, err) => {
  res.send('API is working properly');
});

module.exports = router;
