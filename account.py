import streamlit as st
import firebase_admin

from firebase_admin import credentials
from firebase_admin import auth


cred = credentials.Certificate('meyve-sebze-82a10-1a37dbcf5b47.json')
firebase_admin.initialize_app(cred)



def app():



    st.title('Hoşgeldiniz :violet[Meyve & Sebze] ')


    

    if 'kullanici' not in st.session_state:
        st.session_state.kullanici = ''
    if 'kullaniciemail' not in st.session_state:
        st.session_state.kullaniciemail = ''



    
    def f(): 
        try:
              kullanici = auth.get_user_by_email(email)
              
              
              st.write('Giriş Başarılı')
               
              st.session_state.kullanici = kullanici.uid
              st.session_state.kullaniciemail = kullanici.email
              
              st.session_state.signedout=True
              st.session_state.signout=True

    
        except:
         st.warning('Giriş Başarsız')

    def t():
         st.session_state.signout = False
         st.session_state.signedout = False
         st.session_state.kullanici=''





    if 'signedout' not in st.session_state:
        st.session_state.signedout=False
    if 'signout' not in st.session_state:
        st.session_state.signout=False

       


    if not st.session_state['signedout']:
            choice = st.selectbox('Giriş Yap/Kayıt Ol', ['Giris', 'Kayit Ol'])

         
  
            if choice == "Giris":
                    
                    email= st.text_input('Email Address')
                    sifre= st.text_input('Şifre', type='password')
                    
                    st.button('Giris', on_click=f)



            else:
                    
                    email= st.text_input('Email Address')
                    password= st.text_input('Şifre', type='password')
                    
                    kullanici = st.text_input('Kullancı adı giriniz')
                    
                    if st.button('Kayıt Ol'):
                        kullanici = auth.create_user(email = email, password=password, uid=kullanici)


                        st.success('Başarılı giriş yaptınız')
                        st.markdown('Artık email ve şifre ile giriş yapabilisiniz ')
                        st.balloons()

    if   st.session_state.signout:
         st.text('Adi' + st.session_state.kullanici)
         st.text('Email'+ st.session_state.kullaniciemail)
         st.button("Çıkış Yap", on_click=t)