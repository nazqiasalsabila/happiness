import streamlit as st

st.set_page_config(page_title="Tes Cinta Lucu 💘", layout="centered")

st.markdown("""
    <div style='text-align: center;'>
        <img src='https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif' width='200'>
        <h1 style='color: #ff4b91; font-size: 42px;'>💘 Jelita ❤️ Madut 💘</h1>
        <p style='font-size:20px; color: #ff66a3;'>Tes Cinta Lucu & Receh</p>
        <p style='font-size:18px; color: #555;'>Cocokin jawaban kamu sama pasanganmu dan lihat seberapa cocok kalian 😝</p>
    </div>
""", unsafe_allow_html=True)

pertanyaan = [
    ("1. Kalau aku tiba-tiba nangis, kamu bakal...", ["A. Panik dan ikut nangis", "B. Langsung peluk", "C. Nanya dulu, tapi tetep bingung"]),
    ("2. Pilihan kencan paling seru menurut kamu:", ["A. Nonton film/ main game", "B. Ngobrol ngobrol di cafe", "C. Keliling keliling naik motor"]),
    ("3. Kalau aku bales chat cuma 'Hmm.', kamu akan...", ["A. iya", "B. Bales: 'Oke.'", "C. Kirim stiker nyindir"]),
    ("4. Kalau lagi LDR, hal yang paling kamu butuhin adalah...", ["A. Video call tiap malam", "B. kirim pap tiap waktu", "C. long teks romantis"]),
    ("5. Kamu tuh tipe pasangan yang...", ["A. Gampang baper", "B. cuek tapi sayang", "C. Santai tapi tiba-tiba manja"]),
    ("6. Kalau kita berantem, kamu bakal...", ["A. Minta maaf duluan walau gak salah", "B. Ngilang dulu biar adem", "C. Kirim meme kucing buat baikan"]),
    ("7. Kebiasaan kamu yang paling ngeselin tapi aku kangenin:", ["A. Lupa bales padahal udah baca", "B. Ngasih kode tapi gak mau jujur langsung", "C. Tiba-tiba ngambek terus peluk"]),
    ("8. Kalau disuruh milih panggilan sayang:", ["A. Bubup", "B. Sayang", "C. Nama makanan lucu (e.g. Bakso, Cimol)"]),
    ("9. Kalau kita jadi karakter kartun, kamu bakal jadi...", ["A. Spongebob: rame dan niat", "B. Shinchan: nakal tapi gemes", "C. Nobita: lemot tapi setia"]),
    ("10. Kalau aku ketiduran pas lagi video call...", ["A. Langsung screenshot wajah kamu yang konyol", "B. Bilang besoknya: 'Kamu ngorok tau semalem'", "C. Liatin kamu tidur"]),
]

st.subheader("🔐 Masukkan Jawaban Kunci (Pasanganmu)")
kunci_jawaban = []
with st.form("input_kunci"):
    for i, (tanya, opsi) in enumerate(pertanyaan):
        pilihan = st.radio(f"{tanya} (Jawaban Pasangan)", opsi, key=f"kunci{i}")
        kunci_jawaban.append(pilihan)
    simpan_kunci = st.form_submit_button("✅ Simpan Jawaban Kunci")

if simpan_kunci:
    st.success("Jawaban kunci disimpan! Sekarang isi jawaban kamu dan lihat kecocokannya.")

    st.subheader("📝 Isi Jawaban Kamu")
    jawaban_kamu = []
    cocok = 0
    with st.form("isi_jawaban"):  
        for i, (tanya, opsi) in enumerate(pertanyaan):
            pilihan = st.radio(f"{tanya} (Jawaban Kamu)", opsi, key=f"jawab{i}")
            jawaban_kamu.append(pilihan)
        submit_jawaban = st.form_submit_button("❤️ Lihat Kecocokan")

    if submit_jawaban:
        for j1, j2 in zip(kunci_jawaban, jawaban_kamu):
            if j1 == j2:
                cocok += 1

        persen = cocok / len(pertanyaan) * 100
        st.subheader("🎯 Hasil Kecocokan Kamu")
        st.write(f"Jawaban yang sama: **{cocok} dari {len(pertanyaan)}** pertanyaan")
        st.write(f"Persentase kecocokan: **{persen:.0f}%**")

        if persen == 100:
            st.success("🥰 Kalian kayak kembar pikiran! Langsung aja deh jadi couple goals 💘")
        elif persen >= 70:
            st.info("😍 Cocok banget! Tinggal atur jadwal kencan selanjutnya")
        elif persen >= 50:
            st.warning("🤔 Lumayan cocok, masih bisa diselaraskan lewat obrolan dan pelukan")
        else:
            st.error("😅 Beda frekuensi sih, tapi siapa tahu saling melengkapi?")

st.markdown("""
---
<p style='text-align: center; color: gray;'>Game ini buat seru-seruan dan ngetes chemistry bareng pasangan 💞</p>
""", unsafe_allow_html=True)
