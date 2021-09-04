const express = require("express");
const router = express.Router();
const recordController = require("../controllers/recordController");
//const Record = require("../models/record");

router.get("/", (req, res) => {
  return res.send("hu");
})

router.get("/records", recordController.get_all_records);
router.get("/records/:userid", recordController.get_records);
router.post("/records", recordController.create_record);
router.delete("/records/:id", recordController.delete_record);

module.exports = router;