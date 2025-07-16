import streamlit as st

st.set_page_config(page_title="Tes Cinta Lucu 💘", layout="centered")

if "mulai" not in st.session_state:
    st.session_state.mulai = False
if "jawaban_kamu" not in st.session_state:
    st.session_state.jawaban_kamu = []
if "index" not in st.session_state:
    st.session_state.index = 0

st.markdown("""
    <div style='text-align: center;'>
        <img src='https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif' width='200'>
        <h1 style='color: #ff4b91; font-size: 42px;'>💘 Jelita ❤️ Madut 💘</h1>
        <p style='font-size:20px; color: #ff66a3;'>Tes Cinta Lucu & Receh</p>
        <p style='font-size:18px; color: #555;'>Jawab semua pertanyaannya dan lihat hasil akhir cintamu 😝</p>
    </div>
""", unsafe_allow_html=True)

if not st.session_state.mulai:
    if st.button("❤️ Mulai Tes Cinta!"):
        st.session_state.mulai = True
    st.stop()

pertanyaan = [
    ("1. Kalau aku tiba-tiba nangis, kamu bakal...", [
        "A. Panik dan ikut nangis",
        "B. Langsung peluk",
        "C. Nanya dulu, tapi tetep bingung"
    ]),
    ("2. Pilihan kencan paling seru menurut kamu:", [
        "A. Nonton film/ main game",
        "B. Ngobrol ngobrol di cafe",
        "C. Keliling keliling naik motor"
    ]),
    ("3. Kalau aku bales chat cuma 'Hmm.', kamu akan...", [
        "A. iya",
        "B. Bales: 'Oke.'",
        "C. Kirim stiker nyindir"
    ]),
    ("4. Kalau lagi LDR, hal yang paling kamu butuhin adalah...", [
        "A. Video call tiap malam",
        "B. kirim pap tiap waktu",
        "C. long teks romantis"
    ]),
    ("5. Kamu tuh tipe pasangan yang...", [
        "A. Gampang baper",
        "B. cuek tapi sayang",
        "C. Santai tapi tiba-tiba manja"
    ]),
    ("6. Kalau kita berantem, kamu bakal...", [
        "A. Minta maaf duluan walau gak salah",
        "B. Ngilang dulu biar adem",
        "C. Kirim meme kucing buat baikan"
    ]),
    ("7. Kebiasaan kamu yang paling ngeselin tapi aku kangenin:", [
        "A. Lupa bales padahal udah baca",
        "B. Ngasih kode tapi gak mau jujur langsung",
        "C. Tiba-tiba ngambek terus peluk"
    ]),
    ("8. Kalau disuruh milih panggilan sayang:", [
        "A. Bubup",
        "B. Sayang",
        "C. Nama makanan lucu (e.g. Bakso, Cimol)"
    ]),
    ("9. Kalau kita jadi karakter kartun, kamu bakal jadi...", [
        "A. Spongebob: rame dan niat",
        "B. Shinchan: nakal tapi gemes",
        "C. Nobita: lemot tapi setia"
    ]),
    ("10. Kalau aku ketiduran pas lagi video call...", [
        "A. Langsung screenshot wajah kamu yang konyol",
        "B. Bilang besoknya: 'Kamu ngorok tau semalem'",
        "C. Liatin kamu tidur"
    ])
]

kunci_jawaban = ["B", "B", "B", "A", "B", "A", "B", "B", "C", "A"]

st.subheader("📝 Jawab Pertanyaan Kamu")
idx = st.session_state.index
if idx < len(pertanyaan):
    tanya, opsi = pertanyaan[idx]
    pilihan = st.radio(tanya, opsi, key=f"soal_{idx}")
    if st.button("Selanjutnya"):
        st.session_state.jawaban_kamu.append(pilihan.split('.')[0])
        st.session_state.index += 1
        st.rerun()
else:
    st.subheader("🎯 Hasil Jawabanmu")
    jawaban = st.session_state.jawaban_kamu
    skor = sum([1 for i in range(len(kunci_jawaban)) if jawaban[i] == kunci_jawaban[i]])
    persentase = int((skor / len(kunci_jawaban)) * 100)
    st.write(f"✨ Jawaban yang cocok: {skor} dari {len(kunci_jawaban)}")
    st.write(f"❤️ Persentase Kecocokan: {persentase}%")

    if persentase == 100:
        st.success("Kalian bener-bener cocok banget! Soulmate! 💍")
    elif persentase >= 70:
        st.info("Cocok banget nih! Udah kayak couple goals 💑")
    elif persentase >= 50:
        st.warning("Lumayan cocok, tapi masih bisa disinkronin 💡")
    else:
        st.error("Wah... butuh lebih banyak ngobrol nih 🤔")

    if st.button("🔁 Ulangi Tes"):
        st.session_state.jawaban_kamu = []
        st.session_state.index = 0
        st.session_state.mulai = False
        st.experimental_rerun()

st.markdown("""
---
<p style='text-align: center; color: gray;'>Game ini buat seru-seruan dan ngetes chemistry bareng pasangan 💞</p>
""", unsafe_allow_html=True)
