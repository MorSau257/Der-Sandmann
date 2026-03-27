import streamlit as st

# 1. Grafisches Grundgerüst
st.set_page_config(page_title="Der Sandmann - Mystery Game", page_icon="👁️", layout="centered")

# 2. Grusel-Design mit CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #e0e0e0; }
    .stButton>button { 
        width: 100%; 
        border: 1px solid #ff4b4b; 
        background-color: #1a1a1a; 
        color: white;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #ff4b4b; color: black; }
    h1, h2, h3 { color: #ff4b4b ! confession; font-family: 'Courier New', Courier, monospace; }
    </style>
    """, unsafe_allow_html=True)

# 3. Spiel-Logik
if 'page' not in st.session_state:
    st.session_state.page = 'intro'

def change_page(name):
    st.session_state.page = name

# --- SEITEN-INHALTE ---
if st.session_state.page == 'intro':
    st.title("👁️ DER SANDMANN")
    st.image("https://images.unsplash.com/photo-1509248961158-e54f6934749c?q=80&w=1000", caption="Das Trauma beginnt...")
    st.write("Ein Wetterglashändler hat dich besucht. Die Angst deiner Kindheit ist zurück.")
    if st.button("Erinnere dich an die Kindheit..."):
        change_page('kindheit')

elif st.session_state.page == 'kindheit':
    st.subheader("Wer ist der Sandmann?")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1516339901600-2e3a82dc50d4?w=400", caption="Die Mutter")
        if st.button("Frag die Mutter"):
            st.session_state.info = "mutter"
            change_page('labor')
    with col2:
        st.image("https://images.unsplash.com/photo-1583002623340-420286780996?w=400", caption="Die Kinderfrau")
        if st.button("Frag die Amme"):
            st.session_state.info = "amme"
            change_page('labor')

elif st.session_state.page == 'labor':
    st.subheader("Das dunkle Geheimnis")
    if st.session_state.info == "mutter":
        st.info("Sie beruhigt dich, aber die Schritte auf der Treppe lügen nicht.")
    else:
        st.error("Sie erzählt von blutigen Augen, die an Mondkinder verfüttert werden.")
    
    st.write("Du schleichst dich ins Arbeitszimmer. Coppelius und dein Vater arbeiten an Flammen...")
    st.image("https://images.unsplash.com/photo-1532187875302-1df92649edde?w=600", caption="Der glühende Herd")
    
    if st.button("Der Wahnsinn beginnt: Spring zum Studium..."):
        change_page('olympia')

elif st.session_state.page == 'olympia':
    st.subheader("Die Holzpuppe")
    st.write("Du triffst Olimpia. Sie ist schön, starr und sagt nur: 'Ach, ach!'")
    st.image("https://images.unsplash.com/photo-1543157145-f78c636d023d?w=600", caption="Olimpia")
    if st.button("Die Wahrheit sehen"):
        change_page('finale')

elif st.session_state.page == 'finale':
    st.subheader("Der Turm des Wahnsinns")
    st.write("Du stehst auf dem Turm. Unten wartet Coppelius. Deine Augen brennen.")
    st.image("https://images.unsplash.com/photo-1473163928189-3f4b2c4e3547?w=600", caption="Der Abgrund")
    st.error("Willst du wissen, wie Nathanael fällt?")
    st.button("LIES DAS BUCH FÜR DAS FINALE!")
    if st.button("Zurück zum Start"):
        change_page('intro')