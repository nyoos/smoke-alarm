const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const FollowerSchema = new Schema({
  user_id: { type:String, required: true},
  date: {default: Date.now(), type: Date},
});

const Follower = mongoose.model("Follower", FollowerSchema);
module.exports = Follower;