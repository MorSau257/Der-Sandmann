import streamlit as st

# Seite konfigurieren
st.set_page_config(page_title="Der Sandmann", page_icon="📜")

# --- CSS: DAS PAPIER-DESIGN ---
st.markdown("""
    <style>
    /* Hintergrund: Holzplatte */
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/wood-pattern.png");
        background-color: #2b1d12;
    }

    /* Das Papier-Gefäß (Container) */
    .book-page {
        background-color: #f2e8cf; 
        background-image: url("https://www.transparenttextures.com/patterns/parchment.png");
        padding: 50px;
        border-radius: 5px 20px 20px 5px;
        box-shadow: 20px 20px 50px rgba(0,0,0,0.9);
        border-left: 15px solid #3d2b1f;
        margin: 20px auto;
        min-height: 600px;
        animation: turnPage 1.2s ease-out;
    }

    @keyframes turnPage {
        0% { transform: perspective(1000px) rotateY(-15deg); opacity: 0; }
        100% { transform: perspective(1000px) rotateY(0deg); opacity: 1; }
    }

    /* Schriftart & Farben */
    @import url('https://fonts.googleapis.com/css2?family=Special+Elite&display=swap');
    
    .book-page, .stMarkdown, p, h1, h2, h3 {
        font-family: 'Special Elite', serif !important;
        color: #261a15 !important;
    }

    h1 { border-bottom: 2px solid #d4c5a1; padding-bottom: 10px; text-align: center; }

    /* Button-Styling */
    .stButton>button {
        background-color: #d4c5a1;
        color: #261a15;
        border: 1px solid #261a15;
        border-radius: 0px;
        width: 100%;
        margin-top: 10px;
    }
    .stButton>button:hover {
        background-color: #261a15;
        color: #f2e8cf;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SPIEL-LOGIK ---
if 'page' not in st.session_state:
    st.session_state.page = 'intro'

def change_page(name):
    st.session_state.page = name
    st.rerun()

# --- DER INHALT (JETZT IM PAPIER-CONTAINER) ---
with st.container():
    # Wir packen alles in ein <div> mit der Klasse 'book-page'
    st.markdown('<div class="book-page">', unsafe_allow_html=True)
    
    if st.session_state.page == 'intro':
        st.title("📜 DER SANDMANN")
        st.write("D. 19. November.")
        st.write("»Gewiß bist Du voll Unruhe, daß ich so lange nicht geschrieben... Etwas Entsetzliches ist in mein Leben getreten!«")
        st.write("Ein Wetterglashändler war hier. Sein Name: Coppola. Doch ich weiß, wer er wirklich ist.")
        if st.button("Blättere um..."):
            change_page('kindheit')

    elif st.session_state.page == 'kindheit':
        st.subheader("Kapitel I: Das Trauma")
        st.write("Abends um neun Uhr rief die Mutter: »Der Sandmann kommt!«")
        st.write("Du hörst das unheimliche Poltern auf der Treppe. Wer ist er?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Mutter fragen"):
                st.session_state.info = "mutter"; change_page('labor')
        with col2:
            if st.button("Amme fragen"):
                st.session_state.info = "amme"; change_page('labor')

    elif st.session_state.page == 'labor':
        st.subheader("Kapitel II: Coppelius")
        if st.session_state.info == "mutter":
            st.write("Sie sagte, er sei nur ein Märchen. Doch die Schritte lügten nicht.")
        else:
            st.write("Die Amme sprach von blutigen Augen, die er seinen Mondkindern füttert.")
        st.write("Du siehst ihn im Arbeitszimmer: Coppelius! Er schreit: »Augen her!«")
        if st.button("Weiterlesen..."):
            change_page('olympia')

    elif st.session_state.page == 'olympia':
        st.subheader("Kapitel III: Die Puppe")
        st.write("Du liebst Olimpia. Doch beim Streit zwischen Coppola und Spalanzani passiert es:")
        st.write("Ihre Augen fallen heraus. Sie sind nur aus Glas. Sie ist eine Holzpuppe!")
        if st.button("Zum Finale..."):
            change_page('finale')

    elif st.session_state.page == 'finale':
        st.subheader("Kapitel IV: Der Turm")
        st.write("Auf dem Ratsturm. Du blickst durch das Perspektiv.")
        st.write("Unten steht er. Coppelius.")
        st.markdown("### »Sköne Oke – Sköne Oke!«")
        st.write("Der Wahnsinn siegt. Willst du wissen, wie es endet?")
        st.info("Das wahre Ende steht in Hoffmanns Buch geschrieben.")
        if st.button("Buch zuschlagen"):
            change_page('intro')

    st.markdown('</div>', unsafe_allow_html=True)
