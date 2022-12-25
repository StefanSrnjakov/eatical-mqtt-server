# eatical-mqtt-server

## run for dev: 
  npm install <br/>
  node index.js <br/>
  url: http://localhost:3002 <br/>
  
## This server is used as mqtt broker

## For successuful message you need to connect to any of this topics
   food,
   menu,
   restaurant
## Payload should be Json object stringified that contains 
   coordinates: [double]
   image: <image data>
