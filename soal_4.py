class Buah:

    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa
    # metode
    def setNama(self, item):
        self.nama = item
    def setWarna(self, bahan):
        self.warna = bahan
    def setRasa(self,enak):
        self.rasa = enak
    def information(self):
        return f'Nama Buah : {self.nama} | Warna Buah : {self.warna} | Rasa Buah : {self.rasa}'


buah1 = Buah('apel','merah','manis')
buah1.setNama('pir')
buah1.setWarna('kuning')
print(buah1.information())

buah2 = Buah('Anggur','ungu', 'manis')
buah2.setNama('ceri')
buah2.setWarna('merah')
print(buah2.information())