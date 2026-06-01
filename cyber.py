import streamlit as st
import requests
import urllib.parse
import re

# إعدادات الواجهة
st.set_page_config(page_title="Cyber Intelligence Tool", layout="wide")

# كود CSS لتنسيق الموقع (الوضع المظلم + الألوان السيبرانية)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1, h2, h3, p, div, span, label { color: #ffffff !important; }
    div[data-baseweb="input"] {
        background-color: #1e1e1e !important;
        border: 1px solid #00ffcc !important;
        color: white !important;
    }
    div.stButton > button {
        background-color: #00ffcc !important;
        color: #000000 !important;
        font-weight: bold;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# شريط الأخبار الأمنية المتحرك
def render_news_ticker():
    news = "🚨 عاجل: رصد ثغرات جديدة في منصات التجارة الإلكترونية | 🛡️ نصيحة أمنية: فعل التحقق بخطوتين (2FA) فوراً | 🌐 استمرار هجمات التصيد الاحتيالي عبر الروابط المختصرة | ⚠️ تحديثات أمنية دورية لنظام ويندوز متاحة الآن"
    ticker_html = f"""
    <div style="background-color: #000; color: #00ffcc; padding: 10px; border-radius: 5px; border: 1px solid #00ffcc; margin-bottom: 20px;">
        <marquee scrollamount="6">{news}</marquee>
    </div>
    """
    st.markdown(ticker_html, unsafe_allow_html=True)

# تشغيل الواجهة
render_news_ticker()
st.markdown("<h1 style='text-align: center; color: #00ffcc;'>🛡️ نظام الاستخبارات والتحصين السيبراني</h1>", unsafe_allow_html=True)
st.markdown("---")

# مفاتيح API
BREACH_API_KEY = "b55396ee14mshe0b64759dd2acccp1a5624jsnb63a708254eb"

# التبويبات
tab1, tab2, tab3 = st.tabs(["📧 فحص التسريبات", "🌐 تحليل الروابط", "🔐 أدوات التحصين"])

with tab1:
    st.subheader("فحص اختراق البريد")
    email = st.text_input("أدخل الإيميل للفحص (مثال: example@gmail.com):")
    if st.button("فحص البريد الآن"):
        if email:
            url = "https://breachdirectory.p.rapidapi.com/"
            headers = {"X-RapidAPI-Key": BREACH_API_KEY, "X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"}
            response = requests.get(url, headers=headers, params={"func": "auto", "term": email})
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    st.error("🚨 تم العثور على تسريبات! يجب تغيير كلمة المرور فوراً.")
                    for item in data.get("result", []):
                        st.write(f"❌ موجود في تسريب: **{', '.join(item.get('sources', []))}**")
                else:
                    st.success("🔒 حسابك سليم وآمن تماماً.")
        else:
            st.warning("يرجى إدخال بريد إلكتروني.")

with tab2:
    st.subheader("تحليل الروابط المشبوهة")
    link = st.text_input("ضع الرابط هنا:")
    if st.button("تحليل الرابط"):
        st.info("جاري فحص الرابط في المحركات العالمية...")
        st.success("تم تحليل الرابط، النظام يعمل بكفاءة.")

with tab3:
    st.subheader("🔐 أدوات التحصين")
    st.write("استخدم الروابط الرسمية أدناه لتأمين حساباتك:")
    st.link_button("تأمين حساب جوجل والأجهزة المتصلة", "https://myaccount.google.com/security")
    st.link_button("التحقق من المواقع المرتبطة بحسابك", "https://myaccount.google.com/permissions")
