import streamlit as st

st.set_page_config(
    page_title="Cyber Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

/* إخفاء Sidebar */
[data-testid="stSidebar"]{
    display:none;
}

/* استغلال كامل عرض الشاشة */
.main .block-container{
    max-width:100% !important;
    padding-top:1rem !important;
    padding-left:2rem !important;
    padding-right:2rem !important;
}

/* إزالة المسافات الفارغة */
section.main > div{
    padding-top:0rem;
}

/* إخفاء عناصر Streamlit */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

:root{
    --bg:#0B1020;
    --card:#151B2D;
    --primary:#00D4AA;
}

.stApp{
    background:var(--bg);
}

.hero{
    text-align:center;
    padding:20px;
    margin-bottom:20px;
}

.hero-title{
    font-size:3.5rem;
    font-weight:700;
    color:white;
}

.hero-sub{
    font-size:1.2rem;
    color:#c7c7c7;
}

/* بطاقات الإحصائيات */
.metric-card{
    background:#151B2D;
    border-radius:18px;
    padding:25px;
    text-align:center;
    border:1px solid rgba(255,255,255,.08);
    box-shadow:0 4px 20px rgba(0,0,0,.25);
}

.metric-number{
    font-size:2rem;
    font-weight:bold;
    color:#00D4AA;
}

.metric-text{
    color:white;
}

/* التبويبات */
.stTabs [data-baseweb="tab-list"]{
    gap:20px;
}

.stTabs [data-baseweb="tab"]{
    font-size:18px;
}

/* الإدخال */
div[data-baseweb="input"]{
    border:1px solid #00D4AA !important;
    border-radius:12px !important;
}

/* الأزرار */
.stButton>button{
    width:100%;
    height:55px;
    border-radius:12px;
    background:#00D4AA !important;
    color:black !important;
    font-weight:bold;
    border:none;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# الهيدر
# ==========================

st.markdown("""
<div class="hero">
    <div class="hero-title">
        🛡️ نظام الاستخبارات السيبراني
    </div>

    <div class="hero-sub">
        اكتشف التسريبات الأمنية وحلل الروابط ومؤشرات التهديد
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================
# Dashboard كامل العرض
# ==========================

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">12K+</div>
        <div class="metric-text">عمليات الفحص</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">450</div>
        <div class="metric-text">التسريبات المكتشفة</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">99.8%</div>
        <div class="metric-text">توافر الخدمة</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">24/7</div>
        <div class="metric-text">المراقبة المستمرة</div>
    </div>
    """, unsafe_allow_html=True)
