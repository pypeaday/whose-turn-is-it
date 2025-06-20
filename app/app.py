# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "fastapi",
#     "uvicorn",
#     "jinja2",
#     "python-dotenv",
# ]
# ///
import os
import random
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

# Load .env file for local development (optional, PLAYERS can be set directly in env)
load_dotenv()

app = FastAPI(
    title="Whose Turn Is It?",
    description="A simple web app to determine the order of participants in an event.",
    version="0.1.0"
)

templates = Jinja2Templates(directory="templates")

def get_players():
    players_str = os.getenv("PLAYERS")
    if players_str:
        # Ensure we handle potential empty strings after split if there are trailing commas or multiple commas
        return [player.strip() for player in players_str.split(',') if player.strip()]
    return []

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    players = get_players()
    players_count = len(players)
    error_message = None
    # The template already handles the case where players_count is 0
    # No explicit error message needed here unless there's a different kind of error

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "players_count": players_count,
            "error_message": error_message
        }
    )

@app.get("/generate", response_class=HTMLResponse)
async def generate_order(request: Request):
    players = get_players()
    error_message = None
    shuffled_players = []

    if not players:
        error_message = "The PLAYERS environment variable is not set or is empty. Please set it (e.g., PLAYERS=Alice,Bob,Charlie) and restart the application."
    else:
        shuffled_players = random.sample(players, len(players))
    
    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "players": shuffled_players,
            "error_message": error_message
        }
    )


if __name__ == "__main__":
    import uvicorn
    # Get host and port from environment variables or use defaults
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))
    RELOAD = os.getenv("UVICORN_RELOAD", "true").lower() == "true"

    # Check if PLAYERS is set, and provide a warning if not, as it's crucial for the app
    if not get_players():
        print("\n⚠️ WARNING: The 'PLAYERS' environment variable is not set or is empty.")
        print("Please set it for the application to function correctly.")
        print("Example: export PLAYERS=\"Alice,Bob,Charlie\"\n")

    uvicorn.run("app:app", host=HOST, port=PORT, reload=RELOAD)

# To run this app:
# 1. Ensure PLAYERS environment variable is set (e.g., export PLAYERS="Alice,Bob,Charlie")
#    or create a .env file with PLAYERS="user1,user2,user3".
# 2. If you are not using the script execution method below (python app.py):
#    - Install dependencies: pip install -r requirements.txt (or uv pip install -r requirements.txt)
#    - Run with Uvicorn: uvicorn app:app --reload --host 0.0.0.0 --port 8000
#    - Or using `uv`: uv run app.py (if PLAYERS is in .env or exported)
# 3. To run directly using Python (thanks to PEP 723 script metadata for dependencies):
#    python app.py
# 4. Open your browser to http://localhost:8000 (or the configured port)
#
# 1. Make sure you have an .env file with PLAYERS="user1,user2,user3" or set the environment variable directly.
#    Example .env file content:
#    PLAYERS=Alice,Bob,Charlie,Dave
# 2. Install dependencies: pip install -r requirements.txt (or uv pip install -r requirements.txt)
# 3. Run the server: uvicorn app:app --reload (or uv run app.py as per README)
# 4. Open your browser to http://localhost:8000