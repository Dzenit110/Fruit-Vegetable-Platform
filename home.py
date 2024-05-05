import streamlit as st
from firebase_admin import firestore

def app():
    if 'username' not in st.session_state or st.session_state.username == '':
        st.warning('Lütfen paylaşımı yapabilmek için önce giriş yapınız!!')
    else:
        if 'db' not in st.session_state:
            st.session_state.db = ''

        db = firestore.client()
        st.session_state.db = db

        ph = 'Paylaşım yapabilirsiniz' if st.session_state.username != '' else 'Lütfen paylaşım yapabilmek için giriş yapınız!!'
        post = st.text_area(label=' :orange[+ Yeni Paylaşım]', placeholder=ph, height=None, max_chars=500)
        if st.session_state.username != '' and st.button('Paylaş', use_container_width=20):
            if post != '':
                info = db.collection('Posts').document(st.session_state.username).get()
                if info.exists:
                    info = info.to_dict()
                    if 'Content' in info.keys():
                        pos = db.collection('Posts').document(st.session_state.username)
                        pos.update({u'Content': firestore.ArrayUnion([u'{}'.format(post)])})
                    else:
                        data = {"Content": [post], 'Username': st.session_state.username}
                        db.collection('Posts').document(st.session_state.username).set(data)
                else:
                    data = {"Content": [post], 'Username': st.session_state.username}
                    db.collection('Posts').document(st.session_state.username).set(data)

                st.success('Gönderi yüklendi!!')

        st.header(' :violet[Son Gönderiler] ')

        docs = db.collection('Posts').get()
        for doc in docs:
            d = doc.to_dict()
            try:
                 st.markdown("""
                <style>

                .stTextArea [data-baseweb=base-input] [disabled=""]{
                    # background-color: #e3d8c8;
                    -webkit-text-fill-color: white;
                }
                </style>
                """,unsafe_allow_html=True)
                 st.text_area(label=':green[Paylaşan kullanıcı:] '+':orange[{}]'.format(d['Username']), value=d['Content'][-1], height=20, disabled=True )
            except:
                pass

if __name__ == '__main__':
    app()