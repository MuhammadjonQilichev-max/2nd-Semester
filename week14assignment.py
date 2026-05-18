from abc import ABC, abstractmethod
from enum import Enum
class Sheet:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.lines = []
        return cls._instance
    def mark(self, text):
        self.lines.append(text)
        print(f"=> {text}")
    def __len__(self):
        return len(self.lines)

class ToolKind(Enum):
    BURNER = 1
    VENT = 2
    TIMER = 3

class Recipe(ABC):
    @abstractmethod
    def cook(self, temp):
        pass

class FireIfCold(Recipe):
    def __init__(self, limit):
        self.limit = limit

    def cook(self, temp):
        if temp < self.limit:
            return "FIRE"
        return None

class CoolIfHot(Recipe):
    def __init__(self, limit):
        self.limit = limit

    def cook(self, temp):
        if temp > self.limit:
            return "COOL"
        return None

class Wait(Recipe):
    def cook(self, temp):
        return None

class Tool(ABC):
    @abstractmethod
    def apply(self, temp):
        pass

class Gear(Tool):
    def __init__(self, name, recipe):
        self.name = name
        self.recipe = recipe
    def apply(self, temp):
        result = self.recipe.cook(temp)
        if result is not None:
            Sheet().mark(f"{self.name} {result} (temp={temp}C)")

class Oven:
    def __init__(self):
        self._gears = []

    def attach(self, gear):
        self._gears.append(gear)

    def measure(self, temp):
        Sheet().mark(f"temp={temp}C")

        for gear in self._gears:
            gear.apply(temp)

def make_burner(name):
    return Gear(name, FireIfCold(200))
def make_vent(name):
    return Gear(name, CoolIfHot(350))
def make_timer(name):
    return Gear(name, Wait())

class GearFactory:
    _builders = {ToolKind.BURNER: make_burner, ToolKind.VENT: make_vent, ToolKind.TIMER: make_timer}

    @staticmethod
    def create(kind, name):
        builder = GearFactory._builders.get(kind)

        if builder is None:
            raise ValueError(f"Unknown tool: {kind}")

        return builder(name)

oven = Oven()
oven.attach(GearFactory.create(ToolKind.BURNER, "Flame"))
oven.attach(GearFactory.create(ToolKind.VENT, "Fan"))
oven.attach(GearFactory.create(ToolKind.TIMER, "Clock"))

for temp in [250, 150, 400, 300]:
    oven.measure(temp)

print(f"Total lines: {len(Sheet().lines)}")
