#!/usr/bin/env python3
import gi

gi.require_version("Notify", "0.7")
from gi.repository import Notify


Notify.init("Notifications Script")

# ----------------------------
# VERIFY BATTERY STATUS
# ----------------------------
with open("/sys/class/power_supply/BAT0/capacity", "r") as battery_level:
    if int(battery_level.read()) < 20:
        with open("/sys/class/power_supply/BAT0/status", "r") as battery_status:
            if battery_status.read() != "Discharging":
                battery_notification = Notify.Notification.new(
                    "BATTERY STATUS", "Connect your charger"
                )
                battery_notification.set_urgency(Notify.Urgency.CRITICAL)
                battery_notification.show()

