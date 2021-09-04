const followerTasks = require("./followerTasks");
const tweetTasks = require("./tweetTasks");
const weeklyAnalysis = require("./weeklyAnalysis");
const messageTasks = require("./messageTasks");

const hourly_task = async () => {
  const { new_followers, lost_followers, unchanged_followers } =
    await followerTasks.check_for_follower_updates();
  await followerTasks.delete_followers(lost_followers);
  await tweetTasks.delete_tweets_from_user(lost_followers);
  console.log(" Old Followers deleted");
  await tweetTasks.initialize_new_followers(new_followers);
  console.log("New followers initialized");
  await followerTasks.add_followers(new_followers);
  console.log("New followers added");
  await tweetTasks.check_unchanged_followers(unchanged_followers);
  console.log("Old followers updated.");
  const toNotify = await weeklyAnalysis.analyse(new_followers);
  messageTasks.send_welcomes(new_followers, toNotify);
};

const weekly_task = async () => {
  const followers = await followerTasks.get_followers_from_db();
  const toNotify = await weeklyAnalysis.analyse(followers);
  messageTasks.send_warnings(toNotify);
};

exports.hourly_task = hourly_task;
exports.weekly_task = weekly_task;
