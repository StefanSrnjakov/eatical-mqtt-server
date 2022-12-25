const aedes = require('aedes')()
const express = require('express'); //Permanent, used for testing
const mqttEvents = require('./js/mqttEvents');


const httpPort = 3001; //permanent
const mqttPort = 3002;
const mqttServer = require('net').createServer(aedes.handle);
const httpServer = express(); //permanent

mqttServer.listen(mqttPort, function() {
    console.log('MQTT broker listening on port ', mqttPort)
});

httpServer.listen(httpPort, () => {
    console.log('Http server running on port ' + httpPort);
});


httpServer.get('/sendMessageMqtt', (req, res) => { //TODO
    res.send('Hello World!'); //Permanent, used for testing
})

mqttEvents.initializeMqttEvents(mqttServer, aedes);