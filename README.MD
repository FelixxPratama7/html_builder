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

# Kode Python `html_builder.py`

```python
class PembuatHTML:
    def __init__(self, judul="Dokumen"):
        self.judul = judul
        self.elemen = []
        self.gaya_default = """
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
                color: #333;
            }
            h1, h2, h3, h4, h5, h6 {
                color: #333;
            }
            p {
                margin: 0 0 1em 0;
            }
            a {
                color: #0066cc;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
            }
            th {
                background-color: #f2f2f2;
            }
            form {
                margin: 1em 0;
            }
        """
        self.gaya_custom = ""

    def tambah_elemen(self, tag, konten='', **atribut):
        attrs = ' '.join(f'{key}="{value}"' for key, value in atribut.items())
        if attrs:
            attrs = ' ' + attrs
        if tag in ['img', 'input', 'br', 'hr', 'meta', 'link', 'base']:
            self.elemen.append(f'<{tag}{attrs}>')
        else:
            self.elemen.append(f'<{tag}{attrs}>{konten}</{tag}>')

    def tambah_judul(self, level, konten, **atribut):
        self.tambah_elemen(f'h{level}', konten, **atribut)

    def tambah_paragraf(self, konten, **atribut):
        self.tambah_elemen('p', konten, **atribut)

    def tambah_tautan(self, href, teks, **atribut):
        self.tambah_elemen('a', teks, href=href, **atribut)

    def tambah_gambar(self, src, alt='', **atribut):
        self.tambah_elemen('img', '', src=src, alt=alt, **atribut)

    def tambah_daftar(self, items, terurut=False, **atribut):
        tag = 'ol' if terurut else 'ul'
        item_list = ''.join(f'<li>{item}</li>' for item in items)
        self.tambah_elemen(tag, item_list, **atribut)

    def tambah_formulir(self, aksi='', metode='post', inputs=[], **atribut):
        input_elements = ''.join(f'<input type="{tipe_input}" name="{nama}" value="{nilai}">' for tipe_input, nama, nilai in inputs)
        self.tambah_elemen('form', input_elements, action=aksi, method=metode, **atribut)

    def tambah_table(self, header, baris, **atribut):
        header_elements = ''.join(f'<th>{item}</th>' for item in header)
        baris_elements = ''.join(
            f'<tr>{"".join(f"<td>{item}</td>" for item in row)}</tr>' for row in baris
        )
        self.tambah_elemen('table', f'<thead><tr>{header_elements}</tr></thead><tbody>{baris_elements}</tbody>', **atribut)

    def tambah_div(self, konten='', **atribut):
        self.tambah_elemen('div', konten, **atribut)

    def tambah_span(self, konten='', **atribut):
        self.tambah_elemen('span', konten, **atribut)

    def tambah_audio(self, src, **atribut):
        self.tambah_elemen('audio', '', src=src, **atribut)

    def tambah_video(self, src, **atribut):
        self.tambah_elemen('video', '', src=src, **atribut)

    def tambah_script(self, src='', **atribut):
        self.tambah_elemen('script', '', src=src, **atribut)

    def tambah_link(self, href='', **atribut):
        self.tambah_elemen('link', '', href=href, **atribut)

    def tambah_meta(self, **atribut):
        self.tambah_elemen('meta', '', **atribut)

    def tambah_base(self, href='', **atribut):
        self.tambah_elemen('base', '', href=href, **atribut)

    def set_gaya_custom(self, gaya):
        self.gaya_custom = gaya

    def generate_html(self):
        style = f'<style>{self.gaya_default}\n{self.gaya_custom}</style>' if self.gaya_custom else f'<style>{self.gaya_default}</style>'
        elemen_str = '\n'.join(self.elemen)
        return f'<!DOCTYPE html>\n<html>\n<head>\n<title>{self.judul}</title>\n{style}\n</head>\n<body>\n{elemen_str}\n</body>\n</html>'
```
