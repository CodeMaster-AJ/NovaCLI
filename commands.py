import os
import datetime
import random
from config import (
    CYAN, GREEN, YELLOW, RED, MAGENTA, BLUE, WHITE, RESET, BOLD,
    PROMPT_COLOR, INFO_COLOR, SUCCESS_COLOR, WARN_COLOR, ERROR_COLOR,
    HEADER_COLOR, SEPARATOR, SUB_SEPARATOR
)
from ai_module import ask_ai


JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
    "Why did the developer go broke? Because he used up all his cache.",
    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
    "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
    "What's a computer's favorite snack? Microchips!",
    "Why do Python programmers wear glasses? Because they can't C#.",
    "I told my computer I needed a break, now it won't stop sending me vacation ads.",
    "Why did the programmer quit his job? Because he didn't get arrays.",
    "There are 10 types of people in the world: those who understand binary and those who don't.",
]


def cmd_help():
    print(f"\n{SEPARATOR}")
    print(f"{HEADER_COLOR}{'NOVACLI COMMANDS':^60}{RESET}")
    print(f"{SEPARATOR}")
    commands = [
        ("help", "Show this help menu"),
        ("time", "Display current time"),
        ("date", "Display current date"),
        ("calc", "Run a quick calculator"),
        ("ai <text>", "Ask NovaCLI AI anything"),
        ("notes", "Open notes manager"),
        ("joke", "Get a random programming joke"),
        ("history", "Show command history"),
        ("clear", "Clear the terminal screen"),
        ("exit", "Exit NovaCLI Assistant"),
    ]
    for cmd, desc in commands:
        print(f"  {CYAN}{BOLD}{cmd:<15}{RESET} {WHITE}{desc}{RESET}")
    print(f"{SEPARATOR}\n")


def cmd_time():
    now = datetime.datetime.now()
    print(f"\n{SUB_SEPARATOR}")
    print(f"{INFO_COLOR}Current Time: {WHITE}{BOLD}{now.strftime('%I:%M:%S %p')}{RESET}")
    print(f"{SUB_SEPARATOR}\n")


def cmd_date():
    today = datetime.date.today()
    print(f"\n{SUB_SEPARATOR}")
    print(f"{INFO_COLOR}Current Date: {WHITE}{BOLD}{today.strftime('%A, %B %d, %Y')}{RESET}")
    print(f"{SUB_SEPARATOR}\n")


def cmd_calc():
    print(f"\n{SEPARATOR}")
    print(f"{HEADER_COLOR}{'NOVACLI CALCULATOR':^60}{RESET}")
    print(f"{SEPARATOR}")
    print(f"{YELLOW}Type your expression (e.g. 2 + 2 * 3){RESET}")
    print(f"{YELLOW}Type 'x' to go back.{RESET}")
    print(f"{SEPARATOR}")
    while True:
        try:
            expr = input(f"\n{PROMPT_COLOR}calc> {RESET}").strip()
            if expr.lower() == "x":
                print(f"{SUCCESS_COLOR}Exiting calculator.{RESET}\n")
                break
            if not expr:
                continue
            result = eval(expr, {"__builtins__": {}}, {})
            print(f"{GREEN}{BOLD}Result: {WHITE}{BOLD}{result}{RESET}")
        except ZeroDivisionError:
            print(f"{ERROR_COLOR}Cannot divide by zero!{RESET}")
        except Exception:
            print(f"{ERROR_COLOR}Invalid expression. Try again.{RESET}")


def cmd_ai(text):
    if not text:
        print(f"\n{YELLOW}Usage: ai <your question>{RESET}")
        print(f"{YELLOW}Example: ai explain python lists{RESET}\n")
        return
    print(f"\n{SUB_SEPARATOR}")
    print(f"{INFO_COLOR}You asked: {WHITE}{BOLD}{text}{RESET}")
    print(f"{SUB_SEPARATOR}\n")
    response = ask_ai(text)
    print(f"{CYAN}{BOLD}NovaCLI:{RESET}")
    print(f"{WHITE}{response}{RESET}\n")


