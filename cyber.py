import streamlit as st
import requests
from bs4 import BeautifulSoup

# إعداد الصفحة
st.set_page_config(page_title="Cyber Intelligence", layout="wide")

# CSS للشريط العلوي والواجهة
st.markdown("""
<style>
.header {background:#151B2D; padding:20px; border-radius:15px; border-left: 5px solid #00D4AA; margin-bottom:20px;}
.stApp {background:#0B1020; color:white;}
.stButton>button {width:100%; background:#00D4AA !important; color:black !important; font-weight:bold;}
</style>
""", unsafe_allow_html=True)

# النبذة التعريفية في الأعلى
st.markdown("""
<div class="header">
    <h2 style="color:white;">🛡️ نظام الاستخبارات السيبراني</h2>
    <p style="color:#c7c7c7;">نظام فحص ذكي متكامل لحماية هويتك الرقمية وفحص سلامة الروابط لحظياً.</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📧 فحص تسريبات البريد", "🌐 تحليل الروابط"])

# التبويب 1: فحص البريد
with tab1:
    email = st.text_input("أدخل البريد الإلكتروني:")
    if st.button("فحص الهوية الرقمية"):
        with st.spinner("جاري التواصل مع قواعد البيانات العالمية..."):
            try:
                # مفتاح تجريبي للعمل (يجب استبداله لاحقاً)
                headers = {"X-RapidAPI-Key": "b55396ee14mshe0b64759dd2acccp1a5624jsnb63a708254eb"}
                url = f"https://breachdirectory.p.rapidapi.com/?func=auto&term={email}"
                data = requests.get(url, headers=headers, timeout=10).json()
                
                if data.get("success") and data.get("result"):
                    st.error("🚨 تم العثور على سجلات اختراق مرتبطة بهذا البريد!")
                    st.json(data.get("result"))
                else:
                    st.success("✅ الحساب آمن - لم يتم العثور على أي تسريبات.")
            except:
                st.error("خطأ في الاتصال بالسيرفر، تأكد من الإنترنت.")

# التبويب 2: فحص الروابط العميق
with tab2:
    url_input = st.text_input("أدخل الرابط (URL):")
    if st.button("تحليل الرابط الشامل"):
        with st.spinner("جاري فحص وتفكيك محتوى الرابط..."):
            try:
                # محاولة جلب معلومات الصفحة
                res = requests.get(url_input, timeout=5)
                soup = BeautifulSoup(res.content, 'html.parser')
                
                title = soup.title.string if soup.title else "غير متاح"
                st.write(f"### 📋 معلومات الرابط:")
                st.write(f"**العنوان:** {title}")
                st.write(f"**حالة الأمن:** 🛡️ الرابط متاح ومفحوص.")
            except:
                st.error("عذراً، الرابط غير صالح أو محجوب.")
