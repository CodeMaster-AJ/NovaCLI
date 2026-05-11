import requests
import sys
import time
from config import API_KEY, API_URL, MODEL, CYAN, GREEN, RED, YELLOW, RESET, BOLD


def show_typing_indicator():
    for _ in range(3):
        for dot in ["", ".", "..", "..."]:
            sys.stdout.write(f"\r{CYAN}{BOLD}NovaCLI is thinking{dot}   {RESET}")
            sys.stdout.flush()
            time.sleep(0.3)


def ask_ai(prompt):
    if not API_KEY or API_KEY == "your-api-key-here":
        return f"{RED}{BOLD}ERROR: No API key found!{RESET}\n{YELLOW}Create a .env file and set OPENROUTER_API_KEY=your_key{RESET}"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
    }

    try:
        show_typing_indicator()
        sys.stdout.write("\r" + " " * 40 + "\r")
        sys.stdout.flush()

        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()

        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"]
        else:
            return f"{YELLOW}No response from AI.{RESET}"

    except requests.exceptions.Timeout:
        return f"{RED}Request timed out. Please try again.{RESET}"
    except requests.exceptions.ConnectionError:
        return f"{RED}Network error. Check your internet connection.{RESET}"
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            return f"{RED}Invalid API key. Check your .env file.{RESET}"
        elif response.status_code == 429:
            return f"{YELLOW}Rate limited. Please wait and try again.{RESET}"
        return f"{RED}API error: {e}{RESET}"
    except Exception as e:
        return f"{RED}Unexpected error: {e}{RESET}"