def cmd_notes():
    NOTES_FILE = "notes.txt"
    print(f"\n{SEPARATOR}")
    print(f"{HEADER_COLOR}{'NOVACLI NOTES MANAGER':^60}{RESET}")
    print(f"{SEPARATOR}")
    print(f"{YELLOW}Commands: add <note> | list | delete <number> | x to exit{RESET}")
    print(f"{SEPARATOR}")
    while True:
        try:
            inp = input(f"\n{PROMPT_COLOR}notes> {RESET}").strip()
            if inp.lower() == "x":
                print(f"{SUCCESS_COLOR}Exiting notes.{RESET}\n")
                break
            if not inp:
                continue
            parts = inp.split(maxsplit=1)
            action = parts[0].lower()

            if action == "add" and len(parts) > 1:
                with open(NOTES_FILE, "a") as f:
                    f.write(parts[1] + "\n")
                print(f"{SUCCESS_COLOR}Note added!{RESET}")

            elif action == "list":
                if not os.path.exists(NOTES_FILE):
                    print(f"{YELLOW}No notes yet.{RESET}")
                    continue
                with open(NOTES_FILE, "r") as f:
                    notes = f.readlines()
                if not notes:
                    print(f"{YELLOW}No notes yet.{RESET}")
                else:
                    print(f"\n{BLUE}{'─'*40}{RESET}")
                    for i, note in enumerate(notes, 1):
                        print(f"  {CYAN}{i}.{RESET} {WHITE}{note.strip()}{RESET}")
                    print(f"{BLUE}{'─'*40}{RESET}")

            elif action == "delete" and len(parts) > 1:
                if not os.path.exists(NOTES_FILE):
                    print(f"{YELLOW}No notes to delete.{RESET}")
                    continue
                with open(NOTES_FILE, "r") as f:
                    notes = f.readlines()
                try:
                    idx = int(parts[1]) - 1
                    if 0 <= idx < len(notes):
                        removed = notes.pop(idx).strip()
                        with open(NOTES_FILE, "w") as f:
                            f.writelines(notes)
                        print(f"{SUCCESS_COLOR}Deleted: {removed}{RESET}")
                    else:
                        print(f"{ERROR_COLOR}Invalid note number.{RESET}")
                except ValueError:
                    print(f"{ERROR_COLOR}Provide a valid number.{RESET}")
            else:
                print(f"{YELLOW}Usage: add <note> | list | delete <number>{RESET}")
        except Exception as e:
            print(f"{ERROR_COLOR}Error: {e}{RESET}")


def cmd_joke():
    joke = random.choice(JOKES)
    print(f"\n{SUB_SEPARATOR}")
    print(f"{YELLOW}{BOLD}🤖 Dev Joke:{RESET}")
    print(f"{WHITE}{BOLD}{joke}{RESET}")
    print(f"{SUB_SEPARATOR}\n")


def cmd_history():
    HISTORY_FILE = "history.txt"
    if not os.path.exists(HISTORY_FILE):
        print(f"\n{YELLOW}No command history yet.{RESET}\n")
        return
    with open(HISTORY_FILE, "r") as f:
        lines = f.readlines()
    if not lines:
        print(f"\n{YELLOW}No command history yet.{RESET}\n")
        return
    print(f"\n{SEPARATOR}")
    print(f"{HEADER_COLOR}{'COMMAND HISTORY':^60}{RESET}")
    print(f"{SEPARATOR}")
    for i, line in enumerate(lines[-15:], 1):
        print(f"  {CYAN}{i:>2}.{RESET} {WHITE}{line.strip()}{RESET}")
    print(f"{SEPARATOR}\n")


def cmd_clear():
    os.system("cls" if os.name == "nt" else "clear")


def cmd_exit():
    print(f"\n{YELLOW}Shutting down NovaCLI...{RESET}")
    print(f"{GREEN}{BOLD}Goodbye, developer!{RESET}\n")
    exit()
