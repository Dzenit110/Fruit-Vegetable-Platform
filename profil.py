import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
import json
import requests


cred = credentials.Certificate("meyve-sebze-82a10-1a37dbcf5b47.json")
firebase_admin.initialize_app(cred)
def app():

    st.title('Hoşgeldiniz Meyve🍍- Sebze🍅 Tanıma Uygulaması')

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''


    def sign_up_with_email_and_password(email, password, username=None, return_secure_token=True):
        try:
            rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"
            payload = {
                "email": email,
                "password": password,
                "returnSecureToken": return_secure_token
            }
            if username:
                payload["displayName"] = username 
            payload = json.dumps(payload)
            r = requests.post(rest_api_url, params={"key": "AIzaSyBIOM0-YMieMG0nk5GP2zepSZ0GTlRdxcc"}, data=payload)
            try:
                return r.json()['email']
            except:
                st.warning(r.json())
        except Exception as e:
            st.warning(f'Signup failed: {e}')

    def sign_in_with_email_and_password(email=None, password=None, return_secure_token=True):
        rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

        try:
            payload = {
                "returnSecureToken": return_secure_token
            }
            if email:
                payload["email"] = email
            if password:
                payload["password"] = password
            payload = json.dumps(payload)
            print('payload sigin',payload)
            r = requests.post(rest_api_url, params={"key": "AIzaSyBIOM0-YMieMG0nk5GP2zepSZ0GTlRdxcc"}, data=payload)
            try:
                data = r.json()
                user_info = {
                    'email': data['email'],
                    'username': data.get('displayName')  # Kullanicinın adı varsa gösterir
                }
                return user_info
            except:
                st.warning(data)
        except Exception as e:
            st.warning(f'Signin failed: {e}')

   
        try:
            rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode"
            payload = {
                "email": email,
                "requestType": "PASSWORD_RESET"
            }
            payload = json.dumps(payload)
            r = requests.post(rest_api_url, params={"key": "AIzaSyBIOM0-YMieMG0nk5GP2zepSZ0GTlRdxcc"}, data=payload)
            if r.status_code == 200:
                return True, "Sıfırla E-mail için E-mail gönderildi"
            else:
                
                error_message = r.json().get('error', {}).get('message')
                return False, error_message
        except Exception as e:
            return False, str(e)

    
           

    def f(): 
        try:

            userinfo = sign_in_with_email_and_password(st.session_state.email_input,st.session_state.password_input)
            st.session_state.username = userinfo['username']
            st.session_state.useremail = userinfo['email']

            
            global Usernm
            Usernm=(userinfo['username'])
            
            st.session_state.signedout = True
            st.session_state.signout = True    
  
            
        except: 
              st.warning('Giriş Başarsız')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''


    
    
        
    if "signedout"  not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False    
        

        
    
    if  not st.session_state["signedout"]: 
        choice = st.selectbox('Giriş Yap/Kayıt Ol',['Kayıt Ol','Giriş Yap'])
        email = st.text_input('E-Posta:')
        password = st.text_input('Şifre:',type='password')
        st.session_state.email_input = email
        st.session_state.password_input = password

        

        
        if choice == 'Kayıt Ol':
            username = st.text_input("Kullanıcı adi yazınız")
            
            if st.button('Kayıt Ol'):
                if len(password) < 6:
                  st.warning('Şifreniz en az 6 karakter olmalıdır.')
                else:
                    user = sign_up_with_email_and_password(email=email,password=password,username=username)
                
                    st.success('Hesap başarıyla oluşturuldu!')
                    st.markdown('Artık email ve şifre ile giriş yapabilisiniz ')
                    st.balloons()

        else:
                     
            st.button('Giriş Yap', on_click=f)
            
            
         

            
            
    if st.session_state.signout:
                st.text('Kullanici: '+st.session_state.username)
                st.text('Email:: '+st.session_state.useremail)
                st.button('Çıkış Yap', on_click=t) 
            
                
    

                            
    def ap():
        st.write('Gönderiler')