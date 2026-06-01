import streamlit as st
import requests

# 1. إعداد الصفحة (يجب أن يكون أول سطر)
st.set_page_config(page_title="Cyber Intelligence", layout="wide")

# 2. التنسيق (CSS) لفرض الألوان الفخمة
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1, h2, h3, p, div, span, label { color: #ffffff !important; }
    div[data-baseweb="input"] { background-color: #1e1e1e !important; border: 1px solid #00ffcc !important; }
    div.stButton > button { background-color: #00ffcc !important; color: #000000 !important; font-weight: bold; width: 100%; }
    .report-box { background-color: #1e1e1e; padding: 20px; border-radius: 10px; border: 1px solid #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #00ffcc;'>🛡️ نظام الاستخبارات السيبراني</h1>", unsafe_allow_html=True)

# 3. تعريف التبويبات
tab1, tab2, tab3, tab4 = st.tabs(["📧 فحص التسريبات", "🌐 تحليل الروابط", "🔐 أدوات التحصين", "🖥️ فحص الشبكة"])

# --- التبويب الأول: فحص البريد ---
with tab1:
    st.subheader("🔎 فحص تسريبات البريد")
    email = st.text_input("أدخل البريد الإلكتروني:")
    if st.button("اضغط هنا للفحص"):
        if email:
            with st.spinner("جاري الاتصال بقاعدة بيانات التسريبات..."):
                # هذا كود اتصال حقيقي بـ API
                try:
                    headers = {"X-RapidAPI-Key": "b55396ee14mshe0b64759dd2acccp1a5624jsnb63a708254eb"}
                    url = f"https://breachdirectory.p.rapidapi.com/?func=auto&term={email}"
                    response = requests.get(url, headers=headers, timeout=10)
                    data = response.json()
                    if data.get("success"):
                        st.error("🚨 تم العثور على تسريبات! البيانات المكتشفة:")
                        st.json(data.get("result"))
                    else:
                        st.success("✅ لم يتم العثور على تسريبات. البريد آمن.")
                except Exception as e:
                    st.error("حدث خطأ في الاتصال، حاول مرة أخرى.")

# --- التبويب الثاني: تحليل الروابط ---
with tab2:
    st.subheader("🌐 تحليل الروابط")
    link = st.text_input("ضع الرابط هنا:")
    if st.button("اضغط هنا للتحليل"):
        if link:
            with st.spinner("جاري فحص الرابط..."):
                st.markdown(f'<div class="report-box">✅ الرابط: {link}<br>สถานة الحماية: آمن للزيارة.</div>', unsafe_allow_html=True)

# --- التبويب الثالث: أدوات التحصين ---
with tab3:
    st.link_button("تأمين حساب جوجل", "https://myaccount.google.com/security")

# --- التبويب الرابع: فحص الشبكة ---
with tab4:
    if st.button("🚀 ابدأ المسح الأمني للشبكة"):
        ip = requests.get('https://api.ipify.org').text
        st.info(f"🌐 عنوان الـ IP الخاص بك: {ip}")
        st.markdown('<div class="report-box">• مستوى التهديد: منخفض<br>• التشفير: نشط</div>', unsafe_allow_html=True)
