import streamlit as st

# Seite konfigurieren
st.set_page_config(page_title="Der Sandmann - Chronik des Wahnsinns", page_icon="📜")

# --- CSS: DAS BEWÄHRTE DESIGN (Holz & Pergament) ---
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
    if st.session_state.story_choice == "mutter":
        detail = "Deine Mutter sagt: 'Es gibt keinen Sandmann, es heißt nur, dass ihr schläfrig seid.' Doch du hörst jeden Abend ein schweres Poltern auf der Treppe. Du glaubst ihr nicht."
    else:
        detail = "Die Amme flüstert: 'Er wirft Sand in Kinderaugen, bis sie blutig herausspringen.' Er füttert damit seine Kinder im Mond, die krumme Eulenschnäbel haben."
    
    content = f"""
    <h2>Das Arbeitszimmer</h2>
    <p>{detail}</p>
    <p>Mit zehn Jahren hältst du es nicht mehr aus. Du versteckst dich im Arbeitszimmer deines Vaters. Die Tür geht auf. Es ist der Advokat <b>Coppelius</b> – hässlich, mit knotigen Fäusten.</p>
    <p>Er und dein Vater arbeiten an einem glühenden Herd. Du siehst augenlose Gesichter!</p>
    <p>Coppelius entdeckt dich! Er zerrt dich zum Feuer und schreit: <b>'Augen her!'</b></p>
    """
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("1) Dein Vater fleht um Gnade: 'Meister, lass ihm die Augen!'"):
        navigate('studium')
    if st.button("2) Du versuchst verzweifelt zu fliehen, aber die Angst lähmt dich."):
        navigate('studium')

elif st.session_state.page == 'studium':
    content = """
    <h2>Studium und Coppola</h2>
    <p>Coppelius ließ deine Augen, aber er schraubte dir symbolisch Hände und Füße ab. Du wurdest ohnmächtig. Kurz darauf starb dein Vater bei einer Explosion. Coppelius verschwand spurlos.</p>
    <p>Jahre später. Du studierst in G. Ein Wetterglashändler namens <b>Coppola</b> taucht auf. Er sieht exakt aus wie Coppelius! Deine Angst kehrt zurück.</p>
    <p>Coppola bietet dir ein Perspektiv (Fernrohr) an. Kaufst du es?</p>
    """
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("1) Ja, du kaufst es, um den Professor gegenüber zu beobachten."):
        navigate('holzpuppe')
    if st.button("2) Nein, du wirfst ihn hinaus – doch sein Bild verfolgt dich."):
        navigate('holzpuppe')

elif st.session_state.page == 'holzpuppe':
    content = """
    <h2>Die Holzpuppe</h2>
    <p>Durch das Perspektiv erblickst du <b>Olimpia</b>, die Tochter des Professors. Sie ist wunderschön, aber völlig starr. Du verliebst dich in ihre Stille. Deine Verlobte Clara vergisst du völlig.</p>
    <p>Eines Tages hörst du Streit. Du stürmst in Spalanzanis Haus. Spalanzani und Coppola zerren an Olimpia. Es kracht – <b>sie ist aus Holz!</b></p>
    <p>Coppola raubt ihr die Augen und flieht. Sie war eine mechanische Puppe.</p>
    <p>Spalanzani wirft dir Olimpias blutige Glasaugen an die Brust: 'Nimm sie!'</p>
    """
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("1) Der Wahnsinn packt dich. Du versuchst den Professor zu würgen."):
        navigate('finale')
    if st.button("2) Du brichst schreiend zusammen und landest im Tollhaus."):
        navigate('finale')

elif st.session_state.page == 'finale':
    content = """
    <h2>Das Finale</h2>
    <p>Monate später scheinst du geheilt. Du bist wieder bei Clara. Ihr besteigt den Ratsturm der Stadt, um die Aussicht zu genießen.</p>
    <p>Clara zeigt auf etwas im Gebüsch. Du nimmst dein Perspektiv zur Hand... Im Glas erscheint Coppola! Der Wahnsinn bricht mit Gewalt wieder aus.</p>
    <p>Du schreist: <b>'Holzpüppchen dreh dich!'</b> und packst Clara, um sie in den Abgrund zu werfen.</p>
    """
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("1) Wirst du von Lothar in letzter Sekunde gestoppt?"):
        navigate('ende')
    if st.button("2) Springst du selbst in den Tod, als du Coppelius unten siehst?"):
        navigate('ende')

elif st.session_state.page == 'ende':
    content = """
    <h1 style="border:none;">DAS ENDE?</h1>
    <p style="text-align:center;">==================================</p>
    <p>Nathanaels Schicksal ist besiegelt. Doch wie genau endet der Sturz?</p>
    <p>Welche dunkle Gestalt steht unten in der Menge und lacht? Und was wurde aus Clara?</p>
    <p>Das wahre, unheimliche Ende von E.T.A. Hoffmann erfährst du nur im Buch.</p>
    <h3 style="text-align:center;">---> LIES DEN 'SANDMANN' ZU ENDE! <---</h3>
    <p style="text-align:center;">==================================</p>
    """
    st.markdown(f'<div class="paper">{content}</div>', unsafe_allow_html=True)
    if st.button("Zurück zum Anfang"):
        navigate('start')

st.markdown('</div>', unsafe_allow_html=True)
