from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

PROJECT_NAME = "CrimeCase AI Studio"
VERSION = "1.0.0"

TARGET_AUDIENCE = [
    "United States",
    "United Kingdom",
    "Canada"
]

LANGUAGE = "English"

VIDEOS_PER_DAY = 2

VIDEO_STYLE = "Netflix Documentary"

VOICE = "American Male"

# ==========================
# AI Settings
# ==========================

AI_PROVIDER = "OpenRouter"

# Text Generation
TEXT_MODEL = "deepseek/deepseek-chat-v3-0324"

# Image Generation
IMAGE_MODEL = "black-forest-labs/flux-1.1-pro"

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
