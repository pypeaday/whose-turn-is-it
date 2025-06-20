# Whose Turn Is It?

A simple web app to determine the order of participants in an event

## Configuration

Set an environment variable `PLAYERS` to a comma separated list of people.

PLAYERS=user1,user2,user3

`uv run app/app.py` starts the uvicorn server

go to `http://localhost:8000` and click "generate order" to get a randomly shuffled list of the 3 users