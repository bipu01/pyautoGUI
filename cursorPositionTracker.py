import win32api
import time


def get_cursor_pos():
    return win32api.GetCursorPos()


def track_cursor():
    last_pos = get_cursor_pos()
    print("Cursor tracking started. Press Ctrl+C to stop.")
    print(f"Current position: {last_pos}")

    try:
        while True:
            current_pos = get_cursor_pos()

            # Only print if position has changed
            if current_pos != last_pos:
                print(f"Current position: {current_pos}")
                last_pos = current_pos

            # Small sleep to prevent high CPU usage
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("\nCursor tracking stopped.")


if __name__ == "__main__":
    track_cursor()