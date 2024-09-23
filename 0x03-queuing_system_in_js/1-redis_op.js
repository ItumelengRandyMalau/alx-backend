import { createClient } from 'redis';

const client = createClient();

// Connect to Redis
client.on('connect', function() {
    console.log("Redis client connected to the server");
});

client.on('error', function(err) {
    console.log("Redis client not connected to the server: " + err.message);
});

function setNewSchool(SchoolName, value) {
    client.set(SchoolName, value, (err, reply) => {
        if (err) {
            console.error("Error setting value: ", err);
        } else {
            console.log("Reply: ", reply);  // Should print "OK"
        }
    });
}

function displaySchoolValue(SchoolName) {
    client.get(SchoolName, (err, value) => {
        if (err) {
            console.error("Error getting value: ", err);
        } else {
            console.log(value);  // Should log the value of the key
        }
    });
}

// Call functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
