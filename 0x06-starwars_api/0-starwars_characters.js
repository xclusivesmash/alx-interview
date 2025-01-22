#!/usr/bin/node
/* module: 0-starwars_characters
 * description: prints all characters of a Star Wars movie
 */
const request = require('request');
const movieId = process.argv[2];
const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function sendRequest (characterList, index) {
  if (characterList.length === index) {
    return;
  }
  request(characterList[index], (error, response, body) => {
    if (error) {
      // log in the error to console.
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      sendRequest(characterList, index + 1);
    }
  });
}

request(movieEndpoint, (error, response, body) => {
  if (error) {
    // log in the error to console.
    console.log(error);
  } else {
    const characterList = JSON.parse(body).characters;
    sendRequest(characterList, 0);
  }
});
