const topics = require("./topics")
const BlockSchema = require('../models/BlockModel')
const md5 = require("blueimp-md5");

function initializeMqttEvents(mqttServer, aedes) {

    aedes.on('client', function(client) {
        console.log(`[CLIENT_CONNECTED] Client ${(client ? client.id : client)} connected to broker ${aedes.id}`)
    })

    aedes.on('clientDisconnect', function(client) {
        console.log(`[CLIENT_DISCONNECTED] Client ${(client ? client.id : client)} disconnected from the broker ${aedes.id}`)
    })

    aedes.on('subscribe', function(subscriptions, client) {
        console.log(`[TOPIC_SUBSCRIBED] Client ${(client ? client.id : client)} subscribed to topics: ${subscriptions.map(s => s.topic).join(',')} on broker ${aedes.id}`)
    })

    aedes.on('unsubscribe', function(subscriptions, client) {
        console.log(`[TOPIC_UNSUBSCRIBED] Client ${(client ? client.id : client)} unsubscribed to topics: ${subscriptions.join(',')} from broker ${aedes.id}`)
    })

    aedes.on('publish', async function(packet, client) {
        if (!client) return;

        console.log('[MESSAGE_PUBLISHED] Client ' + client.id + ' has published message on ${packet.topic} to broker ${aedes.id}')
        if (packet.topic == topics.FOOD_TOPIC || packet.topic == topics.MENU_TOPIC || packet.topic == topics.RESTAURANT_TOPIC) {
            handleMessageOnTopic(packet, client);
        }
    })
}
/* in payload needs to be sent
{ 
    coordinates:[double, double] 
    image: <we will choose later>
}*/
async function handleMessageOnTopic(packet, client) {
    const username = packet.username;
    const topic = packet.topic;
    const timestamp = new Date();

    const payload = JSON.parse(packet.payload.toString());
    const coordinates = payload.coordinates;
    const imgPath = payload.image; //TODO get binary image, save it and get path

    const output = await BlockSchema.find().sort({ 'timestamp': -1 });
    if (!output) return;

    const prevHash = output.length > 0 ? output[0].hash : undefined;
    const hash = md5(username + topic + timestamp.toString() + JSON.stringify(coordinates) + imgPath + username);

    const newBlock = new BlockSchema({
        timestamp: timestamp,
        coordinates: coordinates,
        transaction: {
            user: username,
            imgPath: imgPath,
            type: topic
        },
        prevHash: prevHash,
        hash: hash
    })
    const output2 = await newBlock.save();
    if (output2) {
        console.log("[BLOCK_ADDED]");
    }
}
module.exports = { initializeMqttEvents }