var q = require('q');

// Function to get current location from html5 geolocation API
// Returns a promise object
// Saves the current location to session storage
module.exports.getCurrentLocation = function () {
    // Check if current location is saved in sessionStorage
    var currentLocation =  sessionStorage.currentLocation;
    if(currentLocation) {
        return q.resolve(JSON.parse(currentLocation));
    }

    var defer = q.defer();
    // check if browser supports html5 location api
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            currentLocation = {
                'lat': position.coords.latitude,
                'lon': position.coords.longitude
            };

            // save to sessionStorage for future calls
            sessionStorage.currentLocation = JSON.stringify(currentLocation);

            defer.resolve(currentLocation);
        }, function () {
            // user rejected getting current location
            defer.reject(new Error('permission error'));
        });
    } else {
        // browser doesn't support html5 location api
        defer.reject(new Error('location error'));
    }

    return defer.promise;
};
