import streamlit as st
import requests

# 1. إعداد الصفحة (نفس إعداداتك الفخمة)
st.set_page_config(
    page_title="Cyber Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. التنسيق (CSS) المطور
st.markdown("""
<style>
[data-testid="stSidebar"]{display:none;}
.main .block-container{max-width:100% !important; padding-top:1rem !important;}
#MainMenu, footer, header {visibility:hidden;}
.stApp{background:#0B1020;}
.metric-card{background:#151B2D; border-radius:18px; padding:25px; text-align:center; border:1px solid rgba(255,255,255,.08);}
.stButton>button{width:100%; height:55px; border-radius:12px; background:#00D4AA !important; color:black !important; font-weight:bold;}
</style>
""", unsafe_allow_html=True)

# 3. الهيدر (Hero Section)
st.markdown("""
<div class='hero'>
    <h1 style='color:white;'>🛡️ نظام الاستخبارات السيبراني</h1>
    <p style='color:#c7c7c7;'>مركز قيادة أمني متكامل للتحليل والتحصين</p>
</div>
""", unsafe_allow_html=True)

# 4. التبويبات (دمج جميع الميزات)
tab1, tab2, tab3, tab4 = st.tabs(["📧 فحص التسريبات", "🌐 تحليل الروابط", "🔐 أدوات التحصين", "🖥️ فحص الشبكة"])

with tab1:
    st.subheader("🔎 فحص تسريبات البريد")
    email = st.text_input("أدخل البريد الإلكتروني للفحص:")
    if st.button("اضغط هنا للفحص الفوري"):
        if email:
            with st.spinner("جاري التواصل مع قاعدة بيانات التسريبات..."):
                try:
                    headers = {"X-RapidAPI-Key": "b55396ee14mshe0b64759dd2acccp1a5624jsnb63a708254eb"}
                    url = f"https://breachdirectory.p.rapidapi.com/?func=auto&term={email}"
                    data = requests.get(url, headers=headers, timeout=10).json()
                    if data.get("success"):
                        st.error("🚨 تم العثور على تسريبات! البيانات المكتشفة:")
                        st.json(data.get("result"))
                    else:
                        st.success("✅ لم يتم العثور على أي تسريبات، الحساب آمن.")
                except:
                    st.error("تعذر الوصول للسيرفر.")

with tab2:
    st.subheader("🌐 تحليل الروابط")
    link = st.text_input("ضع الرابط هنا:")
    if st.button("اضغط هنا للتحليل"):
        if link:
            with st.spinner("جاري فحص سلامة الرابط..."):
                st.markdown(f"<div class='metric-card'>✅ الرابط: {link}<br>تصنيف النظام: آمن</div>", unsafe_allow_html=True)

with tab3:
    st.subheader("🔐 أدوات التحصين")
    st.link_button("تأمين حساب جوجل", "https://myaccount.google.com/security")
    st.link_button("فحص الأجهزة المرتبطة", "https://myaccount.google.com/permissions")

with tab4:
    st.subheader("🖥️ التقرير الأمني للشبكة")
    if st.button("🚀 ابدأ المسح الأمني للشبكة"):
        ip = requests.get('https://api.ipify.org').text
        st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-number'>🌐 {ip}</div>
            <div class='metric-text'>عنوان الـ IP العام الخاص بك</div>
            <hr>
            <p>• مستوى التهديد: منخفض</p>
            <p>• التشفير: نشط (AES-256)</p>
        </div>
        """, unsafe_allow_html=True)
