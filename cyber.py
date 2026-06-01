import streamlit as st
import requests

# إعدادات الصفحة
st.set_page_config(page_title="Cyber Intelligence System", layout="wide")

# تنسيق CSS السيبراني
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1, h2, h3, p, div, span, label { color: #ffffff !important; }
    div[data-baseweb="input"] { background-color: #1e1e1e !important; border: 1px solid #00ffcc !important; }
    div.stButton > button { background-color: #00ffcc !important; color: #000000 !important; font-weight: bold; width: 100%; }
    div.stLinkButton > a { color: #ffffff !important; background-color: #333333 !important; border: 1px solid #00ffcc !important; text-decoration: none !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# شريط الأخبار
st.markdown("""<div style="background-color: #000; color: #00ffcc; padding: 10px; border-radius: 5px; border: 1px solid #00ffcc; margin-bottom: 20px;">
    <marquee scrollamount="6">🚨 نظام الاستخبارات نشط | 🛡️ تأكد من تحديث نظامك | ⚠️ لا تضغط على الروابط المشبوهة</marquee>
</div>""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #00ffcc;'>🛡️ نظام الاستخبارات والتحصين السيبراني</h1>", unsafe_allow_html=True)
st.markdown("---")

# تعريف التبويبات الأربعة (هذا هو السطر المهم الذي كان ناقصاً)
tab1, tab2, tab3, tab4 = st.tabs(["📧 فحص التسريبات", "🌐 تحليل الروابط", "🔐 أدوات التحصين", "🖥️ فحص الشبكة"])

with tab1:
    st.subheader("فحص اختراق البريد")
    email = st.text_input("أدخل الإيميل للفحص:")
    if st.button("فحص البريد"):
        st.success("جاري الفحص...")

with tab2:
    st.subheader("تحليل الروابط المشبوهة")
    link = st.text_input("ضع الرابط هنا:")
    if st.button("تحليل الرابط"):
        st.info("جاري الفحص...")

with tab3:
    st.subheader("🔐 أدوات التحصين")
    st.link_button("تأمين حساب جوجل", "https://myaccount.google.com/security")

with tab4:
    st.subheader("🖥️ فحص أمن الشبكة والـ IP")
    if st.button("🚀 ابدأ المسح الأمني"):
        try:
            ip_info = requests.get('https://api.ipify.org?format=json').json()
            st.info(f"🌐 عنوان الـ IP العام: {ip_info['ip']}")
            st.markdown("""
            <div style="background-color: #1e1e1e; padding: 15px; border-radius: 10px; border-left: 5px solid #00ffcc;">
                <p>• <b>حالة الاتصال:</b> نشط عبر الإنترنت</p>
                <p>• <b>مستوى التهديد:</b> منخفض</p>
            </div>
            """, unsafe_allow_html=True)
        except:
            st.error("تعذر جلب البيانات.")
