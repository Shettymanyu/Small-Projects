import time
import plyer

def drink_water_reminder():
  while True:
    time.sleep(60 * 60) # Remind every hour (adjust as needed)
    plyer.notification.notify(
      title="Water Reminder",
      message="It's time to drink water! Stay hydrated.",
      timeout=10  # Notification duration in seconds
    )

if __name__ == "__main__":
  drink_water_reminder()