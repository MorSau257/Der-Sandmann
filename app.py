import streamlit as st

# Seite konfigurieren
st.set_page_config(page_title="Der Sandmann - Ein Nachtstück", page_icon="📜")

# CSS für Holzplatte, Altes Buch und die "Umblätter-Animation"
st.markdown("""
    <style>
    /* Hintergrund: Holzplatte */
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/wood-pattern.png");
        background-color: #3d2b1f;
    }

    /* Das Buch / Papier */
    .main .block-container {
        background-color: #f4ecd8;
        padding: 50px;
        border-radius: 2px;
        box-shadow: 15px 15px 30px rgba(0,0,0,0.7);
        border-left: 15px solid #d4c5a1; /* Simuliert den Buchrücken */
        max-width: 750px;
        margin-top: 20px;
        
        /* HIER IST DIE GEISTERHAND-ANIMATION */
        animation: turnPage 1.2s ease-out;
    }

    @keyframes turnPage {
        0% { transform: rotateY(-10deg); opacity: 0; filter: sepia(100%); }
        100% { transform: rotateY(0deg); opacity: 1; filter: sepia(0%); }
    }

    /* Schriftart: Tinte */
    @import url('https://fonts.googleapis.com/css2?family=Special+Elite&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Special Elite', serif;
        color: #2c1e1a;
        line-height: 1.6;
    }

    h1, h2, h3 {
        color: #1a0f0d !important;
        text-align: center;
        text-decoration: underline;
    }

    /* Knöpfe als schlichte Tinte-Links */
    .stButton>button {
        background-color: transparent;
        color: #2c1e1a;
        border: 1px solid #2c1e1a;
        font-family: 'Special Elite', serif;
        width: 100%;
        transition: 0.5s;
    }

    .stButton>button:hover {
        background-color: #2c1e1a;
        color: #f4ecd8;
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
    st.title("📜 Der Sandmann")
    st.write("D. 19. November.")
    st.write("»Gewiß bist Du voll Unruhe, daß ich so lange nicht geschrieben...«")
    st.write("Ein Wetterglashändler war hier. Sein Name: Coppola. Doch ich weiß, wer er wirklich ist.")
    if st.button("Blättere um..."):
        change_page('kindheit')

elif st.session_state.page == 'kindheit':
    st.subheader("Kapitel I: Das Trauma")
    st.write("»Der Sandmann kommt!«, rief die Mutter um neun Uhr.")
    st.write("Du hörst das unheimliche Trippeln auf der Treppe. Wer ist dieses Wesen?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Frag die Mutter"):
            st.session_state.info = "mutter"
            change_page('labor')
    with col2:
        if st.button("Frag die Amme"):
            st.session_state.info = "amme"
            change_page('labor')

elif st.session_state.page == 'labor':
    st.subheader("Kapitel II: Die Beobachtung")
    if st.session_state.info == "mutter":
        st.write("Sie lächelte nur. Doch du sahst die Angst in ihren Augen.")
    else:
        st.write("»Er frisst die Augen der Kinder«, sagte die Amme mit hohler Stimme.")
    
    st.write("Hinter der Gardine siehst du es: Coppelius wirft glühende Körner in die Flammen.")
    st.write("»Augen her! Augen her!«, dröhnt es durch den Raum.")
    if st.button("Die Seite umschlagen..."):
        change_page('olympia')

elif st.session_state.page == 'olympia':
    st.subheader("Kapitel III: Die Puppe")
    st.write("Studentenzeit. Du liebst Olimpia. Ihr starrer Blick stört dich nicht.")
    st.write("Bis der Streit ausbricht. Spalanzani und Coppola zerren an ihr.")
    st.write("Ihre Augen fallen auf den Boden... Glas. Nur leeres Glas.")
    if st.button("Ins Verderben blättern..."):
        change_page('finale')

elif st.session_state.page == 'finale':
    st.subheader("Kapitel IV: Der Turm")
    st.write("Du stehst auf dem Ratsturm. Clara lächelt dich an.")
    st.write("Du nimmst das Perspektiv. Da unten... Coppelius!")
    st.markdown("### »Sköne Oke – Sköne Oke!«")
    st.write("Deine Hände zittern. Der Wahnsinn packt dich.")
    st.button("Lies das Ende im Reclam-Buch")
    if st.button("Zurück zum Anfang"):
        change_page('intro')
