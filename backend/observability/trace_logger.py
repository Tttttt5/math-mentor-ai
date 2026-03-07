import time


class TraceLogger:

    def __init__(self):
        self.events = []

    def log(self, agent):

        self.events.append({
            "agent": agent,
            "timestamp": time.time()
        })

    def get_trace(self):

        return [e["agent"] for e in self.events]