var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var BlockchainImagesSchema = new Schema({
    'timestamp': Date,
    'transaction': {},
    'prevHash': String,
    'hash': String
});

module.exports = mongoose.model('BlockchainImages', BlockchainImagesSchema);