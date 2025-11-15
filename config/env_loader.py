import os
from dotenv import load_dotenv

BASE_ENV_FILE = ".env"

def load_environment():
    load_dotenv(BASE_ENV_FILE)
    env = os.getenv("ENV", "dev")

    env_file = f"config/environments/{env}.env"
    load_dotenv(env_file, override=True)

    return {
        "ENV": env,
        "BASE_URL": os.getenv("BASE_URL"),
        "BROWSER": os.getenv("BROWSER"),
        "HEADLESS": os.getenv("HEADLESS") == "True"
    }
