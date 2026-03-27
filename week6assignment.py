# Athlete Training Tracker
def log_action(func):
    def wrapper(*args, **kwargs):
        print("[ACTION] " + func.__name__ + " executed")
        return func(*args, **kwargs)
    return wrapper
class Athlete:
    _total_athletes = 0
    def __init__(self, name, athlete_id):
        self.name = name
        self.athlete_id = athlete_id
        self._sessions = {}   # exercise : intensity
        Athlete._total_athletes += 1
    @log_action
    def add_session(self, exercise, intensity):
        exercise = exercise.upper()
        self._sessions[exercise] = intensity
        return self.name + " trained " + exercise + " at intensity " + str(intensity)
    def avg_intensity(self):
        if len(self._sessions) == 0:
            return 0.0
        total = 0
        for value in self._sessions.values():
            total += value     
        avg = total / len(self._sessions)
        return float(round(avg, 1))
    def hardest_session(self):
        if len(self._sessions) == 0:
            return "No sessions" 
        max_ex = ""
        max_val = -1 
        for ex, val in self._sessions.items():
            if val > max_val:
                max_val = val
                max_ex = ex
        return max_ex
    @classmethod
    def from_roster(cls, data):
        parts = data.split("-")
        name = parts[0]
        athlete_id = parts[1]
        return cls(name, athlete_id)
    @staticmethod
    def is_valid_id(athlete_id):
        if len(athlete_id) == 7 and athlete_id.isdigit():
            return True
        else:
            return False
    @classmethod
    def total_athletes(cls):
        return cls._total_athletes

# Input

a1 = Athlete("Bobur", "5501001")
a1.add_session("sprints", 95)
a1.add_session("weights", 80)
a1.add_session("swimming", 70)

a2 = Athlete.from_roster("Nilufar-5501002")
a2.add_session("Cycling", 82)
a2.add_session("sprints", 91)

print(f"{a1.name}: Avg = {a1.avg_intensity()}, Hardest = {a1.hardest_session()}")
print(f"{a2.name}: Avg = {a2.avg_intensity()}, Hardest = {a2.hardest_session()}")

print(f"Valid ID '5501001': {Athlete.is_valid_id('5501001')}")
print(f"Valid ID '55X': {Athlete.is_valid_id('55X')}")
print(f"Total athletes: {Athlete.total_athletes()}")

# Expected Output

# [ACTION] add_session executed
# [ACTION] add_session executed
# [ACTION] add_session executed
# [ACTION] add_session executed
# [ACTION] add_session executed
# Bobur: Avg = 81.7, Hardest = SPRINTS
# Nilufar: Avg = 86.5, Hardest = SPRINTS
# Valid ID '5501001': True
# Valid ID '55X': False
# Total athletes: 2
