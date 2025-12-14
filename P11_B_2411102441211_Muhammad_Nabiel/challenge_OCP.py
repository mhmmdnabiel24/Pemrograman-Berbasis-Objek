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
    
# Challenge OCP
class IPKValidator(Validator):
    def __init__(self, ipk):
        self.ipk = ipk

    def validate(self):
        return self.ipk >= 3.0
    
validators = [
    SKSValidator(20),
    PrasyaratValidator(True),
    IPKValidator(3.5)   
]

manager = ValidatorManager(validators)
print(manager.validate())
