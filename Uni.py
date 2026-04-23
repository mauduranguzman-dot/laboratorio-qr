import streamlit as st
import qrcode
from io import BytesIO

st.title("Generador de QR - Laboratorio ICD")

nombre = st.text_input("Nombre Completo")
matricula = st.text_input("Matrícula")

if st.button("Generar Código QR"):
    if nombre and matricula:
        # Formato que lee tu sistema de la cámara
        datos = f"ALUMNO|{matricula}|{nombre}"
        
        qr = qrcode.make(datos)
        buf = BytesIO()
        qr.save(buf)
        
        st.image(buf.getvalue(), caption="Muestra este código en el laboratorio")
    else:
        st.error("Por favor llena ambos campos")