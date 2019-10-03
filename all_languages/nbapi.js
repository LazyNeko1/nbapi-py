//WILL WORK ON IN THE NEXT HOUR (10:53 AM)


//i don't know if this will work, i doubt it does /shrug
exports.RandomNeko = function() {
const https = require('https');

https.get('http://neko-bot.net/info/totalnekos.txt', (resp) => {
  let data = '';

  // A chunk of data has been recieved.
  resp.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received. Print out the result.
  resp.on('end', () => {
    return (JSON.parse(data).explanation);
  });

}).on("error", (err) => {
  console.log("Error: " + err.message);
});
}
