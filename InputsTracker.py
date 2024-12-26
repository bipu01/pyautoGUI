from pynput import mouse, keyboard
from datetime import datetime
import json
import threading
import os


class InputTracker:
    def __init__(self):
        self.events = []
        self.running = True
        self.output_file = "input_events.json"
        # Lock for thread-safe writing
        self.lock = threading.Lock()

    def on_press(self, key):
        try:
            # Handle regular characters
            key_char = key.char
        except AttributeError:
            # Handle special keys
            key_char = str(key)

        event_data = {
            "type": "keyboard_press",
            "key": key_char,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        }

        with self.lock:
            self.events.append(event_data)
            self.save_events()

        print(f"Key pressed: {key_char}")

    def on_click(self, x, y, button, pressed):
        if pressed:  # Only track press events, not releases
            event_data = {
                "type": "mouse_click",
                "x": x,
                "y": y,
                "button": str(button),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            }

            with self.lock:
                self.events.append(event_data)
                self.save_events()

            print(f"Mouse clicked: {button} at ({x}, {y})")

    def save_events(self):
        with open(self.output_file, 'w') as f:
            json.dump({"events": self.events}, f, indent=2)

    def start(self):
        print("Input tracking started. Press Ctrl+C to stop.")

        # Start keyboard listener in a separate thread
        keyboard_listener = keyboard.Listener(on_press=self.on_press)
        keyboard_listener.start()

        # Start mouse listener in a separate thread
        mouse_listener = mouse.Listener(on_click=self.on_click)
        mouse_listener.start()

        try:
            # Keep the main thread alive
            keyboard_listener.join()
            mouse_listener.join()
        except KeyboardInterrupt:
            print("\nInput tracking stopped.")
            self.save_events()


if __name__ == "__main__":
    tracker = InputTracker()
    tracker.start()