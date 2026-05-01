from dataclasses import dataclass, field
class PlantError(Exception):
    pass

@dataclass
class Plant:
    code: str
    name: str
    species: str
    height: int
    _tag: str = field(init=False, default="NEW")

    def __post_init__(self):
        if self.height <= 0:
            raise PlantError(f"Invalid height for {self.code}")
    @property
    def is_tall(self):
        return self.height > 100
    def __str__(self):
        return f"[{self.code}] {self.name} ({self.species}, {self.height}cm) -> {self._tag}"
    def __lt__(self, other):
        return self.height < other.height
class GrowthChecker:
    def __init__(self, plants, max_height):
        self._plants = plants
        self._max_height = max_height
        self._cursor = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._cursor >= len(self._plants):
            raise StopIteration
        plant = self._plants[self._cursor]
        if plant.height <= self._max_height:
            plant._tag = "READY"
        else:
            plant._tag = "OVERSIZED"
        self._cursor += 1
        return plant
def nursery_report(checker):
    ready = 0
    oversized = 0
    for plant in checker:
        if plant._tag == "READY":
            ready += 1
        else:
            oversized += 1
        yield str(plant)
    yield f"Summary: {ready} ready, {oversized} oversized"
class NurserySession:
    def __init__(self, name):
        self.name = name
        self._plants = []

    def __enter__(self):
        print(f"=== Open: {self.name} ===")
        return self

    def add(self, plant):
        self._plants.append(plant)

    def inspect(self, max_height):
        checker = GrowthChecker(self._plants, max_height)
        return nursery_report(checker)

    def __exit__(self, exc_type, exc, tb):
        if exc_type is PlantError:
            print(f"!!! Error: {exc}")
            print(f"=== Close: {self.name} ({len(self._plants)} plants) ===")
            return True

        print(f"=== Close: {self.name} ({len(self._plants)} plants) ===")

with NurserySession("Spring Sale") as ns:
    ns.add(Plant("P01", "Rose", "Flower", 45))
    ns.add(Plant("P02", "Cactus", "Succulent", 20))
    ns.add(Plant("P03", "Bamboo", "Grass", 180))

    for line in ns.inspect(100):
        print(line)

    print(ns._plants[1] < ns._plants[0])

print()

with NurserySession("Summer Sale") as ns:
    ns.add(Plant("P04", "Fern", "Fern", -10))
