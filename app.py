import streamlit as st

# Seite konfigurieren
st.set_page_config(page_title="Der Sandmann - Ein Nachtstück", page_icon="📜", layout="centered")

# CSS für das "Echte Buch"-Gefühl
st.markdown("""
    <style>
    /* Hintergrund: Dunkles Holz */
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/wood-pattern.png");
        background-color: #2b1d12;
    }

    /* Das Buch-Papier */
    [data-testid="stVerticalBlock"] > div:first-child {
        background-color: #f2e8cf; /* Warmes Pergament */
        background-image: url("https://www.transparenttextures.com/patterns/parchment.png"); /* Papier-Struktur */
        padding: 60px 50px !important;
        border-radius: 3px 15px 15px 3px; /* Rechts abgerundet wie eine Buchseite */
        box-shadow: 20px 20px 40px rgba(0,0,0,0.9);
        border-left: 20px solid #3d2b1f; /* Dunkler Buchrücken */
        margin: 40px auto;
        max-width: 650px;
        min-height: 800px;
        animation: turnPage 1.5s ease-in-out;
        position: relative;
    }

    /* Animation: Leichtes Aufklappen */
    @keyframes turnPage {
        0% { transform: perspective(1000px) rotateY(-20deg); opacity: 0; }
        100% { transform: perspective(1000px) rotateY(0deg); opacity: 1; }
    }

    /* Schriftart: Alte Tinte */
    @import url('https://fonts.googleapis.com/css2?family=Special+Elite&display=swap');
    
    html, body, [class*="css"], .stMarkdown, p {
        font-family: 'Special Elite', serif !important;
        color: #261a15 !important;
        font-size: 1.1rem !important;
        line-height: 1.7 !important;
    }

    h1, h2 {
        color: #1a0f0d !important;
        text-align: center;
        border-bottom: 2px solid #d4c5a1;
        margin-bottom: 30px !important;
        padding-bottom: 15px !important;
    }

    /* Buttons als alte Etiketten */
    .stButton>button {
        background-color: #d4c5a1;
        color: #261a15;
        border: 1px solid #261a15;
        font-family: 'Special Elite', serif;
        border-radius: 0px;
        margin-top: 20px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        transition: all 0.3s;
    }

    .stButton>button:hover {
        background-color: #261a15;
        color: #f2e8cf;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# Spiel-Logik
if 'page' not in st.session_state:
    st.session_state.page = 'intro'

def change_page(name):
    st.session_state.page = name
    st.rerun()

# --- INHALT ---
if st.session_state.page == 'intro':
    st.title("📜 DER SANDMANN")
    st.write("D. 19. November.")
    st.write("»Gewiß bist Du voll Unruhe, daß ich so lange nicht geschrieben...«")
    st.write("Ein gräßliches Schicksal hat mich ereilt. Coppola, der Wetterglashändler... er ist es!")
    if st.button("Blättere um..."):
        change_page('kindheit')

elif st.session_state.page == 'kindheit':
    st.subheader("Die Kindheit")
    st.write("»Der Sandmann kommt!« - Du hörst die Tritte. Wer ist er?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Mutter fragen"):
            st.session_state.info = "mutter"
            change_page('labor')
    with col2:
        if st.button("Amme fragen"):
            st.session_state.info = "amme"
            change_page('labor')

elif st.session_state.page == 'labor':
    st.subheader("Das Versteck")
    if st.session_state.info == "mutter":
        st.write("Sie lächelte, aber du sahst die Furcht. Er kommt trotzdem.")
    else:
        st.write("Die Amme sprach von blutigen Augen und Eulenkindern im Mond.")
    
    st.write("Du versteckst dich. Coppelius tritt ein. 'Augen her! Augen her!'")
    if st.button("Das Trauma erleben..."):
        change_page('olympia')

elif st.session_state.page == 'olympia':
    st.subheader("Olimpia")
    st.write("Du blickst durch das Perspektiv. Die schöne Olimpia...")
    st.write("Plötzlich bricht der Streit aus. Spalanzani wirft dir Olimpias Augen an die Brust.")
    st.write("Sie sind aus Glas. Sie ist eine Puppe!")
    if st.button("Zum Wahnsinn blättern..."):
        change_page('finale')

elif st.session_state.page == 'finale':
    st.subheader("Das Ende")
    st.write("Auf dem Ratsturm. Clara zeigt dir die Aussicht. Du ziehst das Glas.")
    st.write("Da unten steht er: Coppelius.")
    st.markdown("### »Sköne Oke – Sköne Oke!«")
    if st.button("Das Buch zuschlagen"):
        change_page('intro')
