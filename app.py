import streamlit as st
import time

# Seite konfigurieren
st.set_page_config(page_title="Der Sandmann", page_icon="📜")

# --- CSS: DAS ULTIMATIVE 180° UMBLÄTTER-DESIGN ---
st.markdown("""
    <style>
    /* Hintergrund: Holzplatte */
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/wood-pattern.png");
        background-color: #2b1d12;
    }

    /* Der Container, der die Drehung erlaubt (Perspective) */
    .book-container {
        perspective: 2000px;
        position: relative;
        margin: 20px auto;
        max-width: 650px;
        min-height: 550px;
    }

    /* Die Buchseite selbst */
    .paper {
        background-color: #f2e8cf;
        background-image: url("https://www.transparenttextures.com/patterns/parchment.png");
        padding: 45px;
        border-radius: 5px 25px 25px 5px;
        box-shadow: 25px 25px 60px rgba(0,0,0,1);
        border-left: 18px solid #3d2b1f; /* Buchrücken */
        
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        
        /* Start-Animation: Aufklappen (von 180° auf 0°) */
        animation: pageOpen 1.2s ease-out forwards;
        transform-origin: left center;
        backface-visibility: hidden; /* Versteckt die Rückseite, wenn sie weggedreht ist */
    }

    /* Die Geisterhand-Animation: Das Blatt kommt von links (180°) und legt sich flach (0°) */
    @keyframes pageOpen {
        0% { transform: rotateY(-180deg); opacity: 0; }
        10% { opacity: 1; } /* Wird schnell sichtbar */
        100% { transform: rotateY(0deg); opacity: 1; }
    }

    /* Schriftart & Farben (wie gehabt) */
    @import url('https://fonts.googleapis.com/css2?family=Special+Elite&display=swap');
    
    .paper div, p, h1, h2, h3 {
        font-family: 'Special Elite', serif !important;
        color: #261a15 !important;
    }

    h1 { border-bottom: 2px solid #d4c5a1; padding-bottom: 10px; text-align: center; }

    /* Button-Styling (angepasst, damit sie zum Buch passen) */
    .stButton>button {
        background-color: #d4c5a1 !important;
        color: #261a15 !important;
        border: 1px solid #261a15 !important;
        font-family: 'Special Elite', serif !important;
        border-radius: 0px !important;
        height: 3em;
        width: 100%;
        margin-top: 15px;
    }
    .stButton>button:hover {
        background-color: #261a15 !important;
        color: #f2e8cf !important;
    }
    
    /* Versteckt Streamlit-UI */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- LOGIK ---
if 'page' not in st.session_state:
    st.session_state.page = 'intro'

def change_page(name):
    # Wir speichern die alte Seite, um sie kurz "wegzudrehen"
    st.session_state.page = name
    st.rerun()

# --- DER INHALT (IM NEUEN 180° CONTAINER) ---
st.markdown('<div class="book-container">', unsafe_allow_html=True)

# Der Trick: Da wir nur st.markdown nutzen, wird das CSS-Element 'paper'
# bei jedem Klick neu erstellt. Die Animation pageOpen (von -180° auf 0°)
# wird also bei jedem Seitenwechsel abgespielt. Das sieht aus wie das
# Aufklappen der neuen Seite.

if st.session_state.page == 'intro':
    content = """
    <h1>📜 DER SANDMANN</h1>
    <p>D. 19. November.</p>
    <p><i>»Gewiß bist Du voll Unruhe, daß ich so lange nicht geschrieben... Etwas Entsetzliches ist in mein Leben getreten!«</i></p>
    <p>Ein Wetterglashändler namens Coppola war hier. Sein bloßer Anblick hat mein Innerstes erschüttert.</p>
    """
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("Blättere zur Kindheit..."):
        change_page('kindheit')

elif st.session_state.page == 'kindheit':
    content = """
    <h2>Kapitel I: Das Trauma</h2>
    <p>Abends um neun Uhr rief die Mutter seufzend: »Der Sandmann kommt!«</p>
    <p>Wer ist dieser Mann? Die Mutter sagt, er sei nur eine Redensart, doch die Amme flüstert Schreckliches...</p>
    """
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Mutter fragen"):
            st.session_state.info = "mutter"; change_page('labor')
    with col2:
        if st.button("Amme fragen"):
            st.session_state.info = "amme"; change_page('labor')

elif st.session_state.page == 'labor':
    info_text = "Märchen." if st.session_state.info == "mutter" else "Eulenschnäbel."
    content = f"<h2>Kapitel II</h2><p>{info_text}</p><p>Hinter der Gardine siehst du Coppelius. Er schreit: »Augen her!«</p>"
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("Weiterlesen..."):
        change_page('olympia')

elif st.session_state.page == 'olympia':
    content = "<h2>Kapitel III</h2><p>Sie ist eine Maschine!</p>"
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("Zum Finale..."):
        change_page('finale')

elif st.session_state.page == 'finale':
    content = "<h2>Kapitel IV</h2><p>»Sköne Oke – Sköne Oke!«</p><p>Der Wahnsinn siegt.</p>"
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("Buch zuschlagen"):
        change_page('intro')

st.markdown('</div>', unsafe_allow_html=True)
