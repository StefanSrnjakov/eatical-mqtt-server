var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var BlockModel = new Schema({
    'timestamp': Date,
    'coordinates': [],
    'transaction': {},
    'prevHash': {
        type: "String",
        required: false
    },
    'hash': String
}, { collection: 'blocks' });

module.exports = mongoose.model('BlockModel', BlockModel);