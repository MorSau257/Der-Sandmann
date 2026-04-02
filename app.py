import streamlit as st

# Seite konfigurieren
st.set_page_config(page_title="Der Sandmann", page_icon="📜")

# --- DAS REPARIERTE ANIMATIONS-CSS ---
st.markdown("""
    <style>
    /* Hintergrund: Holzplatte */
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/wood-pattern.png");
        background-color: #2b1d12;
    }

    /* Der Container für die 3D-Perspektive */
    .book-viewport {
        perspective: 2500px;
        display: flex;
        justify-content: center;
        padding: 40px 20px;
    }

    /* Die Buchseite */
    .paper {
        background-color: #f2e8cf;
        background-image: url("https://www.transparenttextures.com/patterns/parchment.png");
        padding: 50px;
        border-radius: 5px 25px 25px 5px;
        box-shadow: 25px 25px 60px rgba(0,0,0,1);
        border-left: 18px solid #3d2b1f;
        
        width: 100%;
        max-width: 700px;
        min-height: 600px;
        
        /* HIER IST DIE MAGIE: 180 Grad Drehung */
        transform-origin: left center;
        backface-visibility: hidden;
        animation: flipIn 1.2s cubic-bezier(0.15, 0.0, 0.3, 1.0) forwards;
    }

    @keyframes flipIn {
        0% { transform: rotateY(-180deg); opacity: 0; }
        30% { opacity: 1; }
        100% { transform: rotateY(0deg); opacity: 1; }
    }

    /* Schriftart & Styling */
    @import url('https://fonts.googleapis.com/css2?family=Special+Elite&display=swap');
    
    .paper, .stMarkdown, p, h1, h2, h3 {
        font-family: 'Special Elite', serif !important;
        color: #261a15 !important;
    }

    h1 { border-bottom: 2px solid #d4c5a1; padding-bottom: 10px; text-align: center; }

    /* Buttons passend zum Buch */
    .stButton>button {
        background-color: #d4c5a1 !important;
        color: #261a15 !important;
        border: 1px solid #261a15 !important;
        font-family: 'Special Elite', serif !important;
        border-radius: 0px !important;
        width: 100%;
        height: 3.5em;
        margin-top: 15px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #261a15 !important;
        color: #f2e8cf !important;
    }
    
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- LOGIK ---
if 'page' not in st.session_state:
    st.session_state.page = 'intro'

def change_page(name):
    st.session_state.page = name
    st.rerun()

# --- INHALT ---
st.markdown('<div class="book-viewport">', unsafe_allow_html=True)

# Wir nutzen f-Strings, um für jede Seite eine eindeutige ID zu vergeben. 
# Das zwingt den Browser, die Animation jedes Mal neu zu starten.
if st.session_state.page == 'intro':
    content = """<h1>📜 DER SANDMANN</h1><p>D. 19. November.</p><p><i>»Gewiß bist Du voll Unruhe...«</i></p>"""
    st.markdown(f'<div class="paper" id="p1">{content}</div>', unsafe_allow_html=True)
    if st.button("Das Buch aufschlagen"):
        change_page('kindheit')

elif st.session_state.page == 'kindheit':
    content = """<h2>Kapitel I: Die Angst</h2><p>Um neun Uhr klopft es. »Der Sandmann kommt!«</p>"""
    st.markdown(f'<div class="paper" id="p2">{content}</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Mutter fragen"):
            st.session_state.info = "mutter"; change_page('labor')
    with col2:
        if st.button("Amme fragen"):
            st.session_state.info = "amme"; change_page('labor')

elif st.session_state.page == 'labor':
    info = "Ein Märchen." if st.session_state.info == "mutter" else "Er frisst Augen."
    content = f"<h2>Kapitel II</h2><p>{info}</p><p><b>»Augen her!«</b></p>"
    st.markdown(f'<div class="paper" id="p3">{content}</div>', unsafe_allow_html=True)
    if st.button("Jahre später..."):
        change_page('olympia')

elif st.session_state.page == 'olympia':
    content = "<h2>Kapitel III</h2><p>Die Augen liegen auf dem Boden. Kalte Glasmurmeln.</p>"
    st.markdown(f'<div class="paper" id="p4">{content}</div>', unsafe_allow_html=True)
    if st.button("Zum Finale..."):
        change_page('finale')

elif st.session_state.page == 'finale':
    content = "<h2>Kapitel IV</h2><p><b>»Ha! Sköne Oke – Sköne Oke!«</b></p>"
    st.markdown(f'<div class="paper" id="p5">{content}</div>', unsafe_allow_html=True)
    if st.button("Buch zuschlagen"):
        change_page('intro')

st.markdown('</div>', unsafe_allow_html=True)
