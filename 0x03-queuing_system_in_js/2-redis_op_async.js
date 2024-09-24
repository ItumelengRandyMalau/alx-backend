import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

// Connect to Redis
client.on('connect', function () {
    console.log("Redis client connected to the server");
});

client.on('error', function (err) {
    console.log("Redis client not connected to the server: " + err.message);
});

// Promisify the Redis 'get' method
const getAsync = promisify(client.get).bind(client);

// Function to set a new school
function setNewSchool(SchoolName, value) {
    client.set(SchoolName, value, (err, reply) => { // Define the callback inline
        if (err) {
            console.log("Error setting value:", err);
        } else {
            console.log("Reply:", reply);
        }
    });
}

// Async function to display the school value
async function displaySchoolValue(SchoolName) {
    try {
        const value = await getAsync(SchoolName); // Get value asynchronously
        console.log(value); // Log the value retrieved from Redis
    } catch (error) {
        console.error("Error retrieving value:", error);
    }
}

// Calls to the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
