# PembuatHTML - Modul Python untuk Membuat HTML

PembuatHTML adalah modul Python yang memudahkan pembuatan halaman HTML dengan berbagai elemen HTML umum dan dukungan untuk CSS. Modul ini memungkinkan Anda untuk membuat HTML secara dinamis dan menambahkan gaya default atau kustom sesuai kebutuhan.

## Fitur

- Menambahkan berbagai elemen HTML: judul, paragraf, tautan, gambar, daftar, formulir, tabel, dan banyak lagi.
- Dukungan untuk elemen-elemen HTML seperti `<audio>`, `<video>`, `<script>`, `<link>`, `<meta>`, dan `<base>`.
- Gaya CSS default yang diterapkan untuk elemen umum.
- Kemampuan untuk menambahkan gaya CSS kustom.
- Metode sederhana dan mudah digunakan untuk membangun struktur HTML.

## Instalasi

Modul ini tidak memerlukan instalasi tambahan selain Python. Anda hanya perlu menyimpan file `html_builder.py` ke dalam proyek Anda.

## Penggunaan

1. **Membuat instance dari PembuatHTML**

   ```python
   from html_builder import PembuatHTML

   # Membuat instance dari PembuatHTML
   builder = PembuatHTML(judul="Judul Halaman")
   ```

2. **Menambahkan elemen-elemen HTML**

   ```python
   builder.tambah_judul(1, "Selamat Datang di Halaman Web")
   builder.tambah_paragraf("Ini adalah paragraf teks.")
   builder.tambah_tautan("https://contoh.com", "Kunjungi Contoh.com")
   builder.tambah_gambar("https://via.placeholder.com/150", alt="Gambar Placeholder")
   builder.tambah_daftar(["Item 1", "Item 2", "Item 3"], terurut=True)
   builder.tambah_formulir(aksi="/submit", inputs=[('text', 'nama', ''), ('email', 'email', '')])
   builder.tambah_table(header=["Kolom 1", "Kolom 2"], baris=[["Data 1", "Data 2"], ["Data 3", "Data 4"]])
   builder.tambah_div(konten="Ini adalah div.")
   builder.tambah_span(konten="Ini adalah span.")
   builder.tambah_audio(src="audio.mp3", controls=True)
   builder.tambah_video(src="video.mp4", controls=True)
   builder.tambah_script(src="script.js")
   builder.tambah_link(href="styles.css", rel="stylesheet")
   builder.tambah_meta(charset="UTF-8")
   builder.tambah_base(href="https://example.com/")
   ```

3. **Menambahkan gaya kustom (opsional)**

   ```python
   gaya_custom = """
       body {
           background-color: #ffffff;
       }
       h1 {
           color: #0000ff;
       }
   """
   builder.set_gaya_custom(gaya_custom)
   ```

4. **Menghasilkan HTML dan menyimpannya ke file**

   ```python
   html_content = builder.generate_html()
   with open('output.html', 'w') as file:
       file.write(html_content)
   ```

## Contoh Output

Modul ini menghasilkan HTML seperti berikut:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Judul Halaman</title>
    <style>
        /* Gaya default dan gaya kustom */
    </style>
</head>
<body>
    <!-- Elemen HTML yang ditambahkan -->
</body>
</html>
```

## Kontribusi

Jika Anda memiliki saran atau ingin berkontribusi pada proyek ini, silakan buka issue atau pull request di repositori GitHub ini.

## Lisensi

Modul ini dilisensikan di bawah [MIT License](LICENSE).

## Kontak

Untuk pertanyaan lebih lanjut, Anda dapat menghubungi [kami](mailto:felixxx@felixxx.my.id).

---
