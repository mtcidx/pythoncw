class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas_segitiga(self):
        return self.alas * self.tinggi / 2