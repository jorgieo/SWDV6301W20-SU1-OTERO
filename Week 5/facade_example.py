"""
Facade Pattern Example: A Washing Machine
"""

class CycleDial():
    def select_cycle(self, cycle):
        return f"{cycle} Cycle Selected"

class TemperatureDial():
    def set_water_temp(self, temp):
        return f"Water Temperature: {temp}"

class WaterValve():
    def open_valve(self):
        return "Fill Valve Open"
    def close_valve(self):
        return "Fill Valve Closed"

class DrainPump():
    def start_pump(self):
        return "Drain Pump Running"
    def stop_pump(self):
        return "Drain Pump Stopping"

class DrumMotor():
    def wash(self):
        return "Drum Washing"
    def stop(self):
        return "Drum Stopping"
    def spin(self):
        return "Drum Spinning"

class LidLock():
    def lock(self):
        return "Lid Locked"
    def unlock(self):
        return "Lid Unlocked"

class WashingMachineFacade:
    def __init__(self):
        self.cycle = CycleDial()
        self.temp = TemperatureDial()
        self.fill = WaterValve()
        self.drain = DrainPump()
        self.drum = DrumMotor()
        self.lid = LidLock()

    def begin_cycle(self, cycle, temp='TAP COLD'):
        self.cycle.select_cycle(cycle)
        if cycle == 'wash':
            self._wash(temp)
        if cycle == 'spin':
            self._spin()

    def _wash(self, temp):
        print(self.temp.set_water_temp(temp))
        print(self.fill.open_valve())
        print(self.fill.close_valve())
        print(self.drum.wash())
        print(self.drain.start_pump())
        print(self.lid.lock())
        print(self.drum.spin())
        print(self.drain.stop_pump())
        print(self.drum.stop())
        print(self.lid.unlock())
        print("DONE\n")

    def _spin(self):
        print(self.lid.lock())
        print(self.drain.start_pump())
        print(self.drum.spin())
        print(self.drain.stop_pump())
        print(self.lid.unlock())
        print("DONE\n")

if __name__ == '__main__':
    washer = WashingMachineFacade()
    washer.begin_cycle('wash')
    washer.begin_cycle('spin')
    washer.begin_cycle('wash', 'HOT')