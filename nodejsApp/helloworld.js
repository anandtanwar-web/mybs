const express = require('express');
const app = express();

// Set up a route to serve the HTML file
app.get('/', function (req, res) {
  res.sendFile(__dirname + '/public/helloworld.html');
});

// Start the server
app.listen(3000, function () {
  console.log('Server listening on port 3000');
});
