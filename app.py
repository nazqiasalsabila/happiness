import streamlit as st

st.set_page_config(page_title="Tes Cinta Romantis 💘", layout="centered")

if "mulai" not in st.session_state:
    st.session_state.mulai = False
if "jawaban_kamu" not in st.session_state:
    st.session_state.jawaban_kamu = []
if "index" not in st.session_state:
    st.session_state.index = 0

st.markdown("""
    <div style='text-align: center;'>
        <img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExd25lMWhuZHEyb3llMmpxb2V5NW9wbzN4cnUwcDZkNHdtbTJlaTdoZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hcUtVbt1y2BvW/giphy.gif' width='220'>
        <h1 style='color: #ff4b91; font-size: 45px; font-family: "Comic Sans MS", cursive;'>💘 Jelita 💖 Madut 💘</h1>
        <p style='font-size:22px; color: #ffaaff; font-style: italic;'>A Love Quiz That’s Silly, Sweet, and Full of Heart 💌</p>
        <p style='font-size:18px; color: #ccc;'>Let’s see how romantically synced you really are! 🌹</p>
    </div>
""", unsafe_allow_html=True)

if not st.session_state.mulai:
    if st.button("💖 Take the Test Now! 💖"):
        st.session_state.mulai = True
    st.stop()

pertanyaan = [
    ("1. <span style='font-size:22px;'>Kalau aku tiba-tiba nangis, kamu bakal...</span>", [
        "A. Panik dan ikut nangis",
        "B. Langsung peluk",
        "C. Nanya dulu, tapi tetep bingung"
    ]),
    ("2. <span style='font-size:22px;'>Pilihan kencan paling seru menurut kamu:</span>", [
        "A. Nonton film/ main game",
        "B. Ngobrol ngobrol di cafe",
        "C. Keliling keliling naik motor"
    ]),
    ("3. <span style='font-size:22px;'>Kalau aku bales chat cuma 'Hmm.', kamu akan...</span>", [
        "A. iya",
        "B. Bales: 'Oke.'",
        "C. Kirim stiker nyindir"
    ]),
    ("4. <span style='font-size:22px;'>Kalau lagi LDR, hal yang paling kamu butuhin adalah...</span>", [
        "A. Video call tiap malam",
        "B. kirim pap tiap waktu",
        "C. long teks romantis"
    ]),
    ("5. <span style='font-size:22px;'>Kamu tuh tipe pasangan yang...</span>", [
        "A. Gampang baper",
        "B. cuek tapi sayang",
        "C. Biasa aja"
    ]),
    ("6. <span style='font-size:22px;'>Kalau kita berantem, kamu bakal...</span>", [
        "A. Minta maaf duluan walau gak salah",
        "B. Ngilang dulu biar adem",
        "C. Kirim stiker lucu buat baikan"
    ]),
    ("7. <span style='font-size:22px;'>Kebiasaan kamu yang paling ngeselin tapi aku kangenin:</span>", [
        "A. Lupa bales padahal udah baca",
        "B. Ngasih kode tapi gak mau jujur langsung",
        "C. Tiba-tiba ngambek terus peluk"
    ]),
    ("8. <span style='font-size:22px;'>Kalau disuruh milih panggilan sayang:</span>", [
        "A. Bubup",
        "B. Sayang",
        "C. Nama-Nama Lucu"
    ]),
    ("9. <span style='font-size:22px;'>Kalau kita jadi karakter kartun, kamu bakal jadi...</span>", [
        "A. Spongebob: rame dan niat",
        "B. Shinchan: nakal tapi gemes",
        "C. Nobita: lemot tapi setia"
    ]),
    ("10. <span style='font-size:22px;'>Kalau aku ketiduran pas lagi video call...</span>", [
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
    st.markdown(f"<p>{tanya}</p>", unsafe_allow_html=True)
    pilihan = st.radio("", opsi, key=f"soal_{idx}")
    if st.button("Selanjutnya"):
        st.session_state.jawaban_kamu.append(pilihan.split('.')[0])
        st.session_state.index += 1
        st.rerun()
else:
    st.balloons()
    st.markdown("""
        <div style='text-align:center;'>
            <img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDlsN3R1d243NHRtZXZ4cGlhdjhrZ3FtemxhaGZzMDNxdXRmMmlmYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OF9VWbLZ5xCl2uSMJg/giphy.gif' width='250'>
            <h2 style='color:#ff69b4;'>Here’s your 💘 Love Compatibility Score 💘</h2>
        </div>
    """, unsafe_allow_html=True)
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
        st.rerun()

st.markdown("""
---
<p style='text-align: center; color: gray;'>This game is just for fun and to test your sweet chemistry 💞</p>
""", unsafe_allow_html=True)
