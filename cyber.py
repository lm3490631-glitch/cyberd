import streamlit as st
import requests
import urllib.parse
import time
import re
import socket

# إعدادات الواجهة
st.set_page_config(page_title="Cyber Intelligence Tool", layout="wide")

# كود CSS لتغيير الخلفية للأسود وفرض لون أبيض للنصوص
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
    }
    h1, h2, h3, p, div, span, label {
        color: #ffffff !important;
    }
    .stTabs [data-baseweb="tab-list"] button [data-baseweb="tab"] {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# كود شريط الأخبار
def render_news_ticker():
    news = "🚨 عاجل: رصد ثغرات جديدة في منصات التجارة الإلكترونية | 🛡️ نصيحة أمنية: فعل التحقق بخطوتين (2FA) فوراً"
    ticker_html = f"""
    <div style="background-color: #000; color: #00ffcc; padding: 10px; border-radius: 5px; border: 1px solid #00ffcc; margin-bottom: 20px;">
        <marquee scrollamount="6">{news}</marquee>
    </div>
    """
    st.markdown(ticker_html, unsafe_allow_html=True)

render_news_ticker()
st.markdown("<h1 style='text-align: center; color: #00ffcc;'>🛡️ نظام الاستخبارات والتحصين السيبراني</h1>", unsafe_allow_html=True)
st.markdown("---")

# الدوال البرمجية
VIRUSTOTAL_API_KEY = "e629c15676bcfbf170ec5b27d6854bacf231137123d81ebbd425c0048f955f34"
BREACH_API_KEY = "b55396ee14mshe0b64759dd2acccp1a5624jsnb63a708254eb"

# التبويبات
tab1, tab2, tab3 = st.tabs(["📧 فحص التسريبات", "🌐 تحليل الروابط", "🔐 أدوات التحصين"])

with tab1:
    st.subheader("فحص اختراق البريد")
    email = st.text_input("أدخل الإيميل للفحص:")
    if st.button("فحص البريد"):
        st.success("جاري الفحص...")

with tab2:
    st.subheader("تحليل الروابط المشبوهة")
    link = st.text_input("ضع الرابط هنا:")
    if st.button("فحص الرابط"):
        st.success("جاري التحليل...")

with tab3:
    st.subheader("🔐 أدوات التحصين")
    st.link_button("تأمين حساب جوجل", "https://myaccount.google.com/security")
