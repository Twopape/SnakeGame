var mongoose         = require('mongoose');

var PlayerSchema    = mongoose.Schema({
        // The _id property serves as the primary key. If you don't include it
        // the it is added automatically. However, you can add it in if you
        // want to manually include it when creating an object.

        // _id property is created by default when data is inserted.

        player:    {"type" : "String", required: true},
        score: {"type" : Number, required: true, min:0},
        difficulty: {"type" : "String",  required: true, enum: ['Easy', 'Medium', 'Hard', 'MJ']}

    },
    {
        versionKey: false,
    });
var Player    = mongoose.model('Players', PlayerSchema);
module.exports = Player;
