from html_builder import PembuatHTML

# Membuat instance dari PembuatHTML
builder = PembuatHTML(judul="Halaman Web Dengan Gaya")

# Menambahkan elemen-elemen ke HTML
builder.tambah_judul(1, "Selamat Datang di Halaman Web Dengan Gaya")
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

# Menambahkan gaya custom
gaya_custom = """
    body {
        background-color: #ffffff;
    }
    h1 {
        color: #0000ff;
    }
"""
builder.set_gaya_custom(gaya_custom)

# Menghasilkan HTML dan menyimpannya ke file
html_content = builder.generate_html()
with open('output.html', 'w') as file:
    file.write(html_content)

print("HTML berhasil dibuat dan disimpan di 'output.html'")
