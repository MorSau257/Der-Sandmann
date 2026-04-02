import streamlit as st

# Seite konfigurieren
st.set_page_config(page_title="Der Sandmann - Chronik des Wahnsinns", page_icon="📜")

# --- CSS: DESIGN (Unverändert, da es top aussah) ---
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/wood-pattern.png");
        background-color: #2b1d12;
    }
    .book-viewport {
        display: flex;
        justify-content: center;
        padding: 40px 20px;
    }
    .paper {
        background-color: #f2e8cf;
        background-image: url("https://www.transparenttextures.com/patterns/parchment.png");
        padding: 50px;
        border-radius: 5px 25px 25px 5px;
        box-shadow: 25px 25px 60px rgba(0,0,0,1);
        border-left: 18px solid #3d2b1f;
        width: 100%;
        max-width: 750px;
        min-height: 650px;
    }
    @import url('https://fonts.googleapis.com/css2?family=Special+Elite&display=swap');
    .paper, .stMarkdown, p, h1, h2, h3 {
        font-family: 'Special Elite', serif !important;
        color: #261a15 !important;
        line-height: 1.6;
    }
    h1 { border-bottom: 2px solid #d4c5a1; padding-bottom: 10px; text-align: center; font-size: 1.8em; }
    h2 { font-size: 1.4em; margin-top: 15px; border-bottom: 1px solid #d4c5a1; }
    
    .stButton>button {
        background-color: #d4c5a1 !important;
        color: #261a15 !important;
        border: 1px solid #261a15 !important;
        font-family: 'Special Elite', serif !important;
        width: 100%;
        height: 3.5em;
        margin-top: 10px;
    }
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- LOGIK-STEUERUNG ---
if 'page' not in st.session_state:
    st.session_state.page = 'start'
if 'story_choice' not in st.session_state:
    st.session_state.story_choice = None
if 'father_reaction' not in st.session_state:
    st.session_state.father_reaction = None
if 'professor_reaction' not in st.session_state:
    st.session_state.professor_reaction = None

def navigate(to):
    st.session_state.page = to
    st.rerun()

# --- DER INHALT ---
st.markdown('<div class="book-viewport">', unsafe_allow_html=True)

if st.session_state.page == 'start':
    content = """
    <h1>DER SANDMANN: DIE CHRONIK DES WAHNSINNS</h1>
    <p>Du bist Nathanael. Dein Leben wird von einem Schatten aus der Vergangenheit verfolgt.</p>
    <p>Alles beginnt in deiner Kindheit. Wenn es acht Uhr schlug, hieß es: <b>'Der Sandmann kommt!'</b></p>
    <p>Von wem willst du die Wahrheit über den Sandmann erfahren?</p>
    """
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("1) Von deiner Mutter (Die rationale Erklärung)"):
        st.session_state.story_choice = "mutter"
        navigate('arbeitszimmer')
    if st.button("2) Von der alten Kinderfrau (Die Schauergeschichte)"):
        st.session_state.story_choice = "amme"
        navigate('arbeitszimmer')

elif st.session_state.page == 'arbeitszimmer':
    detail = ("Deine Mutter sagt: 'Es gibt keinen Sandmann, es heißt nur, dass ihr schläfrig seid.' Doch du hörst jeden Abend ein schweres Poltern auf der Treppe." 
              if st.session_state.story_choice == "mutter" else 
              "Die Amme flüstert: 'Er wirft Sand in Kinderaugen, bis sie blutig herausspringen.' Er füttert damit seine Kinder im Mond.")
    
    content = f"""
    <h2>Das Arbeitszimmer</h2>
    <p>{detail}</p>
    <p>Mit zehn Jahren versteckst du dich im Arbeitszimmer. Ein Mann tritt ein: Der Advokat <b>Coppelius</b>. Er arbeitet mit deinem Vater an einem glühenden Herd.</p>
    <p>Coppelius entdeckt dich! Er zerrt dich zum Feuer und schreit: <b>'Augen her!'</b></p>
    """
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("1) Dein Vater fleht um Gnade: 'Meister, lass ihm die Augen!'"):
        st.session_state.father_reaction = "gnade"
        navigate('studium')
    if st.button("2) Du versuchst verzweifelt zu fliehen, aber die Angst lähmt dich."):
        st.session_state.father_reaction = "angst"
        navigate('studium')

elif st.session_state.page == 'studium':
    if st.session_state.father_reaction == "gnade":
        reaction_text = "Dein Vater wirft sich weinend vor Coppelius. 'Meister, lass ihm die Augen!', fleht er. Coppelius lacht hämisch, lässt dich aber los, nur um dir symbolisch Hände und Füße auszuschrauben."
    else:
        reaction_text = "Du starrst wie gebannt in die Flammen, unfähig dich zu bewegen. Coppelius packt dich grob: 'Schöne Augen! Schöne Augen!', murmelt er, während er dich fast in die Glut drückt, bevor er dich wie ein kaputtes Spielzeug wegwirft."
    
    content = f"""
    <h2>Studium in Gießen</h2>
    <p>{reaction_text}</p>
    <p>Kurz nach jener Nacht starb dein Vater bei einer Explosion. Coppelius verschwand spurlos.</p>
    <p>Jahre später studierst du in <b>Gießen</b>. Ein Wetterglashändler namens <b>Coppola</b> taucht auf. Er sieht exakt aus wie Coppelius! Er bietet dir ein Perspektiv an.</p>
    """
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("1) Ja, du kaufst es sofort."):
        navigate('holzpuppe')
    if st.button("2) Nein, du wirfst ihn voller Zorn hinaus!"):
        navigate('reue')

elif st.session_state.page == 'reue':
    content = """
    <h2>Die quälende Neugier</h2>
    <p>Du hast Coppola hinausgeworfen, doch sein Bild lässt dich nicht los. Die Angst mischt sich mit einer krankhaften Neugier.</p>
    <p>Nach Tagen der Unruhe suchst du Coppola heimlich auf und kaufst das Perspektiv doch noch. Du musst wissen, was sich hinter den Fenstern verbirgt.</p>
    """
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("Blicke durch das Glas..."):
        navigate('holzpuppe')

elif st.session_state.page == 'holzpuppe':
    content = """
    <h2>Die Holzpuppe</h2>
    <p>Durch das Perspektiv erblickst du <b>Olimpia</b>. Sie ist wunderschön, aber völlig starr. Eines Tages stürmst du in Spalanzanis Haus. Er und Coppola zerren an Olimpia. Es kracht – <b>sie ist aus Holz!</b></p>
    <p>Coppola raubt ihr die Augen und flieht. Spalanzani wirft dir Olimpias blutige Glasaugen an die Brust: 'Nimm sie!'</p>
    """
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("1) Der Wahnsinn packt dich. Du würgst den Professor."):
        st.session_state.professor_reaction = "wuergen"
        navigate('wahnsinn_text')
    if st.button("2) Du brichst schreiend zusammen und landest im Tollhaus."):
        st.session_state.professor_reaction = "zusammenbruch"
        navigate('wahnsinn_text')

elif st.session_state.page == 'wahnsinn_text':
    if st.session_state.professor_reaction == "wuergen":
        wahnsinn_desc = "Mit übermenschlicher Kraft stürzt du dich auf Spalanzani. 'Feuerkreis! Feuerkreis!', schreist du, während du versuchst, ihm das Leben auszupressen. Nur das Eingreifen der herbeieilenden Studenten rettet ihn vor deinem Zorn."
    else:
        wahnsinn_desc = "Ein gellender Schrei entfährt deiner Kehle. Die Realität zerbricht in tausend Scherben. Du fällst zu Boden, die blutigen Glasaugen in den Händen, und lachst hysterisch, während die Dunkelheit dich verschlingt."
    
    content = f"""
    <h2>Der Abgrund</h2>
    <p>{wahnsinn_desc}</p>
    <p>Man bringt dich weg. Es folgen dunkle Monate im Tollhaus von Gießen, fernab von Licht und Vernunft. Doch irgendwann scheinst du geheilt...</p>
    """
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("Zurück zu Clara..."):
        navigate('finale')

elif st.session_state.page == 'finale':
    content = """
    <h2>Das Finale</h2>
    <p>Alles scheint gut. Mit Clara besteigst du den Ratsturm. Du nimmst dein Perspektiv zur Hand... und im Glas erscheint Coppola!</p>
    <p>Der Wahnsinn bricht aus. Du schreist: <b>'Holzpüppchen dreh dich!'</b> und willst Clara in den Abgrund werfen.</p>
    """
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("1) Wirst du von Lothar gerettet?"):
        navigate('ende')
    if st.button("2) Springst du selbst in den Tod?"):
        navigate('ende')

elif st.session_state.page == 'ende':
    content = """
    <h1>DAS ENDE?</h1>
    <p>Nathanaels Schicksal ist besiegelt. Welche dunkle Gestalt steht unten und lacht?</p>
    <p>Das unheimliche Ende von E.T.A. Hoffmann erfährst du nur im Buch.</p>
    <h3 style="text-align:center;">---> LIES DEN 'SANDMANN'! <---</h3>
    """
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("Zurück zum Anfang"):
        navigate('start')

st.markdown('</div>', unsafe_allow_html=True)
