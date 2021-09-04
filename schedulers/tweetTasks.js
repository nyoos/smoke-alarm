const Record = require("../models/record");
const { spawn } = require("child_process");
const JSONbigString = require("json-bigint")({ storeAsString: true });
var sub = require("date-fns/sub");
var formatISO = require("date-fns/formatISO");

const read_last_100_tweets = async (user_id) => {
  return new Promise((resolve, reject) => {
    let posts;
    const python = spawn("python", ["./scripts/analyse_tweets.py", user_id]);
    python.stdout.on("data", function (data) {
      posts = data.toString();
      posts = JSONbigString.parse(posts);
      console.log(posts);
    });
    python.on("close", (code) => {
      console.log(user_id);
      resolve(posts);
    });
  });
};

const initialize_new_followers = async (user_ids) => {
  new_data = await Promise.all(
    user_ids.map((user_id) => {
      return read_last_100_tweets(user_id);
    })
  );

  console.log(new_data);
  new_data.forEach((element, i) => {
    element.forEach((datapoint) => {
      console.log(datapoint);
      const { anger, joy, optimism, sadness } = datapoint["score"];
      const created_at = datapoint["created_at"];
      const record = new Record({
        user_id: user_ids[i],
        date: created_at,
        anger,
        joy,
        optimism,
        sadness,
      });

      record.save();
    });
  });
};

const delete_tweets_from_user = async (user_id) => {
  await Record.deleteMany({ user_id: user_id });
};

const read_last_15_minute_tweets = async (user_id, last_check) => {
  return new Promise((resolve, reject) => {
    let posts;
    const python = spawn("python", [
      "./scripts/analyse_tweets.py",
      user_id,
      last_check,
    ]);
    python.stdout.on("data", function (data) {
      posts = data.toString();
      posts = JSONbigString.parse(posts);
      console.log(posts);
    });
    python.on("close", (code) => {
      console.log(user_id);
      resolve(posts);
    });
  });
};

const check_unchanged_followers = async (user_ids) => {
  const last_check = formatISO(sub(new Date(), { minutes: 15 }));
  console.log(last_check);
  new_data = await Promise.all(
    user_ids.map((user_id) => {
      return read_last_15_minute_tweets(user_id, last_check);
    })
  );

  console.log(new_data);
  new_data.forEach((element, i) => {
    element.forEach((datapoint) => {
      console.log(datapoint);
      const { anger, joy, optimism, sadness } = datapoint["score"];
      const created_at = datapoint["created_at"];
      const record = new Record({
        user_id: user_ids[i],
        date: Date.now(),
        anger,
        joy,
        optimism,
        sadness,
      });

      record.save();
    });
  });
};

exports.initialize_new_followers = initialize_new_followers;
exports.check_unchanged_followers = check_unchanged_followers;
exports.delete_tweets_from_user = delete_tweets_from_user;
