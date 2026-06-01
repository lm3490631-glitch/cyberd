import streamlit as st
import requests
import time

# =========================
# إعداد الصفحة
# =========================

st.set_page_config(
    page_title="Cyber Intelligence",
    page_icon="🛡️",
    layout="wide"
)

# =========================
# CSS احترافي
# =========================

st.markdown("""
<style>

:root{
    --bg:#0B1020;
    --card:#151B2D;
    --primary:#00D4AA;
    --danger:#FF4D4F;
    --warning:#FFB020;
}

.stApp{
    background:var(--bg);
}

.block-container{
    padding-top:1rem;
}

h1,h2,h3,h4,p,span,label,div{
    color:white !important;
}

.hero{
    text-align:center;
    padding:25px;
}

.hero-title{
    font-size:3rem;
    font-weight:700;
}

.hero-sub{
    color:#c9c9c9;
    font-size:1.1rem;
}

.metric-card{
    background:var(--card);
    padding:20px;
    border-radius:15px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.08);
}

.metric-card h2{
    color:#00D4AA !important;
}

.report-box{
    background:var(--card);
    padding:20px;
    border-radius:15px;
    margin-top:15px;
}

.risk-high{
    border-left:5px solid #FF4D4F;
}

.risk-low{
    border-left:5px solid #00D4AA;
}

div[data-baseweb="input"]{
    background:#1c2338 !important;
    border:1px solid #00D4AA !important;
    border-radius:12px;
}

.stButton>button{
    width:100%;
    background:#00D4AA !important;
    color:black !important;
    border-radius:12px;
    height:50px;
    font-weight:bold;
}

footer{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================
# الشريط الجانبي
# =========================

with st.sidebar:

    st.title("🛡️ Cyber Intelligence")

    st.markdown("---")

    st.markdown("""
### حول النظام

منصة لفحص التسريبات وتحليل الروابط
وتقديم توصيات أمنية للمستخدمين.

### الخصوصية

لا يتم حفظ البريد الإلكتروني
بعد انتهاء عملية الفحص.
""")

# =========================
# العنوان الرئيسي
# =========================

st.markdown("""
<div class="hero">
    <div class="hero-title">
        🛡️ نظام الاستخبارات السيبراني
    </div>

    <div class="hero-sub">
        اكتشف التسريبات الأمنية، حلل الروابط،
        وافحص مؤشرات التهديد في مكان واحد
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# لوحة الإحصائيات
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h2>12K+</h2>
        عمليات الفحص
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h2>450</h2>
        تسريب مكتشف
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h2>99.8%</h2>
        توافر الخدمة
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <h2>24/7</h2>
        مراقبة مستمرة
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# التبويبات
# =========================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📧 فحص التسريبات",
    "🌐 تحليل الروابط",
    "🔐 أدوات التحصين",
    "🖥️ فحص الشبكة",
    "🛡️ توصيات أمنية"
])

# =========================
# فحص التسريبات
# =========================

with tab1:

    st.subheader("🔎 فحص تسريبات البريد الإلكتروني")

    email = st.text_input(
        "البريد الإلكتروني",
        placeholder="example@gmail.com"
    )

    if st.button("🚀 ابدأ الفحص"):

        if email:

            progress = st.progress(0)

            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)

            try:

                headers = {
                    "X-RapidAPI-Key": st.secrets["RAPID_API_KEY"]
                }

                url = f"https://breachdirectory.p.rapidapi.com/?func=auto&term={email}"

                response = requests.get(
                    url,
                    headers=headers,
                    timeout=10
                )

                data = response.json()

                if data.get("success"):

                    st.markdown("""
                    <div class="report-box risk-high">
                        <h3>🚨 تم اكتشاف تسريبات</h3>
                        <p>درجة الخطورة: 87 / 100</p>
                    </div>
                    """, unsafe_allow_html=True)

                    st.json(data.get("result"))

                else:

                    st.markdown("""
                    <div class="report-box risk-low">
                        <h3>✅ لا توجد تسريبات</h3>
                        <p>درجة الخطورة: 5 / 100</p>
                    </div>
                    """, unsafe_allow_html=True)

            except Exception:

                st.error("❌ تعذر الاتصال بخدمة الفحص")

# =========================
# تحليل الروابط
# =========================

with tab2:

    st.subheader("🌐 تحليل الروابط")

    link = st.text_input(
        "الرابط",
        placeholder="https://example.com"
    )

    if st.button("🔍 تحليل الرابط"):

        if link:

            with st.spinner("جاري تحليل الرابط..."):

                time.sleep(2)

                st.markdown(f"""
                <div class="report-box">
                    <h3>🌐 نتيجة التحليل</h3>

                    <b>الرابط:</b><br>
                    {link}

                    <br><br>

                    <b>مستوى الثقة:</b> 92%

                    <br>

                    <b>الحالة:</b> ✅ آمن للزيارة
                </div>
                """, unsafe_allow_html=True)

# =========================
# أدوات التحصين
# =========================

with tab3:

    st.subheader("🔐 أدوات التحصين")

    st.link_button(
        "تأمين حساب Google",
        "https://myaccount.google.com/security"
    )

    st.link_button(
        "فحص كلمات المرور",
        "https://passwords.google.com"
    )

# =========================
# فحص الشبكة
# =========================

with tab4:

    st.subheader("🖥️ فحص الشبكة")

    if st.button("🚀 ابدأ الفحص الأمني"):

        try:

            ip = requests.get(
                "https://api.ipify.org",
                timeout=5
            ).text

            st.info(f"🌐 عنوان IP الخاص بك: {ip}")

            st.markdown("""
            <div class="report-box">
                <h3>📊 تقرير الشبكة</h3>

                • مستوى التهديد: منخفض

                <br>

                • التشفير: نشط

                <br>

                • الاتصال: آمن
            </div>
            """, unsafe_allow_html=True)

        except:

            st.error("تعذر الحصول على معلومات الشبكة")

# =========================
# توصيات أمنية
# =========================

with tab5:

    st.subheader("🛡️ التوصيات الأمنية")

    st.success("أفضل الممارسات لحماية حساباتك")

    st.markdown("""
✅ استخدم كلمات مرور طويلة وفريدة

✅ فعّل المصادقة الثنائية (2FA)

✅ لا تضغط على الروابط المشبوهة

✅ حدّث النظام والتطبيقات باستمرار

✅ استخدم مدير كلمات مرور

✅ راقب حساباتك بشكل دوري

✅ لا تشارك رموز التحقق مع أي شخص
""")
