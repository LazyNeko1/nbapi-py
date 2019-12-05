exports.RandomNeko = function() {

 const https = require('http');

https.get('http://neko-bot.net/info/totalnekos.txt', (resp) => {
  let data = '';

  // A chunk of data has been recieved.
  resp.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received. Print out the result.
  resp.on('end', () => {
    //output: data
    low=1
    high=data
 return("http://neko-bot.net/nekos/"+Math.floor(Math.random() * (high - low + 1) + low) +".png"
   
)    
    
    
    
  });

}).on("error", (err) => {
  console.log("Error: " + err.message);
});
}
exports.RandomAnime = function() {

 const https = require('http');

https.get('http://neko-bot.net/info/totalanime.txt', (resp) => {
  let data = '';

  // A chunk of data has been recieved.
  resp.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received. Print out the result.
  resp.on('end', () => {
    //output: data
    low=1
    high=data
 return("http://neko-bot.net/anime/"+Math.floor(Math.random() * (high - low + 1) + low)+".png"
   
)    
    
    
    
  });

}).on("error", (err) => {
  console.log("Error: " + err.message);
});
}
