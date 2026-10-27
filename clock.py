"""A simple digital clock built with Python's standard library."""

from datetime import datetime
import tkinter as tk


class DigitalClock(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Digital Clock")
        self.geometry("420x180")
        self.resizable(False, False)
        self.configure(background="#101820")

        self.time_label = tk.Label(
            self,
            font=("Segoe UI", 56, "bold"),
            foreground="#00d1b2",
            background="#101820",
        )
        self.time_label.pack(expand=True, pady=(18, 0))

        self.date_label = tk.Label(
            self,
            font=("Segoe UI", 14),
            foreground="#c5d0dc",
            background="#101820",
        )
        self.date_label.pack(pady=(0, 20))

        self._update_clock()

    def _update_clock(self) -> None:
        now = datetime.now()
        self.time_label.config(text=now.strftime("%H:%M:%S"))
        self.date_label.config(text=now.strftime("%A, %B %d, %Y"))
        self.after(1000, self._update_clock)


if __name__ == "__main__":
    DigitalClock().mainloop()