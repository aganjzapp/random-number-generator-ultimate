import tkinter as tk
import random
import time


class RandomNumberGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Random Number Generator")
        self.geometry("400x400")

        self.number_label = tk.Label(self, text="", font=("Arial", 30))
        self.number_label.pack(pady=5)

        count_frame = tk.Frame(self)
        count_frame.pack(pady=5)
        self.countdown_label = tk.Label(count_frame, text="", font=("Arial", 20))
        self.countdown_label.pack(side=tk.LEFT)
        self.interval_entry = tk.Entry(count_frame, font=("Arial", 14), width=3)
        self.interval_entry.pack(side=tk.LEFT)

        seed = hash(int(time.time()))  # Change this seed value to your desired value
        random.seed(seed)

        self.update_random_number()  # Initial random number
        self.auto_update_interval = 3000  # in milliseconds (3 seconds)
        self.remaining_time = 3
        self.auto_update_random_number
        self.auto_update_enabled = True

        self.toggle_button = tk.Checkbutton(
            self, text="pause", command=self.toggle_auto_update
        )
        self.toggle_button.pack(pady=5)

        range_frame = tk.Frame(self)
        range_frame.pack(pady=5)

        self.start_range_label = tk.Label(range_frame, text="min:", font=("Arial", 14))
        self.start_range_label.pack(side=tk.LEFT)
        self.start_range_entry = tk.Entry(range_frame, font=("Arial", 14), width=7)
        self.start_range_entry.pack(side=tk.LEFT)

        self.end_range_label = tk.Label(range_frame, text="max:", font=("Arial", 14))
        self.end_range_label.pack(side=tk.LEFT)

        self.end_range_entry = tk.Entry(range_frame, font=("Arial", 14), width=7)
        self.end_range_entry.pack(side=tk.LEFT)
        self.update_random_number()  # Initial random number

        self.auto_update_random_number()
        self.manual_update_button = tk.Button(
            self, text="Update", command=self.update_random_number
        )
        self.manual_update_button.pack(pady=5)

    def update_random_number(self, event=None):
        start, end = 1, 100
        try:
            start1 = self.start_range_entry.get()
            end1 = self.end_range_entry.get()
            start, end = int(start1), int(end1)
        except:
            print("err")

        random_number = random.randint(start, end)
        self.number_label.config(text=str(random_number))

    def toggle_auto_update(self):
        self.auto_update_enabled = not self.auto_update_enabled

    def auto_update_random_number(self):
        remain = 3
        try:
            remain = int(self.interval_entry.get()) - 1
        except:
            print("no interval")
        if self.auto_update_enabled:
            self.countdown_label.config(text=f"countdown:{self.remaining_time}")
            self.remaining_time -= 1
            if self.remaining_time == -1:
                self.update_random_number()
                self.remaining_time = remain  # Convert to seconds
        self.after(1000, self.auto_update_random_number)  # Update every 1 second


if __name__ == "__main__":
    app = RandomNumberGeneratorApp()
    app.mainloop()
