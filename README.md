# Transport Vositalari Parki – Polimorfizm Misoli (Python)

## Tavsif
Ushbu loyiha transport vositalarini OOP yordamida modellashtiradi. Uchta sinf mavjud:

- **Avtobus**
- **YukMashinasi**
- **SportAvto**

Barchasi umumiy `Transport` bazaviy sinfidan meros oladi. Har bir sinf quyidagi metodlarga ega:

- `tezlik_oshirish()` – transportning harakat tezligini qaytaradi
- `yoqilgi_sarfi()` – km uchun yoqilg‘i sarfini qaytaradi
- `sayohat_masofa(masofa)` – berilgan masofaga ko‘ra vaqt va yoqilg‘i sarfini hisoblaydi
- `yuk_kotarish(yuk)` – faqat YukMashinasi sinfida ishlaydi, boshqalar 0 qaytaradi

---

## Funksionallik

- Transport obyektlari yaratiladi.
- Polimorfizm orqali ro‘yxatda aylantirilib quyidagilar hisoblanadi:
  - umumiy vaqt
  - umumiy yoqilg‘i sarfi
- YukMashinasi sinfi yuk ko‘tara oladi, qolganlari 0 qaytaradi.

---

## Ishga tushirish

```bash
python main.py
