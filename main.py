class Transport:
    def tezlik_oshirish(self):
        raise NotImplementedError

    def yoqilgi_sarfi(self):
        raise NotImplementedError

    def sayohat_masofa(self, masofa):
        tezlik = self.tezlik_oshirish()
        vaqt = masofa / tezlik
        yoqilgi = masofa * self.yoqilgi_sarfi()
        return vaqt, yoqilgi

    def yuk_kotarish(self, yuk):
        return 0


class Avtobus(Transport):
    def __init__(self, tezlik, sarf):
        self.tezlik = tezlik
        self.sarf = sarf

    def tezlik_oshirish(self):
        return self.tezlik

    def yoqilgi_sarfi(self):
        return self.sarf


class YukMashinasi(Transport):
    def __init__(self, tezlik, sarf, max_yuk):
        self.tezlik = tezlik
        self.sarf = sarf
        self.max_yuk = max_yuk

    def tezlik_oshirish(self):
        return self.tezlik

    def yoqilgi_sarfi(self):
        return self.sarf

    def yuk_kotarish(self, yuk):
        if yuk <= self.max_yuk:
            return yuk
        return 0


class SportAvto(Transport):
    def __init__(self, tezlik, sarf):
        self.tezlik = tezlik
        self.sarf = sarf

    def tezlik_oshirish(self):
        return self.tezlik

    def yoqilgi_sarfi(self):
        return self.sarf


transportlar = [
    Avtobus(80, 0.15),
    YukMashinasi(60, 0.25, 5000),
    SportAvto(200, 0.12)
]

masofa = 240

umumiy_vaqt = 0
umumiy_yoqilgi = 0

for t in transportlar:
    vaqt, yoqilgi = t.sayohat_masofa(masofa)
    umumiy_vaqt += vaqt
    umumiy_yoqilgi += yoqilgi

print(umumiy_vaqt)
print(umumiy_yoqilgi)
print(transportlar[1].yuk_kotarish(3000))
print(transportlar[0].yuk_kotarish(1000))
