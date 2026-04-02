import streamlit as st

# Seite konfigurieren
st.set_page_config(page_title="Der Sandmann", page_icon="📜")

# --- CSS: DAS DESIGN (Bleibt gleich, Animation leicht verstärkt) ---
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/wood-pattern.png");
        background-color: #2b1d12;
    }

    /* Die Buchseite mit der Animation */
    .paper {
        background-color: #f2e8cf;
        background-image: url("https://www.transparenttextures.com/patterns/parchment.png");
        padding: 45px;
        border-radius: 5px 25px 25px 5px;
        box-shadow: 25px 25px 60px rgba(0,0,0,1);
        border-left: 18px solid #3d2b1f;
        margin-bottom: 25px;
        min-height: 500px;
        
        /* Animation-Einstellungen */
        animation: pageFlip 0.8s ease-out forwards;
        transform-origin: left center;
    }

    @keyframes pageFlip {
        0% { transform: perspective(1000px) rotateY(-20deg); opacity: 0; }
        100% { transform: perspective(1000px) rotateY(0deg); opacity: 1; }
    }

    .stMarkdown div, p, h1, h2, h3 {
        font-family: 'Special Elite', serif !important;
        color: #261a15 !important;
    }

    .stButton>button {
        background-color: #d4c5a1 !important;
        color: #261a15 !important;
        border: 1px solid #261a15 !important;
        font-family: 'Special Elite', serif !important;
        width: 100%;
    }
    
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Special+Elite&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# --- LOGIK ---
if 'page' not in st.session_state:
    st.session_state.page = 'intro'

def change_page(name):
    st.session_state.page = name
    st.rerun()

# --- DER INHALT ---
content = ""

# Der "Trick": Wir nutzen st.container und vergeben einen Key basierend auf der aktuellen Seite
# Das zwingt den Browser, das CSS-Element neu zu zeichnen
with st.container():
    if st.session_state.page == 'intro':
        content = """<h1>📜 DER SANDMANN</h1><p>D. 19. November.</p><p><i>»Gewiß bist Du voll Unruhe...«</i></p>"""
        st.markdown(f'<div class="paper" key="intro">{content}</div>', unsafe_allow_html=True)
        if st.button("Blättere zur Kindheit..."):
            change_page('kindheit')

    elif st.session_state.page == 'kindheit':
        content = """<h2>Kapitel I: Der Nachtbesucher</h2><p>Die Mutter rief: »Der Sandmann kommt!«</p>"""
        st.markdown(f'<div class="paper" key="kindheit">{content}</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Mutter fragen"):
                st.session_state.info = "mutter"; change_page('labor')
        with col2:
            if st.button("Amme fragen"):
                st.session_state.info = "amme"; change_page('labor')

    elif st.session_state.page == 'labor':
        info_text = "Märchen." if st.session_state.info == "mutter" else "Eulenschnäbel."
        content = f"<h2>Kapitel II</h2><p>{info_text}</p><p><b>»Augen her!«</b></p>"
        st.markdown(f'<div class="paper" key="labor">{content}</div>', unsafe_allow_html=True)
        if st.button("Jahre später..."):
            change_page('olympia')

    elif st.session_state.page == 'olympia':
        content = "<h2>Kapitel III</h2><p>Sie ist eine Maschine!</p>"
        st.markdown(f'<div class="paper" key="olympia">{content}</div>', unsafe_allow_html=True)
        if st.button("Zum Finale..."):
            change_page('finale')

    elif st.session_state.page == 'finale':
        content = "<h2>Kapitel IV</h2><h3>»Ha! Sköne Oke!«</h3>"
        st.markdown(f'<div class="paper" key="finale">{content}</div>', unsafe_allow_html=True)
        if st.button("Das Buch zuschlagen"):
            change_page('intro')
