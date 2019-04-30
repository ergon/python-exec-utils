import collections
import threading
from datetime import datetime


class Slurper(threading.Thread):

    def __init__(self, handle, log_file, log_console, console_handle, capture_output):
        super().__init__()
        self.capture_output = capture_output
        self.console_handle = console_handle

        if callable(log_console):
            self.console_log_function = log_console
            self.log_console = True
        else:
            self.console_log_function = console_handle.write
            self.log_console = log_console

        self.log_console = log_console
        self.log_file = log_file
        if self.log_file:
            self.log_handle = open(log_file, "a")
        else:
            self.log_handle = None

        self.handle = handle
        self.result = None
        super().start()

    def run(self):
        if self.capture_output:
            lines = []
        else:
            # limit to 4096 lines of data (mainly for error handling, we want some output
            # even if the user doesn't want any
            lines = collections.deque(maxlen=4096)

        for line_bytes in iter(self.handle.readline, ''):
            if line_bytes == b'':
                break
            line = line_bytes.decode("utf-8", "backslashreplace")
            lines.append(line)
            if self.log_console:
                self.console_log_function(line)
            if self.log_handle:
                self.log_handle.write("%s: %s" % (
                    datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                    line))
        self.result = "".join(lines)
