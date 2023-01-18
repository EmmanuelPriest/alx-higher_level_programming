#!/usr/bin/node
/*
Script that computes the number of tasks completed by user id
*/

// Importing the request module
const request = require('request');

// Creating the first user API URL argument based on index
const userApiUrl = process.argv[2];

// Creating empty key-value objects that will hold the completed tasks
const userCompletedTask = {};

// Using the request module to get user API URL
request.get(userApiUrl, (error, res, body) => {
  if (error) {
    return console.error(error);
  }
  const tasks = JSON.parse(body); // Creating JSON file
  tasks.forEach((task) => {
    if (task.completed) {
      if (!userCompletedTask[task.userId]) {
        userCompletedTask[task.userId] = 0;
      }
      userCompletedTask[task.userId] += 1;
    }
  });
  console.log(userCompletedTask); // Displaying the task completed by the user
});
