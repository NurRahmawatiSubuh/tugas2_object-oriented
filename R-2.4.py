class Bunga :
    def __init__(self, nama,jumlah_kelopak,harga):
        self.nama = nama
        self.jumlah_kelopak= jumlah_kelopak
        self.harga=harga
    def set_nama(self, new_nama):
        self.nama = new_nama

    def jumlah_kelopak(self, new_jumlah_kelopak):
        self.nama=new_jumlah_kelopak
    def set_harga(self, new_harga):
        self.harga = new_harga
        return self.nama

flower1=Bunga("Amarilis",9,3)
print("Bunga",flower1.nama,"berkelopak",flower1.jumlah_kelopak,"harganya",flower1.harga)
flower1.set_nama("Melati")
print("Bunga",flower1.nama,"berkelopak",flower1.jumlah_kelopak,"harganya",flower1.harga)
