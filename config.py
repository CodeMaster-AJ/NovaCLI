import os
from pathlib import Path
from dotenv import load_dotenv
from colorama import Fore, Back, Style, init

init(autoreset=True)

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "nvidia/nemotron-3-super-120b-a12b:free"

CYAN = Fore.CYAN
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RED = Fore.RED
MAGENTA = Fore.MAGENTA
BLUE = Fore.BLUE
WHITE = Fore.WHITE
RESET = Style.RESET_ALL
BOLD = Style.BRIGHT

PROMPT_COLOR = CYAN + BOLD
INFO_COLOR = BLUE + BOLD
SUCCESS_COLOR = GREEN + BOLD
WARN_COLOR = YELLOW + BOLD
ERROR_COLOR = RED + BOLD
HEADER_COLOR = MAGENTA + BOLD

SEPARATOR = f"{CYAN}{'='*60}{RESET}"
SUB_SEPARATOR = f"{BLUE}{'-'*40}{RESET}"
