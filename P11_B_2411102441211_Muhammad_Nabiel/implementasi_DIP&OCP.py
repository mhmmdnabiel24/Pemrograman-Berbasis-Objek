from abc import ABC, abstractmethod

#membuat  inrterface Validator
class Validator(ABC):
    @abstractmethod
    def validate(self):
        pass

#implementasi validasi SKS
class SKSValidator(Validator):
    def __init__(self, sks):
        self.sks = sks

    def validate(self):
        return self.sks <= 24
    

#implementasi validasi prasyarat
class PrasyaratValidator(Validator):
    def __init__(self, terpenuhi):
        self.terpenuhi = terpenuhi

    def validate(self):
        return self.terpenuhi

#implementasi SRP
class ValidatorManager:
    def __init__(self, validators):
        self.validators = validators

    def validate(self):
        for validator in self.validators:
            if not validator.validate():
                return "Registrasi gagal"
        return "Registrasi berhasil"

# contoh input true
validators = [
    SKSValidator(20),
    PrasyaratValidator(True)
]

manager = ValidatorManager(validators)
print(manager.validate())

#contoh input false
validators_false = [
    SKSValidator(20),
    PrasyaratValidator(False)
]
manager_false = ValidatorManager(validators_false)
print(manager_false.validate())