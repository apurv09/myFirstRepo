import datetime
import time

def set_alarm():
    print("--- Python Alarm Clock ---")
    while True:
        alarm_time_input = input("Enter alarm time in 24-hour format (HH:MM): ").strip()
        try:
            datetime.datetime.strptime(alarm_time_input, "%H:%M")
            break
        except ValueError:
            print("❌ Invalid format. Please use HH:MM (e.g., 07:30).")
            
    print(f"🔔 Alarm set for {alarm_time_input}.")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time_input:
            print("\n🚨 WAKE UP! The alarm is ringing! 🚨")
            try:
                import winsound
                winsound.Beep(1000, 3000) 
            except ImportError:
                for _ in range(5):
                    print("\a", end="", flush=True)
                    time.sleep(0.5)
            break
        time.sleep(10)

if __name__ == "__main__":
    set_alarm()
