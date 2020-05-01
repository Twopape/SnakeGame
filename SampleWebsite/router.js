
var PlayerController= require('./Controllers/PlayerController')
const cors = require('cors');

// Routes
module.exports = function(app){

    app.post('/Player/AddScore', cors(), PlayerController.AddScore);
    app.get('/Player/All', cors(), PlayerController.All);

};
