import { createClient } from 'redis';
const client = createClient();

// Connect to Redis
client.on('connect', function() {
    console.log("Redis client connected to the server");
});

client.on('error', function(err) {
    console.log("Redis client not connected to the server: " + err.message);
});
