const express = require('express');
const app = express();

app.use(express.static(__dirname + '/public'));

// Define routes for the different services
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/mock-interviews.html');
//  res.render('mock-interviews.html')
//res.sendFile(__dirname + '/public/helloworld.html');
});

app.get('/mock-interviews', (req, res) => {
  res.sendFile(__dirname + '/public/mock-interviews.html');
//  res.render('mock-interviews.html')
//res.sendFile(__dirname + '/public/helloworld.html');
});

app.get('/feedback-evaluation', (req, res) => {
  res.sendFile(__dirname + '/public/feedback-evaluation.html');
  //res.render('mock-interviews.html')
  //res.sendFile(__dirname + '/public/helloworld.html');
});

app.get('/Signup', (req, res) => {
  res.sendFile(__dirname + '/public/Accounts.html');
  //res.render('mock-interviews.html')
  //res.sendFile(__dirname + '/public/helloworld.html');
});

// Start the server
app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
