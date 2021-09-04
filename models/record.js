const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const RecordSchema = new Schema({
  user_id: { type:String, required: true},
  date: {default: Date.now(), type: Date},
  anger: {default: NaN, type: Number},
  joy: {default: NaN, type: Number},
  optimism: {defualt: NaN, type: Number},
  sadness: {default: NaN, type: Number}
});

const Record = mongoose.model("Record", RecordSchema);
module.exports = Record;