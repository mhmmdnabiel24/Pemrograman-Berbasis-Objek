class ValidatorManager:
    def validate(self, sks, prasyarat_terpenuhi):
        if sks > 24:
            return "Registrasi gagal: SKS melebihi batas"
        elif not prasyarat_terpenuhi:
            return "Registrasi gagal: Prasyarat belum terpenuhi"
        else:
            return "Registrasi berhasil"

validator = ValidatorManager()

# Contoh 1 (True)
print("Contoh 1:")
print(validator.validate(20, True))

# Contoh 2 (False)
print("\nContoh 2:")
print(validator.validate(20, False))