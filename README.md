# Whose Turn Is It?

A simple web app to determine the order of participants in an event

## Configuration

Set an environment variable `PLAYERS` to a comma separated list of people.

PLAYERS=user1,user2,user3

`uv run app/app.py` starts the uvicorn server

go to `http://localhost:8000` and click "generate order" to get a randomly shuffled list of the 3 users

# Examples

![20250620011931_fdb87783.png](https://cdn.statically.io/gh/pypeaday/images.pype.dev/main/blog-media/20250620011931_fdb87783.png)

After cliking "Generate"

![20250620012026_f1bb8be8.png](https://cdn.statically.io/gh/pypeaday/images.pype.dev/main/blog-media/20250620012026_f1bb8be8.png)