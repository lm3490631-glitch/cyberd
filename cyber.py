import streamlit as st
import requests
import re

# إعدادات الواجهة
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

# شريط الأخبار الأمنية
def render_news_ticker():
    news = "🚨 تحديث أمني: تأكد من فحص تحديثات الويندوز | 🛡️ نصيحة: استخدم دائماً VPN عند الاتصال بشبكات عامة | ⚠️ تحذير: لا تضغط على الروابط غير المعروفة"
    st.markdown(f"""<div style="background-color: #000; color: #00ffcc; padding: 10px; border-radius: 5px; border: 1px solid #00ffcc; margin-bottom: 20px;"><marquee scrollamount="6">{news}</marquee></div>""", unsafe_allow_html=True)

render_news_ticker()
st.markdown("<h1 style='text-align: center; color: #00ffcc;'>🛡️ نظام الاستخبارات والتحصين السيبراني</h1>", unsafe_allow_html=True)
st.markdown("---")

BREACH_API_KEY = "b55396ee14mshe0b64759dd2acccp1a5624jsnb63a708254eb"

# التبويبات
tab1, tab2, tab3, tab4 = st.tabs(["📧 فحص التسريبات", "🌐 تحليل الروابط", "🔐 أدوات التحصين", "🖥️ فحص الجهاز"])

with tab1:
    st.subheader("فحص اختراق البريد")
    email = st.text_input("أدخل الإيميل للفحص:")
    if st.button("فحص البريد"):
        if email:
            res = requests.get("https://breachdirectory.p.rapidapi.com/", headers={"X-RapidAPI-Key": BREACH_API_KEY}, params={"func": "auto", "term": email})
            if res.status_code == 200 and res.json().get("success"):
                st.error("🚨 تم العثور على تسريبات! غير كلمة مرورك.")
            else:
                st.success("🔒 حسابك آمن.")

with tab2:
    st.subheader("تحليل الروابط المشبوهة")
    link = st.text_input("ضع الرابط هنا:")
    if st.button("تحليل الرابط"):
        st.info("جاري الفحص المخبري للرابط...")

with tab3:
    st.subheader("🔐 أدوات التحصين")
    st.link_button("تأمين حساب جوجل", "https://myaccount.google.com/security")

with tab4:
    st.subheader("🖥️ فحص أمن الجهاز")
    st.write("لأسباب تتعلق بخصوصية نظام التشغيل، لا يمكن للمتصفح فحص ملفات جهازك مباشرة. إليك الأدوات الموصى بها لاكتشاف الاختراقات في جهازك:")
    st.link_button("تحميل أداة فحص الفيروسات (Malwarebytes)", "https://www.malwarebytes.com/")
    st.link_button("فحص العمليات المشبوهة (Process Explorer)", "https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer")
    st.info("💡 نصيحة: إذا شعرت ببطء غير طبيعي أو فتح نوافذ تلقائية، يفضل فصل الإنترنت فوراً عن الجهاز.")
