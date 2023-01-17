#!/usr/bin/node
/*
Script that computes the number of tasks completed by user id
*/

const request = require('request');
const userApiUrl = process.argv[2];

const userCompletedTask = {};

request(userApiUrl, (error, res, body) => {
  if (error) {
    return console.error(error);
  }
  const tasks = JSON.parse(body);
  tasks.forEach((task) => {
    if (task.completed) {
      if (!userCompletedTask[task.userId]) {
        userCompletedTask[task.userId] = 0;
      }
      userCompletedTask[task.userId] += 1;
    }
  });

  for (const userId in userCompletedTask) {
    console.log(`'${userId}': ${userCompletedTask[userId]}`);
  }
});
