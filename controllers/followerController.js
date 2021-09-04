const Follower = require("../models/follower");
const { body, validationResult } = require("express-validator");

exports.create_follower = [
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

    const follower = new Follower({
      user_id,
      date: Date.now(),
    });

    follower.save((err) => {
      if (err) {
        return next(err);
      }
      res.status(200).json({ msg: "follower added" });
    });
  },
];

exports.get_all_followers = async (req, res, next) => {
  try {
    const followers = await Follower.find({});
    if (!followers) {
      return res.status(404).json({ err: "followers not found" });
    }
    res.status(200).json({ followers });
  } catch (err) {
    console.log(err);
    next(err);
  }
};

exports.delete_follower = async (req, res, next) => {
  try {
    const follower = await Follower.deleteMany(req.params.id.toString());
    if (!follower) {
      return res
        .status(404)
        .json({ err: `follower with id ${req.params.id} not found` });
    }
    res
      .status(200)
      .json({ msg: `follower ${req.params.id} deleted sucessfully` });
  } catch (err) {
    next(err);
  }
};
