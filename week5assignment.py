from abc import ABC, abstractmethod
class Validator(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def validate(self, value):
        pass
    def check(self, value):
        result = self.validate(value)
        if result:
            status = "PASS"
        else:
            status = "FAIL"
        print(f"[{status}] {self.name}: {value}")
        return result
class LengthValidator(Validator):
    def __init__(self, min_len, max_len):
        super().__init__(f"Length({min_len}-{max_len})")
        self.min_len = min_len
        self.max_len = max_len
    def validate(self, value):
        result = False
        if self.min_len <= len(value) <= self.max_len:
            result = True
        return result
class ContainsDigitValidator(Validator):
    def __init__(self):
        super().__init__("ContainsDigit")
    def validate(self, value):
        result = False
        for ch in value:
            if ch.isdigit():
                result = True
        return result
class NoSpacesValidator(Validator):
    def __init__(self):
        super().__init__("NoSpaces")
    def validate(self, value):
        result = True
        if " " in value:
            result = False
        return result
class StartsWithUpperValidator:
    def __init__(self):
        self.name = "StartsWithUpper"
    def validate(self, value):
        result = False
        if value != "" and value[0].isupper():
            result = True
        return result
    def check(self, value):
        result = self.validate(value)
        if result:
            status = "PASS"
        else:
            status = "FAIL"
        print(f"[{status}] {self.name}: {value}")
        return result
class ValidationReport:
    def __init__(self):
        self.entries = []
    def add(self, name, value, passed):
        result = self.entries.append((name, value, passed))
        return result
    def summary(self):
        total = len(self.entries)
        passed = 0
        for item in self.entries:
            if item[2]:
                passed += 1
        failed = total - passed
        result = print(f"Total: {total}, Passed: {passed}, Failed: {failed}")
        return result
class FormField:
    def __init__(self, field_name):
        self.field_name = field_name
        self.validators = []
        self.report = ValidationReport()
    def add_validator(self, validator):
        result = self.validators.append(validator)
        return result
    def validate(self, value):
        print(f'Validating {self.field_name}: "{value}"')
        all_passed = True
        for v in self.validators:
            res = v.check(value)
            self.report.add(v.name, value, res)
            if res == False:
                all_passed = False
        result = all_passed
        return result
    def show_report(self):
        print(f"--- Report for {self.field_name} ---")
        result = self.report.summary()
        return result
username_field = FormField('username')
username_field.add_validator(LengthValidator(3, 15))
username_field.add_validator(NoSpacesValidator())
username_field.add_validator(ContainsDigitValidator())
username_field.add_validator(StartsWithUpperValidator())

valid1 = username_field.validate('Admin1')
print(f'Valid: {valid1}')
print()

valid2 = username_field.validate('no')
print(f'Valid: {valid2}')
print()

valid3 = username_field.validate('has space')
print(f'Valid: {valid3}')
print()

username_field.show_report()

try:
    v = Validator('test')
except TypeError:
    print('Cannot instantiate abstract class')
