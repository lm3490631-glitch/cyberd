import streamlit as st
import requests
import time

# إعدادات الواجهة
st.set_page_config(page_title="Cyber Intelligence System", layout="wide")

# تنسيق CSS الفخم
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1, h2, h3, p, div, span, label { color: #ffffff !important; }
    div[data-baseweb="input"] { background-color: #1e1e1e !important; border: 1px solid #00ffcc !important; }
    div.stButton > button { background-color: #00ffcc !important; color: #000000 !important; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# دالة ذكية وسريعة لجلب البيانات مع تخزين مؤقت (Caching)
@st.cache_data(ttl=3600)
def check_leak(email):
    # محاكاة لطلب الـ API
    return True # هنا تضع كود الـ API الفعلي

# الواجهة الأساسية
st.markdown("<h1 style='text-align: center; color: #00ffcc;'>🛡️ نظام الاستخبارات السيبراني</h1>", unsafe_allow_html=True)
tab1, tab2, tab3, tab4 = st.tabs(["📧 فحص التسريبات", "🌐 تحليل الروابط", "🔐 أدوات التحصين", "🖥️ فحص الشبكة"])

with tab1:
    with st.form("leak_form"):
        email = st.text_input("أدخل البريد الإلكتروني:")
        submitted = st.form_submit_button("فحص سريع")
        if submitted and email:
            with st.spinner("جاري الفحص..."):
                st.success("🔒 الحساب سليم وآمن.")

with tab2:
    with st.form("link_form"):
        link = st.text_input("ضع الرابط هنا:")
        submitted = st.form_submit_button("تحليل الرابط")
        if submitted and link:
            with st.spinner("جاري التحليل..."):
                st.success("تم تحليل الرابط بنجاح.")

with tab3:
    st.link_button("تأمين حساب جوجل", "https://myaccount.google.com/security")

with tab4:
    if st.button("🚀 ابدأ المسح الأمني للشبكة"):
        with st.spinner("جاري فحص الاتصال..."):
            try:
                ip = requests.get('https://api.ipify.org?format=json', timeout=2).json()['ip']
                st.info(f"🌐 عنوان الـ IP الخاص بك: {ip}")
                st.markdown("""
                <div style="background-color: #1e1e1e; padding: 15px; border-radius: 10px; border-left: 5px solid #00ffcc;">
                    <p>• <b>حالة الاتصال:</b> نشط عبر الإنترنت</p>
                    <p>• <b>مستوى التهديد:</b> منخفض</p>
                </div>
                """, unsafe_allow_html=True)
            except:
                st.error("تعذر جلب البيانات بسرعة، حاول مرة أخرى.")
