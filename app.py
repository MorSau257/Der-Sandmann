import streamlit as st

# Seite konfigurieren
st.set_page_config(page_title="Der Sandmann - Ein Nachtstück", page_icon="📜")

# CSS FIX: Damit das Papier (Buch) über dem Holz erscheint
st.markdown("""
    <style>
    /* Hintergrund: Holzplatte */
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/wood-pattern.png");
        background-color: #3d2b1f;
    }

    /* Das "Buch" / Die Papierseite */
    [data-testid="stVerticalBlock"] > div:first-child {
        background-color: #f4ecd8; /* Helles Papier */
        padding: 40px;
        border-radius: 5px;
        box-shadow: 15px 15px 30px rgba(0,0,0,0.8);
        border-left: 12px solid #d4c5a1; /* Buchrücken */
        margin: 20px auto;
        max-width: 700px;
        animation: turnPage 1s ease-out;
    }

    /* Animation für das Umblättern */
    @keyframes turnPage {
        0% { transform: rotateY(-15deg); opacity: 0; }
        100% { transform: rotateY(0deg); opacity: 1; }
    }

    /* Schriftart: Tinte / Special Elite */
    @import url('https://fonts.googleapis.com/css2?family=Special+Elite&display=swap');
    
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Special Elite', serif !important;
        color: #2c1e1a !important; /* Dunkle Tinte */
    }

    h1, h2, h3 {
        color: #1a0f0d !important;
        text-align: center;
        border-bottom: 1px solid #d4c5a1;
    }

    /* Buttons schöner machen */
    .stButton>button {
        background-color: #e2d1b3;
        color: #2c1e1a;
        border: 1px solid #2c1e1a;
        font-family: 'Special Elite', serif;
        border-radius: 2px;
    }
    </style>
    """, unsafe_allow_html=True)

# Spiel-Logik (wie gehabt)
if 'page' not in st.session_state:
    st.session_state.page = 'intro'

def change_page(name):
    st.session_state.page = name
    st.rerun()

# --- INHALT ---
if st.session_state.page == 'intro':
    st.title("📜 Der Sandmann")
    st.write("D. 19. November. [cite: 230]")
    st.write("*»Gewiß seid ihr alle voll Unruhe, daß ich so lange - lange nicht geschrieben.«* [cite: 248]")
    st.write("Ein Wetterglashändler namens Coppola ist erschienen. Er weckt dunkle Ahnungen eines gräßlichen Geschicks. [cite: 254, 258]")
    if st.button("Das Buch aufschlagen..."):
        change_page('kindheit')

elif st.session_state.page == 'kindheit':
    st.subheader("Kapitel I: Der Besucher")
    st.write("Abends um neun Uhr schlägt die Uhr. Die Mutter ruft: »Der Sandmann kommt!« [cite: 279, 280]")
    st.write("Du hörst das Poltern auf der Treppe. [cite: 281] Wem willst du glauben?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Glaube der Mutter"):
            st.session_state.info = "mutter"
            change_page('labor')
    with col2:
        if st.button("Glaube der Amme"):
            st.session_state.info = "amme"
            change_page('labor')

elif st.session_state.page == 'labor':
    st.subheader("Kapitel II: Die Beobachtung")
    if st.session_state.info == "mutter":
        st.write("Sie sagt, es gäbe keinen Sandmann. [cite: 284] Doch das Poltern bleibt.")
    else:
        st.write("Die Amme erzählt von den Kinderaugen, die Coppelius für seine Jungen im Mond raubt. [cite: 286]")
    
    st.write("Du versteckst dich im Arbeitszimmer. [cite: 313] Coppelius tritt ein. Er schwingt eine glutrothe Zange. [cite: 377, 385]")
    st.write("»Augen her! Augen her!«, dröhnt seine Stimme. [cite: 377, 387]")
    if st.button("Blättere weiter..."):
        change_page('olympia')

elif st.session_state.page == 'olympia':
    st.subheader("Kapitel III: Olimpia")
    st.write("Du liebst Olimpia. Doch ein Streit bricht aus. Spalanzani und Coppola zerren an ihr. [cite: 394]")
    st.write("Plötzlich siehst du: Es ist eine Puppe. Ihre Augen liegen als blutige Murmeln auf dem Boden.")
    if st.button("Zum Finale blättern..."):
        change_page('finale')

elif st.session_state.page == 'finale':
    st.subheader("Kapitel IV: Der Sprung")
    st.write("Du stehst auf dem Turm. Unten wartet Coppelius. [cite: 371]")
    st.write("Der Wahnsinn packt dich: »Ha! Sköne Oke – Sköne Oke!« [cite: 380, 394]")
    if st.button("Das Buch schließen"):
        change_page('intro')
