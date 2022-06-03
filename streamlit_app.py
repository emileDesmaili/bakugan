import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_app.components import scrape_images, display_images


# PAGE SETUP
st.set_page_config(
    page_title="BakuGAN",
    layout="wide",
    page_icon="streamlit_app/assets/L_Old_London.png",

)

# with open("streamlit_app/navbar-bootstrap.html","r") as navbar:
#     st.markdown(navbar.read(),unsafe_allow_html=True)


# From https://discuss.streamlit.io/t/how-to-center-images-latex-header-title-etc/1946/4
with open("streamlit_app/style.css") as f:
    st.markdown("""<link href='http://fonts.googleapis.com/css?family=Roboto:400,100,100italic,300,300italic,400italic,500,500italic,700,700italic,900italic,900' rel='stylesheet' type='text/css'>""", unsafe_allow_html=True)
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


left_column, center_column,right_column = st.columns([1,3,1])

with left_column:
    st.info("**Demo** Project using streamlit")
with right_column:
    st.write("##### Authors\nThis tool has been developed by [Emile D. Esmaili](https://github.com/emileDesmaili)")
with center_column:
    st.image("streamlit_app/assets/app_logo.PNG")


side1, side2 = st.sidebar.columns([1,3])
with side1:
    st.image("streamlit_app/assets/midoryia.png", width=70)
with side2:
    st.write(f'# Welcome SuperUser')

page_container = st.sidebar.container()
with page_container:
    page = option_menu("Menu", ["Main Page", 'Image Bank','Model training'], 
    icons=['house','cash','dpad'], menu_icon="cast", default_index=0)

if "animes" not in st.session_state:
    st.session_state["animes"] = []



if page == "Main Page":
    st.title('First We Scrape!')
    with st.form('image scraping'):
        anime = st.text_input('Select anime')
        
        n_images = st.number_input('How many images?',1,1000)
        submitted = st.form_submit_button('Lets scrape!')
    if submitted:
        st.session_state["animes"].append(anime)
        scrape_images(anime, n_images)
        st.success('Scraping completed')
if page == 'Image Bank':
        animes = st.multiselect('Which animes to display?',set(st.session_state["animes"]))
        for anime in set(animes):
            st.write(f'#### {anime}')
            display_images(anime)