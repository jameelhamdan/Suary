/**
 * Simple script to render and serve the frontend alone using remote API_URL
 *
 */

const path = require("path");
const express = require("express");
const app = express();
app.engine('html', require('ejs').renderFile);

const frontendStatic = path.join(__dirname, 'public');
const frontendEntryFile = path.join(__dirname, 'frontend', 'templates', 'index_raw.html');
const PORT = process.env.PORT || 3000;
const API_URL = process.env.API_URL || 'http://127.0.0.1:8000/api';  // the /api is very important

const context = {
  static_root: 'public',
  api_url: API_URL
};

app.use('/public', express.static(frontendStatic));
app.get('/*', (req, res) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Credentials", "true");
  res.header("Access-Control-Allow-Methods", "GET,HEAD,OPTIONS,POST,PUT,PATCH");
  res.header("Access-Control-Allow-Headers", "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers");
  res.render(frontendEntryFile, context);
});

// start express server on port PORT
app.listen(PORT, () => {
  console.log(`frontend started on port ${PORT}`);
});
