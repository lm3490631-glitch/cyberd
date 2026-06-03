import streamlit as st
import requests

# 1. إعداد الصفحة - يجب أن يكون أول سطر
st.set_page_config(page_title="Cyber Intelligence", layout="wide", initial_sidebar_state="collapsed")

# 2. التنسيق (CSS)
st.markdown("""
<style>
[data-testid="stSidebar"]{display:none;}
.stApp{background:#0B1020; color:white;}
.stButton>button{width:100%; height:50px; background:#00D4AA !important; color:black !important; font-weight:bold; border-radius:10px;}
</style>
""", unsafe_allow_html=True)

# 3. تعريف التبويبات (هذا الجزء كان يسبب الخطأ، تم إعادة تعريفه بوضوح)
tab1, tab2, tab3, tab4 = st.tabs(["📧 فحص", "🌐 روابط", "🔐 تحصين", "🖥️ شبكة"])

# 4. محتوى التبويبات
with tab1:
    st.subheader("🔎 فحص تسريبات البريد")
    email = st.text_input("أدخل البريد:")
    if st.button("فحص"):
        st.info("جاري الفحص...")

with tab2:
    st.subheader("🌐 تحليل الروابط")
    link = st.text_input("ضع الرابط:")
    if st.button("تحليل"):
        st.success("الرابط تحت الفحص.")

with tab3:
    st.subheader("🔐 أدوات التحصين")
    st.write("استخدم أدوات التحصين المتقدمة.")

with tab4:
    st.subheader("🖥️ فحص الشبكة")
    if st.button("بدء فحص الشبكة"):
        st.write("جاري مسح الشبكة...")
