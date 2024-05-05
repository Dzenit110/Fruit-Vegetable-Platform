import streamlit as st
from streamlit_option_menu import option_menu
import about, profil, home, trending, your_posts

st.set_page_config(
    page_title="Meyve&Sebze Sınıflandırma"
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='Meyve&Sebze Platform',
                options=['AnaSayfa','Profil','Calculator','Postlarım','Hakkımızda'],
                icons=['house-fill','person-circle','calculator-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
                    "icon": {"color": "white", "font-size": "23px"}, 
                    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"}
                }
            )

        for app_item in self.apps:
            if app == app_item['title']:
                app_item['function']()

if __name__ == '__main__':
    multi_app = MultiApp()
    multi_app.add_app('AnaSayfa', home.app)
    multi_app.add_app('Profil', profil.app)
    multi_app.add_app('Calculator', trending.run)  # Değişiklik burada
    multi_app.add_app('Hakkımızda', about.app)
    multi_app.add_app('Postlarım', your_posts.app)

    multi_app.run()
