const followerTasks = require("./followerTasks");
const tweetTasks = require("./tweetTasks");
const getUnixTime = require("date-fns/getUnixTime");
const Record = require("../models/record");
const Statistics = require("../node_modules/statistics.js/statistics.js");

const should_notify = (tweets) => {
  try {
    const score = correlation_analysis(tweets);
    return score > 0.2;
  } catch {
    return false;
  }
};

const correlation_analysis = (tweets) => {
  const time = [],
    stress_ratings = [];
  tweets.forEach((tweet) => {
    stress_ratings.push(tweet["sadness"] + tweet["anger"]);
    time.push(getUnixTime(tweet["date"]));
  });
  const normalized_time = normalize_array(time);
  const data = [];
  normalized_time.forEach((element, index) => {
    data.push({ time: element, stress: stress_ratings[index] });
  });
  columns = {
    time: "interval",
    stress: "interval",
  };
  console.log("Data");
  console.log(data);
  const stats = new Statistics(data, columns);
  return stats.correlationCoefficient("time", "stress")[
    "correlationCoefficient"
  ];
};

const normalize_array = (array) => {
  let max_value = array[0],
    min_value = array[0];
  array.forEach((element) => {
    if (element > max_value) max_value = element;
    if (element < min_value) min_value = element;
  });
  return array.map((element) => {
    return (element - min_value) / (max_value - min_value);
  });
};

const analyse_single_user = async (user_id) => {
  const tweets = await Record.find({ user_id: user_id });
  const status = should_notify(tweets);
  return status;
};

const analyse = async (user_ids) => {
  console.log("Analysing users...");
  const toNotify = [];
  statuses = await Promise.all(
    user_ids.map((user_id) => analyse_single_user(user_id))
  );
  user_ids.forEach((user_id, index) => {
    if (statuses[index] === true) toNotify.push(user_id);
  });

  return toNotify;
};

exports.analyse_single_user = analyse_single_user;
exports.analyse = analyse;
