var createError = require("http-errors");
var express = require("express");
var path = require("path");
var cookieParser = require("cookie-parser");
var logger = require("morgan");
const cron = require("node-cron");
const taskMaster = require("./schedulers/taskMaster");
require("dotenv").config();

//var indexRouter = require('./routes/index');

//Production Middleware
var compression = require("compression");
var helmet = require("helmet");
//End production middleware

var app = express();

//Stuff for production
app.use(compression()); //Compress all routes
app.use(helmet());
//End stuff for production

//Set up mongoose connection
var mongoose = require("mongoose");
var mongoDB = process.env.MONGODB_URL;

//console.log(mongoDB);

mongoose.connect(mongoDB, { useNewUrlParser: true, useUnifiedTopology: true });
var db = mongoose.connection;
db.on("error", console.error.bind(console, "MongoDB connection error:"));

app.use(logger("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, "public")));

const indexRouter = require("./routes/index");
app.use("/", indexRouter);

// catch 404 and forward to error handler
app.use(function (req, res, next) {
  next(createError(404));
});

// error handler
// app.use(function(err, req, res, next) {
//   // set locals, only providing error in development
//   res.locals.message = err.message;
//   res.locals.error = req.app.get('env') === 'development' ? err : {};

//   // render the error page
//   res.status(err.status || 500);
//   res.render('error');
// });

cron.schedule("*/15 * * * *", () => {
  // Every 15 minutes
  console.log("Updating followers and tweets..");
  taskMaster.hourly_task();
});

cron.schedule("0 0 * * *", () => {
  // The start of every day
  console.log("Analysing trend data to check for at-risk individuals..");
  taskMaster.weekly_task;
});

module.exports = app;
