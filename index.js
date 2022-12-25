const aedes = require('aedes')()
const express = require('express'); //Permanent, used for testing
const mongoose = require("mongoose");
const mqttEvents = require('./js/mqttEvents');
const config = require('./config/config')

const mqttServer = require('net').createServer(aedes.handle);
const httpServer = express(); //permanent

mongoose.connect(config.db_url, {
    useNewUrlParser: true,
    useUnifiedTopology: true
}, function(error) {
    if (error) console.log("Database connection failed!")
    else console.log("Connected to database")
});

mqttServer.listen(config.mqtt_port, function() {
    console.log('MQTT broker listening on port ', config.mqtt_port)
});

httpServer.listen(config.http_port, () => { //permanent
    console.log('Http server running on port ' + config.http_port);
});

mqttEvents.initializeMqttEvents(mqttServer, aedes);

httpServer.get('/sendMessageMqtt', (req, res) => {
    res.send('Hello World!'); //Permanent, used for testing
})