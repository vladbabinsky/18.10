class Schedule:
    def __init__(self):
        self.schedules = []

    def add_schedule(self, transport, time):
        self.schedules.append((transport, time))

    def show_schedules(self):
        for transport, time in self.schedules:
            print(f"{transport}: {time}")
