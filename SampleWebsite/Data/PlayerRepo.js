const Players = require('../Models/Players');


class PlayerRepo {

    // This is the constructor.
    PlayerRepo() {
    }

    async allPlayers() {
        let players = await Players.find().exec();
        return players;
    }

    async create(tempObj) {
        try {
            // Checks if model conforms to validation rules that we set in Mongoose.
            var error = await tempObj.validateSync();

            // The model is invalid. Return the object and error message.
            if(error) {
                let response = {
                    obj:          tempObj,
                    errorMessage: error.message };

                return response; // Exit if the model is invalid.
            }

            // Model is not invalid so save it.
            const result = await tempObj.save();

            // Success! Return the model and no error message needed.
            let response = {
                obj:          result,
                errorMessage: "" };

            return response;
        }
            //  Error occurred during the save(). Return orginal model and error message.
        catch (err) {
            let response = {
                obj:          tempObj,
                errorMessage: err.message };

            return  response;
        }
    }
}

module.exports = PlayerRepo;
