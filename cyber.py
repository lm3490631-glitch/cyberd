import streamlit as st
import re
import urllib.parse
import urllib.request

# إعدادات الصفحة
st.set_page_config(page_title="محلل الروابط السيبراني", page_icon="🛡️", layout="centered")

st.markdown("<h1 style='text-align: center; color: #00ffcc;'>🛡️ نظام فحص وتحليل الروابط السيبراني</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>قم بوضع الرابط في الأسفل لفحصه وتحليله مباشرة</p>", unsafe_allow_html=True)

# خانة إدخال الرابط
url_input = st.text_input("أدخل الرابط المراد فحصه:", placeholder="https://example.com")

if url_input:
    st.info("جاري تحليل الرابط... 🔎")
    
    # تنظيف الرابط
    url = url_input.strip()
    
    # 1. فحص الهيكل العام للرابط
    try:
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.netloc
        scheme = parsed_url.scheme
        
        st.write(f"**البروتوكول المستخدم:** {scheme.upper()}")
        st.write(f"**النطاق (Domain):** {domain}")
        
        # 2. فحص الأمان المبدئي (HTTPS)
        if scheme == "https":
            st.success("🔒 الرابط يستخدم بروتوكول آمن (HTTPS).")
        else:
            st.warning("⚠️ تحذير: الرابط يستخدم بروتوكول غير مشفر (HTTP)، قد يكون غير آمن!")
            
        # 3. فحص الكلمات الدلالية المشبوهة في الرابط
        phishing_keywords = ["login", "signin", "verify", "bank", "secure", "update", "free", "gift", "bonus"]
        found_keywords = [word for word in phishing_keywords if word in url.lower()]
        
        if found_keywords:
            st.error(f"🚨 تحذير عالي الخطورة: الرابط يحتوي على كلمات مشبوهة تستخدم في التصيد: {', '.join(found_keywords)}")
        else:
            st.success("✅ لم يتم العثور على كلمات مشبوهة صريحة في نص الرابط.")
            
    except Exception as e:
        st.error("❌ عذراً، الرابط المدخل غير صحيح أو غير مدعوم بالفحص السريع.")
