import json
import os
import sys

PROGRESS_FILE = 'progress.json'
TOTAL_DAYS = 100

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            try:
                data = json.load(f)
                return set(data.get('completed_days', []))
            except json.JSONDecodeError:
                # Reset the file if it's corrupted
                save_progress(set())
                return set()
    return set()

def save_progress(days):
    with open(PROGRESS_FILE, 'w') as f:
        json.dump({'completed_days': sorted(days)}, f, indent=2)

def print_progress(days):
    completed = len(days)
    percent = completed / TOTAL_DAYS * 100
    print(f"Completed {completed}/{TOTAL_DAYS} days ({percent:.1f}%):")
    progress_bar = '[' + '#' * int(percent // 2) + ' ' * (50 - int(percent // 2)) + ']'
    print(progress_bar)

def main():
    days = load_progress()

    if len(sys.argv) > 1:
        try:
            day = int(sys.argv[1])
            if day < 1 or day > TOTAL_DAYS:
                print(f"Day must be between 1 and {TOTAL_DAYS}.")
                return
            days.add(day)
            save_progress(days)
            print(f"Marked day {day} as completed.")
        except ValueError:
            print("Please provide a valid day number.")
            return

    print_progress(days)

if __name__ == '__main__':
    main()
