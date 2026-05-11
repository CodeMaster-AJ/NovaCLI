import sys
import time
from config import (
    CYAN, GREEN, YELLOW, RED, MAGENTA, BLUE, WHITE, RESET, BOLD,
    PROMPT_COLOR, INFO_COLOR, SUCCESS_COLOR, WARN_COLOR, ERROR_COLOR,
    HEADER_COLOR, SEPARATOR
)
from commands import (
    cmd_help, cmd_time, cmd_date, cmd_calc,
    cmd_ai, cmd_notes, cmd_joke, cmd_history,
    cmd_clear, cmd_exit
)


BANNER_TEXT = "NovaCLI"
TAGLINE = "Your Terminal AI Assistant"

COMMANDS = {
    "help": cmd_help,
    "time": cmd_time,
    "date": cmd_date,
    "calc": cmd_calc,
    "ai": cmd_ai,
    "notes": cmd_notes,
    "joke": cmd_joke,
    "history": cmd_history,
    "clear": cmd_clear,
    "exit": cmd_exit,
}


def show_banner():
    try:
        import pyfiglet
        banner = pyfiglet.figlet_format(BANNER_TEXT, font="slant")
        print(f"{CYAN}{banner}{RESET}")
    except ImportError:
        print(f"{CYAN}{'='*40}{RESET}")
        print(f"{HEADER_COLOR}{'NovaCLI Assistant':^40}{RESET}")
        print(f"{CYAN}{'='*40}{RESET}")
    print(f"{BLUE}{BOLD}{TAGLINE:^40}{RESET}")
    print(f"{GREEN}{'v1.0.0':^40}{RESET}")
    print(f"{SEPARATOR}\n")


def loading_animation():
    frames = ["■□□□□□□□□□", "■■□□□□□□□□", "■■■□□□□□□□", "■■■■□□□□□□",
              "■■■■■□□□□□", "■■■■■■□□□□", "■■■■■■■□□□", "■■■■■■■■□□",
              "■■■■■■■■■□", "■■■■■■■■■■"]
    for frame in frames:
        sys.stdout.write(f"\r{HEADER_COLOR}Starting NovaCLI {CYAN}{frame}{RESET}")
        sys.stdout.flush()
        time.sleep(0.08)
    sys.stdout.write("\r" + " " * 50 + "\r")
    sys.stdout.flush()


def save_history(command):
    with open("history.txt", "a") as f:
        f.write(command + "\n")


def main():
    loading_animation()
    show_banner()

    print(f"{INFO_COLOR}Type '{CYAN}{BOLD}help{INFO_COLOR}' to see available commands.{RESET}")
    print(f"{INFO_COLOR}Type '{CYAN}{BOLD}exit{INFO_COLOR}' to quit.{RESET}\n")

    while True:
        try:
            raw = input(f"{PROMPT_COLOR}nova> {RESET}").strip()
            if not raw:
                continue

            parts = raw.split(maxsplit=1)
            command = parts[0].lower()
            argument = parts[1] if len(parts) > 1 else ""

            save_history(raw)

            if command == "ai":
                cmd_ai(argument)
            elif command in COMMANDS:
                COMMANDS[command]()

            else:
                print(f"\n{WARN_COLOR}Unknown command: '{command}'{RESET}")
                print(f"{YELLOW}Type '{CYAN}{BOLD}help{YELLOW}' to see available commands.{RESET}\n")

        except KeyboardInterrupt:
            print(f"\n\n{YELLOW}Use '{CYAN}{BOLD}exit{YELLOW}' to quit gracefully.{RESET}\n")
        except EOFError:
            cmd_exit()


if __name__ == "__main__":
    main()
