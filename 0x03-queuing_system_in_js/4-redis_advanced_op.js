// Import the Redis module
import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Listen for connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Store the hash using hset
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

// Retrieve and display the hash using hgetall
client.hgetall('HolbertonSchools', (err, object) => {
  if (err) {
    console.error('Error fetching hash:', err);
  } else {
    console.log(object);
  }
});
