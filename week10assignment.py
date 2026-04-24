class TournamentError(Exception):
    pass
class TeamAlreadyRegisteredError(TournamentError):
    def __init__(self, team_name):
        self.team_name = team_name
        error_text = f"team already registered: {team_name}"
        super().__init__(error_text)
        
class TeamNotRegisteredError(TournamentError):
    def __init__(self, team_name):
        self.team_name = team_name
        error_text = f"team not registered: {team_name}"
        super().__init__(error_text)

class InvalidRoundError(TournamentError):
    def __init__(self, round_num, valid_rounds):
        self.round_num = round_num
        self.valid_rounds = valid_rounds
        error_text = f"invalid round {round_num}. valid rounds: {valid_rounds}"
        super().__init__(error_text)

class QuizJudge:
    def __init__(self, official_answers):
        self.official_answers = official_answers
        self.submissions = {}

    def register_team(self, team_name):
        if team_name in self.submissions:
            raise TeamAlreadyRegisteredError(team_name)
        self.submissions[team_name] = {}

    def submit_answer(self, team_name, round_num, answer):
        try:
            team_answers = self.submissions[team_name]
        except KeyError:
            raise TeamNotRegisteredError(team_name) from None

        if round_num not in self.official_answers:
            valid_rounds = list(self.official_answers.keys())
            raise InvalidRoundError(round_num, valid_rounds)
        team_answers[round_num] = answer

    def score(self, team_name):
        try:
            team_answers = self.submissions[team_name]
        except KeyError:
            raise TeamNotRegisteredError(team_name) from None
        if not team_answers:
            return 0
        correct = 0
        total_rounds = len(self.official_answers)
        for round_num, answer in team_answers.items():
            if self.official_answers.get(round_num) == answer:
                correct += 1
        return (correct * 100) // total_rounds

answers = {1: "Paris", 2: "7", 3: "Mars", 4: "Einstein", 5: "1945", 6: "Au"}
judge = QuizJudge(answers)

judge.register_team("Wolves")
judge.register_team("Eagles")

judge.submit_answer("Wolves", 1, "Paris")
judge.submit_answer("Wolves", 2, "7")
judge.submit_answer("Wolves", 3, "Jupiter")
judge.submit_answer("Wolves", 4, "Einstein")
judge.submit_answer("Wolves", 5, "1945")
judge.submit_answer("Wolves", 6, "Au")

judge.submit_answer("Eagles", 1, "London")
judge.submit_answer("Eagles", 2, "7")
judge.submit_answer("Eagles", 3, "Mars")

print(f"Wolves: {judge.score('Wolves')}%")
print(f"Eagles: {judge.score('Eagles')}%")

tests = [
    lambda: judge.register_team("Wolves"),
    lambda: judge.submit_answer("Foxes", 1, "Paris"),
    lambda: judge.submit_answer("Eagles", 10, "answer"),
]

for test in tests:
    try:
        test()
    except TournamentError as e:
        print(e)