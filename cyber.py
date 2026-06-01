import streamlit as st
import requests
import urllib.parse
import time
import re
import socket

# إعدادات واجهة الأداة السيبرانية
st.set_page_config(page_title="تحليل المعلومات السيبرانية المحترف", page_icon="🛡️", layout="wide")
st.markdown("<h1 style='text-align: center; color: #00ffcc;'>🛡️ نظام الاستخبارات وفحص الروابط والبريد المتقدم</h1>", unsafe_allow_html=True)
st.markdown("---")

# مفاتيح الـ API العالمية 
VIRUSTOTAL_API_KEY = "e629c15676bcfbf170ec5b27d6854bacf231137123d81ebbd425c0048f955f34"
BREACH_API_KEY = "ضع_مفتاحك_الجديد_هنا"  # 👈 امسح هذه الجملة وضع مفتاحك السري الجديد هنا بين القوسين

# 1️⃣ دالة تحليل تفاصيل الرابط (البلد، نوع المنصة، طبيعة المحتوى)
def get_advanced_link_details(url_input):
    country_name = "سيرفر عالمي موزع (CDN)"
    platform_type = "🌐 موقع ويب مستقل / متجر إلكتروني"
    content_type = "📄 صفحة ويب رئيسية / واجهة موقع"

    try:
        parsed_url = urllib.parse.urlparse(url_input)
        domain = parsed_url.netloc if parsed_url.netloc else parsed_url.path.split('/')[0]
        path = parsed_url.path.lower()
        query = parsed_url.query.lower()

        domain_lower = domain.lower()
        if any(x in domain_lower for x in ['tiktok.com', 'instagram.com', 'twitter.com', 'x.com', 'youtube.com', 'snapchat.com', 'facebook.com']):
            platform_type = "📱 شبكات التواصل الاجتماعي / برامج تطبيقات الهاتف"
        elif "salla" in domain_lower or "s.salla.sa" in domain_lower:
            platform_type = "🛍️ منصة تجارة إلكترونية (تطبيق سلة)"

        if any(x in path or x in query for x in ['video', 'reel', 'clip', 'watch', 'shorts', '/p/', '/reel/', 'status']):
            content_type = "🎥 محتوى مرئي (فيديو / ريلز)"
        elif any(x in path for x in ['article', 'blog', 'news', 'post', 'wiki', '.html', '.php']) or len(path) > 15:
            content_type = "📝 محتوى قرائي (مقال / منشور نصي)"
        elif any(x in path for x in ['.jpg', '.jpeg', '.png', '.gif', 'image']):
            content_type = "🖼️ محتوى بصري (صورة / جرافيك)"

        ip_address = socket.gethostbyname(domain)
        geo_res = requests.get(f"https://ipapi.co/{ip_address}/json/", timeout=3)
        if geo_res.status_code == 200:
            country_name = geo_res.json().get("country_name", "غير مدرج")
    except:
        pass

    return country_name, platform_type, content_type

# 2️⃣ دالة فحص خروقات البريد الإلكتروني (بيانات حقيقية 100%)
def get_real_email_breach(email):
    url = "https://breachdirectory.p.rapidapi.com/"
    querystring = {"func": "auto", "term": email}
    headers = {
        "X-RapidAPI-Key": BREACH_API_KEY,
        "X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"
    }
    
    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get("success") and data.get("result"):
                return True, data["result"]
        return False, []
    except Exception as e:
        return None, []

# تقسيم واجهة الموقع إلى قسمين متوازيين
col1, col2 = st.columns(2)

# القسم الأول: فحص الروابط
with col1:
    st.header("🌐 فحص وتحليل الروابط العالمي")
    url_input = st.text_input("أدخل رابط الموقع الإلكتروني هنا:", placeholder="https://example.com")

    if st.button("تحليل الرابط عبر VirusTotal"):
        if url_input:
            if not url_input.startswith(('http://', 'https://')):
                url_input = 'https://' + url_input

            st.subheader("📊 تحليل معطيات الرابط الحيوية:")
            country, source_type, content_type = get_advanced_link_details(url_input)

            st.info(f"📍 **بلد المصدر (مقر السيرفر):** {country}")
            st.info(f"📂 **نوع المنصة والمصدر:** {source_type}")
            st.info(f"🔍 **طبيعة محتوى الرابط:** {content_type}")

            with st.spinner("جاري مطابقة الرابط مع المحركات العالمية..."):
                try:
                    post_url = "https://www.virustotal.com/api/v3/urls"
                    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
                    post_res = requests.post(post_url, data={"url": url_input}, headers=headers)

                    if post_res.status_code == 200:
                        analysis_id = post_res.json().get("data", {}).get("id")
                        analysis_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
                        time.sleep(3)
                        response = requests.get(analysis_url, headers=headers)

                        if response.status_code == 200:
                            stats = response.json().get("data", {}).get("attributes", {}).get("stats", {})
                            malicious = stats.get("malicious", 0)

                            st.markdown("### 🛡️ تقرير الأمان المخبري:")
                            if malicious > 0:
                                st.error(f"🚨 تحذير: الرابط مصنف كتهديد من قبل {malicious} محرك أمني!")
                            else:
                                st.success("✅ الرابط سليم وآمن 100% في الفحص المخبري.")
                except Exception as e:
                    st.error(f"خطأ أثناء الفحص: {e}")

# القسم الثاني: فحص تسريبات الجيميل الحقيقية
with col2:
    st.header("📧 فحص تسريبات وأمان البريد")
    email_input = st.text_input("أدخل حساب الجيميل المراد فحصه:", placeholder="username@gmail.com")

    if st.button("فحص الحساب الآن"):
        if email_input:
            if re.match(r"[^@]+@[^@]+\.[^@]+", email_input):
                st.subheader("📊 تقرير استخبارات التهديدات الحقيقي للبريد:")

                with st.spinner("جاري فحص وتتبع سجل الخروقات للبريد من الخوادم العالمية..."):
                    is_breached, results = get_real_email_breach(email_input)

                    if is_breached is None:
                        st.warning("⚠️ عذراً، هناك مشكلة مؤقتة في الاتصال بخادم الفحص العالمي.")
                    elif is_breached and len(results) > 0:
                        st.error(f"🚨 تحذير أمني: تم العثور على هذا البريد في خروقات وتسريبات حقيقية!")
                        
                        st.markdown("### 🏢 المنصات وقواعد البيانات التي سُرّب منها الحساب:")
                        sites_found = set()
                        data_types = set()
                        
                        for item in results:
                            if "sources" in item:
                                for src in item["sources"]:
                                    sites_found.add(src)
                            if "fields" in item:
                                for field in item["fields"]:
                                    data_types.add(field)
                        
                        for site in sites_found:
                            st.write(f"❌ مصنف في تسريب: **{site}**")
                            
                        st.markdown("### 🗂️ نوع البيانات المكشوفة في التسريب:")
                        st.warning(f"⚠️ البيانات التي انتشرت تشمل: {', '.join(data_types)}")
                        
                        st.markdown("> 💡 **نصيحة حماية سيبرانية:** إذا كنت تستخدم نفس كلمة مرور هذا التسريب في حساباتك الحالية، يرجى تغييرها فوراً وتفعيل التحقق بخطوتين (2FA) لحمايتك.")
                    else:
                        st.success("🔒 حسابك سليم وآمن تماماً! لم يتم رصد أي تسريبات حقيقية لهذا البريد في قواعد البيانات الحية.")
            else:
                st.error("الرجاء إدخال بريد إلكتروني صيغته صحيحة.")
        else:
            st.error("الرجاء إدخال البريد الإلكتروني أولاً.")
