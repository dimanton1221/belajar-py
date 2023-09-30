class Mobil:
    def __init__(self, merek, model, tahun):
        self.merek = merek
        self.model = model
        self.tahun = tahun

    def print_info(self):
        print(f"Merek: {self.merek}\nModel: {self.model}\nTahun: {self.tahun}")
