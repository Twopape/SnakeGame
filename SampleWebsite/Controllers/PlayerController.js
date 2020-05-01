const PlayerRepo   = require('../Data/PlayerRepo');
const _playerRepo  = new PlayerRepo();
const Player       = require('../Models/Players');


exports.AddScore = async function(request, response) {

    let tempPlayerObj  = new Player( {
        "player":    request.body.player,
        "score":    request.body.score,
        "difficulty":     request.body.difficulty
    });

    let responseObject = await _playerRepo.create(tempPlayerObj);
    // No errors so save is successful.
    if(responseObject.errorMessage == "") {
        response.json({ order:responseObject.obj, errorMessage:"Success: player added"});
    }
    // There are errors. Show form the again with an error message.
    else {
        console.log("An error occured. Item not created.");
        response.json({ orders:responseObject.obj,
            errorMessage:"[Object object]."});
    }
};

exports.All = async function(request, response) {

    let players = await _playerRepo.allPlayers();
    if(players!= null) {
        response.json({players:players});
    }
    else {
        response.json({players:[]});
    }
};
