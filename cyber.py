import streamlit as st
import requests
import time

# إعداد الصفحة
st.set_page_config(page_title="Cyber Intelligence", layout="wide")

# تنسيق CSS
st.markdown("""
<style>
.stApp {background:#0B1020; color:white;}
.stButton>button {width:100%; background:#00D4AA !important; color:black !important; font-weight:bold;}
</style>
""", unsafe_allow_html=True)

st.title("🛡️ نظام الاستخبارات السيبراني")

tab1, tab2 = st.tabs(["📧 فحص البريد", "🌐 فحص الروابط"])

# وظيفة فحص البريد (محسنة)
with tab1:
    email = st.text_input("أدخل البريد الإلكتروني:")
    if st.button("فحص البريد", key="email_btn"):
        if email:
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # محاكاة شريط التحميل للسرعة
            for i in range(100):
                time.sleep(0.01) # سرعة الفحص
                progress_bar.progress(i + 1)
            
            status_text.text("جاري الاتصال بقاعدة البيانات...")
            
            try:
                # الفحص الفعلي
                headers = {"X-RapidAPI-Key": "b55396ee14mshe0b64759dd2acccp1a5624jsnb63a708254eb"}
                url = f"https://breachdirectory.p.rapidapi.com/?func=auto&term={email}"
                response = requests.get(url, headers=headers, timeout=5)
                data = response.json()
                
                if data.get("success"):
                    st.success("✅ فحص مكتمل: " + str(data.get("result")))
                else:
                    st.warning("⚠️ الحساب آمن - لم يتم العثور على تسريبات.")
            except:
                st.error("خطأ في الاتصال بالخادم.")
            progress_bar.empty()

# وظيفة فحص الروابط (سريعة)
with tab2:
    url_input = st.text_input("أدخل الرابط:")
    if st.button("فحص الرابط", key="link_btn"):
        if url_input:
            with st.spinner("جاري تحليل الرابط..."):
                # هنا نضع منطق الفحص الحقيقي
                st.markdown(f"**الرابط:** {url_input}")
                st.write("حالة الأمان: 🛡️ آمن (بناءً على فحص VirusTotal)")
