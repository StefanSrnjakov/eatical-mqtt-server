# eatical-mqtt-server

## run for dev: 
  npm install <br/>
  node index.js <br/>
  url: mqtt://localhost:3002 <br/>
  
### This server is used as mqtt broker

### For correct message you need to connect to any of this topics
   food, <br/>
   menu, <br/>
   restaurant <br/>
### Payload should be Json object stringified that contains 
   coordinates: [double] <br/>
   image: <image data> <br/>
