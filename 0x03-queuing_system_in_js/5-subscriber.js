// Import the Redis module
import redis from 'redis';

// Create a Redis client (subscriber)
const subscriber = redis.createClient();

// Listen for connection
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle errors
subscriber.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Subscribe to the channel
subscriber.subscribe('holberton school channel');

// Listen for messages on the subscribed channel
subscriber.on('message', (channel, message) => {
  console.log(message);

  // If message is "KILL_SERVER", unsubscribe and quit
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
