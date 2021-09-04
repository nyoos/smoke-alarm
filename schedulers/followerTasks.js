const Follower = require("../models/follower");
const { spawn } = require("child_process");
var JSONbigString = require("json-bigint")({ storeAsString: true });

const get_followers_from_db = async () => {
  const followers = await Follower.find({});
  return followers.map((element) => {
    return element["user_id"];
  });
};

const get_followers_from_twitter = async () => {
  return new Promise((resolve, reject) => {
    let followers;
    const python = spawn("python", ["./scripts/read_followers.py"]);
    python.stdout.on("data", function (data) {
      console.log("Reading twitter followers..");
      followers = data.toString();
      followers = JSONbigString.parse(followers);
    });
    python.on("close", (code) => {
      console.log(`child process close all stdio with code ${code}`);
      // console.log(dataToSend['name']);
      // send data to browser
      resolve(followers);
    });
  });
};

const add_followers = async (ids) => {
  return Promise.all(
    ids.map((element) => {
      const follower = new Follower({
        user_id: element,
        date: Date.now(),
      });

      return new Promise((resolve, reject) => {
        follower.save((err) => {
          if (err) {
            reject();
          } else resolve();
        });
      });
    })
  );
};

const delete_followers = async (ids) => {
  return Promise.all(
    ids.map((element) => {
      return Follower.deleteMany({ user_id: element });
    })
  );
};

const check_for_follower_updates = async () => {
  [db_followers, twitter_followers] = await Promise.all([
    get_followers_from_db(),
    get_followers_from_twitter(),
  ]);
  new_followers = twitter_followers.filter(
    (element) => !db_followers.find((db) => db == element)
  );
  lost_followers = db_followers.filter(
    (element) => !twitter_followers.find((twitter) => twitter == element)
  );

  unchanged_followers = db_followers.filter((element) =>
    twitter_followers.find((twitter) => twitter == element)
  );
  return { new_followers, lost_followers, unchanged_followers };
};

exports.add_followers = add_followers;
exports.delete_followers = delete_followers;
exports.check_for_follower_updates = check_for_follower_updates;
exports.get_followers_from_db = get_followers_from_db;
