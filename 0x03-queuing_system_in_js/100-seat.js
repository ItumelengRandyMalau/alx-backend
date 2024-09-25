// Import required modules
const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const kue = require('kue');

// Set up Redis client and promisify methods
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Create an Express server
const app = express();
const port = 1245;

// Initialize available seats and reservation flag
let reservationEnabled = true;

// Function to reserve a seat (set the number of available seats)
async function reserveSeat(number) {
    await setAsync('available_seats', number);
}

// Function to get the current number of available seats
async function getCurrentAvailableSeats() {
    const seats = await getAsync('available_seats');
    return seats;
}

// Initialize available seats to 50 on server start
reserveSeat(50);

// Create a Kue queue for handling seat reservations
const queue = kue.createQueue();

// Route: GET /available_seats
// Returns the current number of available seats
app.get('/available_seats', async (req, res) => {
    const availableSeats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats: availableSeats });
});

// Route: GET /reserve_seat
// Reserves a seat by creating and queuing a job
app.get('/reserve_seat', (req, res) => {
    if (!reservationEnabled) {
        return res.json({ status: "Reservation are blocked" });
    }

    const job = queue.create('reserve_seat').save((err) => {
        if (err) {
            return res.json({ status: "Reservation failed" });
        }
        res.json({ status: "Reservation in process" });
    });

    job.on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`);
    });

    job.on('failed', (errorMessage) => {
        console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
    });
});

// Route: GET /process
// Processes the seat reservation queue
app.get('/process', (req, res) => {
    res.json({ status: 'Queue processing' });

    queue.process('reserve_seat', async (job, done) => {
        let availableSeats = await getCurrentAvailableSeats();
        availableSeats = parseInt(availableSeats);

        if (availableSeats > 0) {
            await reserveSeat(availableSeats - 1);
            if (availableSeats - 1 === 0) {
                reservationEnabled = false;
            }
            done();  // Job succeeded
        } else {
            done(new Error('Not enough seats available'));  // Job failed
        }
    });
});

// Start the Express server
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
