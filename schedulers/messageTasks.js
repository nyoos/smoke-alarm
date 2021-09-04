const { spawn } = require("child_process");

const send_warning_message = async (user_id) => {
  return new Promise((resolve, reject) => {
    let posts;
    const python = spawn("python", ["./scripts/warning_message.py", user_id]);
    python.stdout.on("data", function (data) {});
    python.on("close", (code) => {
      console.log("Warning message sent");
      resolve();
    });
  });
};

const send_warnings = async (user_ids) => {
  await Promise.all(
    user_ids.map((user_id) => {
      return send_warning_message(user_id);
    })
  );
  return;
};

const send_welcome_message = async (user_id, status) => {
  return new Promise((resolve, reject) => {
    let posts;
    const python = spawn("python", [
      "./scripts/welcome_message.py",
      user_id,
      status,
    ]);
    python.stdout.on("data", function (data) {});
    python.on("close", (code) => {
      console.log("Welcome message sent");
      resolve();
    });
  });
};

const send_welcomes = async (user_ids, trending_negative) => {
  console.log(trending_negative);
  await Promise.all(
    user_ids.map((user_id) => {
      return send_welcome_message(
        user_id,
        trending_negative.find((element) => element == user_id)
      );
    })
  );
  return;
};

exports.send_warnings = send_warnings;
exports.send_welcomes = send_welcomes;
