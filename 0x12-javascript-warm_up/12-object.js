#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

/* const elementIndex = myObject.findIndex((obj => obj.type === 'object'));
myObject[elementIndex].value = 89; */
myObject['value'] = 89;
console.log(myObject);
