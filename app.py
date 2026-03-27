import streamlit as st

# Seite konfigurieren
st.set_page_config(page_title="Der Sandmann", page_icon="📜")

# --- DAS ULTIMATIVE BUCH-FIX CSS ---
st.markdown("""
    <style>
    /* Hintergrund: Holzplatte */
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/wood-pattern.png");
        background-color: #2b1d12;
    }

    /* Der Textbereich selbst wird zum Papier */
    .stMarkdown div, p, h1, h2, h3 {
        font-family: 'Special Elite', serif !important;
        color: #261a15 !important;
    }

    /* Wir erstellen eine Klasse für unsere Buchseite */
    .paper {
        background-color: #f2e8cf;
        background-image: url("https://www.transparenttextures.com/patterns/parchment.png");
        padding: 45px;
        border-radius: 5px 25px 25px 5px;
        box-shadow: 25px 25px 60px rgba(0,0,0,1);
        border-left: 18px solid #3d2b1f; /* Buchrücken */
        margin-bottom: 25px;
        min-height: 500px; /* Garantiert eine gewisse Höhe */
        animation: pageFlip 1s ease-out;
    }

    @keyframes pageFlip {
        0% { transform: perspective(1000px) rotateY(-10deg); opacity: 0; }
        100% { transform: perspective(1000px) rotateY(0deg); opacity: 1; }
    }

    /* Buttons stylen, damit sie zum Buch passen */
    .stButton>button {
        background-color: #d4c5a1 !important;
        color: #261a15 !important;
        border: 1px solid #261a15 !important;
        font-family: 'Special Elite', serif !important;
        border-radius: 0px !important;
        height: 3em;
        width: 100%;
    }
    
    /* Versteckt unnötiges Streamlit-Design am Rand */
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
# Wir nutzen eine einzige große Box ("paper"), in die wir den Text per f-String packen
content = ""

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
    <h2>Kapitel I: Der Nachtbesucher</h2>
    <p>Jeden Abend um neun Uhr hörtest du das schwere Trippeln auf der Treppe. Die Mutter seufzte: »Der Sandmann kommt!«</p>
    <p>Wer ist dieser Mann wirklich? Die Mutter beruhigt dich, doch die alte Amme weiß Schrecklicheres zu berichten...</p>
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
    info_text = "Die Mutter sagt, er sei nur eine Redensart. Doch das Poltern blieb real." if st.session_state.info == "mutter" else "Die Amme flüstert von Kinderaugen, die er als Speise für seine Brut im Mond raubt."
    content = f"""
    <h2>Kapitel II: Das Experiment</h2>
    <p>{info_text}</p>
    <p>Du versteckst dich hinter der Gardine im Arbeitszimmer. Ein Mann tritt ein: Der Advokat Coppelius.</p>
    <p>Er arbeitet an glühenden Kohlen. Plötzlich schreit er: <b>»Augen her! Augen her!«</b></p>
    """
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("Jahre später..."):
        change_page('olympia')

elif st.session_state.page == 'olympia':
    content = """
    <h2>Kapitel III: Die schöne Puppe</h2>
    <p>Du liebst die stille Olimpia. Doch ein Streit bricht aus zwischen Spalanzani und Coppola.</p>
    <p>Sie zerren an ihr, bis die Augen herausfallen – hohle Glasmurmeln auf dem Boden. Sie ist eine Maschine!</p>
    """
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("Zum Schicksalsturm..."):
        change_page('finale')

elif st.session_state.page == 'finale':
    content = """
    <h2>Kapitel IV: Der Abgrund</h2>
    <p>Du stehst auf dem hohen Ratsturm mit Clara. Du ziehst dein Perspektiv.</p>
    <p>Da unten... in der Menge... steht ER. Coppelius!</p>
    <p style="text-align: center; font-size: 1.5em;"><b>»Ha! Sköne Oke – Sköne Oke!«</b></p>
    <p>Der Wahnsinn kehrt zurück. Was nun geschieht, steht nur in den alten Büchern geschrieben.</p>
    """
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("Das Buch zuschlagen"):
        change_page('intro')
