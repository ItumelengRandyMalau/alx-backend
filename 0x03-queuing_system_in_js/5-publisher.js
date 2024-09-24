// Import the Redis module
import redis from 'redis';

// Create a Redis client (publisher)
const publisher = redis.createClient();

// Listen for connection
publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle errors
publisher.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Function to publish a message after a delay
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish('holberton school channel', message);
  }, time);
}

// Call publishMessage for each message with different time delays
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
