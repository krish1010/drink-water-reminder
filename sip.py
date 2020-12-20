"""Remind to drink water."""
from win10toast import ToastNotifier
import schedule
import time

from constants import ICON_PATH


def remind() -> None:
    """Spun up a notification reminding to take a sip."""
    toaster = ToastNotifier()
    toaster.show_toast("It is time...", "Have a sip!", icon_path=ICON_PATH)


schedule.every().hour.do(remind)
while True:
    schedule.run_pending()
    time.sleep(1)
