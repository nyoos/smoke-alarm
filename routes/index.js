const express = require("express");
var { spawn } = require("child_process");
const router = express.Router();
const recordController = require("../controllers/recordController");
const taskMaster = require("../schedulers/taskMaster");
const analyse_functionality = require("../schedulers/weeklyAnalysis");
router.get("/", (req, res) => {
  taskMaster.hourly_task();
  // analyse_functionality.analyse_single_user("1434233339733368834");
  res.send("hi");
});

router.get("/records", recordController.get_all_records);
router.get("/records/users/:userid", recordController.get_records);
router.post("/records", recordController.create_record);
router.delete("/records/:id", recordController.delete_record);

module.exports = router;
