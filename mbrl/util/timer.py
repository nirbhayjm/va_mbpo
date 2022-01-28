# Adapted from: https://realpython.com/python-timer/#a-python-timer-context-manager

import time
from collections import deque

import numpy as np


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

    pass


class Timer:
    timers = dict()

    def __init__(
        self,
        # logger,
        name=None,
        text="Elapsed time: {:0.4f} seconds",
        max_num_record=10,
        verbose=True,
    ):
        self._start_time = None
        self.name = name
        self.text = text
        # self.logger = logger.info
        self.verbose = verbose

        # Add new named timers to dictionary of timers
        if name and name not in self.timers.keys():
            # self.timers.setdefault(name, 0)
            self.timers[name] = deque(maxlen=max_num_record)

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

        # if self.verbose and self.logger:
        #     self.logger(f"[{self.name}] " + self.text.format(elapsed_time))
        if self.name:
            self.timers[self.name].append(elapsed_time)

        return elapsed_time

    def get_elapsed_time(self):
        """Report the elapsed time without stopping timer"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time

        # if self.verbose and self.logger:
        #     self.logger(f"[{self.name}] " + self.text.format(elapsed_time))
        # if self.name:
        #     self.timers[self.name].append(elapsed_time)

        return elapsed_time

    def get_mean_time(self, name=None):
        if name is None:
            name = self.name
        if name not in self.timers:
            raise KeyError

        time_list = self.timers[name]
        if len(time_list) > 0:
            return np.mean(time_list)
        else:
            return 0
