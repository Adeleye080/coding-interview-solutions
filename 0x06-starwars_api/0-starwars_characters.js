#!/usr/bin/node
// include request module
const request = require('request');
// Star Wars API URL to be queried
const API_URL = 'https://swapi-api.alx-tools.com/api/films';
// check if command line argument present
// if present it is assumed to be an integer
// it is then added to the url as '/api/films/:id'
// retrieve the url of the characters of the star war movie as an array
// using the retrieved array of URLs, retrieve characters name
// log all characters name to the console
if (process.argv.length > 2) {
  request(`${API_URL}/${process.argv[2]}/`, (err, res, body) => {
    if (err) {
      console.log(err);
    }
    const charsUrl = JSON.parse(body).characters;
    const charsName = charsUrl.map(
      url => new Promise((resolve, reject) => {
        request(url, (err, res, body) => {
          if (err) {
            reject(err);
          }
          resolve(JSON.parse(body).name);
        });
      })
    );
    Promise.all(charsName)
      .then(names => { console.log(names.join('\n')); })
      .catch((error) => {
        console.log(`Error: ${error}`);
      });
  });
}
