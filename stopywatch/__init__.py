from copy import copy
import time
from datetime import timedelta

class Stopwatch:
    def __init__(self, start=True, timer=time.time):
        self._timer = timer
        self._start_time = None
        self._elapsed_time = 0
        self._lap_time = 0
        self._running = False
        if start:
            self.start()
    @property
    def timer(self):
        return self._timer
    @property
    def start_time(self):
        return self._start_time
    @property
    def elapsed_time(self):
        return self._elapsed_time
    @property
    def running(self):
        return self._running

    def start(self):
        if not self.running:
            if self._start_time is None:
                self._start_time = self.timer()
                self._lap_time = copy(self.start_time)
            self._running = True

    def stop(self):
        if self.running:
            self._elapsed_time = self.timer()
            self._running = False

    def time(self):
        return self.timer()

    def elapsed(self):
        if self.running:
            self._elapsed_time = self.timer()
        return f"Elapsed: {Stopwatch.s_to_hms(self._elapsed_time - self.start_time)}"

    def lap(self):
        time = self.timer()
        out = time - self._lap_time
        self._lap_time = time
        return f"Laptime: {Stopwatch.s_to_hms(out)}"

    @staticmethod
    def s_to_hms(time_in_s):
        # Create a timedelta object from the duration
        return timedelta(seconds=time_in_s)
