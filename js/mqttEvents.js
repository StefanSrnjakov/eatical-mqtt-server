const topics = require("./topics")
const Transactions = require('../models/BlockchainImagesModel')

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
        if (client) {
            console.log(`[MESSAGE_PUBLISHED] Client ${(client ? client.id : 'BROKER_' + aedes.id)} has published message on ${packet.topic} to broker ${aedes.id}`)
        }
        if (packet.topic == topics.FOOD_TOPIC || packet.topic == topics.MENU_TOPIC || packet.topic == topics.RESTAURANT_TOPIC) {
            handleMessageOnTopic(packet, client);
        }
    })
}

function handleMessageOnTopic(packet, client) {

}
module.exports = { initializeMqttEvents }