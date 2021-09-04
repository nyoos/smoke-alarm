const Record = require("../models/record");
const { body, validationResult } = require("express-validator");

exports.create_record = [
  body("user_id", "Empty userid").trim().escape(),
  
  function (req, res, next) {
    
    const errors = validationResult(req);

    if (!errors.isEmpty()) {
      res.json({
        data: req.body,
        errors: errors.array(),
      });
      return;
    }

    const { user_id, anger, joy, optimism, sadness } = req.body;

    const record = new Record({
      user_id,
      date:Date.now(),
      anger,
      joy,
      optimism,
      sadness
    });

    record.save((err)=>{
      if (err) {
        return next(err);
      }
      res.status(200).json({ msg: "post sent" });
    });
  },
];

exports.get_records = async (req, res, next) => {

  try {
    console.log(req.params);
    const user_id = req.params.userid;

    const records = await Record.find({}).where('user_id').equals(user_id);
    if (!records) {
      return res.status(404).json({ err: "records not found" });
    }
    res.status(200).json({ records });
  } catch (err) {
    console.log(err)
    next(err);
  }

}

exports.get_all_records = async (req, res, next) => {

  try {

    const records = await Record.find({});
    if (!records) {
      return res.status(404).json({ err: "records not found" });
    }
    res.status(200).json({ records });
  } catch (err) {
    console.log(err)
    next(err);
  }

}

exports.delete_record = async (req, res, next) => {

  try {
    const record = await Record.findByIdAndDelete(req.params.id.toString());
    if (!record) {
      return res.status(404).json({ err: `record with id ${req.params.id} not found` });
    }
    res.status(200).json({ msg: `record ${req.params.id} deleted sucessfully` });
  } catch (err) {
    next(err);
  }

}

