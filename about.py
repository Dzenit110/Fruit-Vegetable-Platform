import streamlit as st

def app():
     
     st.header(' :violet[Hakkımızda] ')
     st.write("""
              
      Bu projenin amacı, meyve ve sebzelerin sınıflandırılması için bir web uygulaması geliştirmektir. 
      Uygulama, söz konusu öğenin bir görüntüsünü yüklemesi gereken tüm kullanıcılar tarafından erişilebilir olacak şekilde tasarlanmıştır.
      Sistem daha sonra görüntüyü otomatik olarak sınıflandırır ve meyve veya sebzenin adının bir tahminini sağlar. 
      Ayrıca, tahmin edilen nesneyle ilişkili kalorileri tahmin eden yeni bir modül de eklenmiştir. 
      Uygulama, herhangi bir tarayıcıdan doğrudan erişilebilen web tabanlı bir araçtır. 
      Projenin arka uçtaki işleyişini anlayabilmek için ilgili süreçleri incelemek gerekmektedir.
              

 Yapan Öğrenciler:
      Ahmet Melih Türkmen  ve
      Dzenit Vildic 


    """)
     st.image('./images/Screenshot_123.png')
     st.balloons() 