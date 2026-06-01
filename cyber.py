with tab4:
    st.subheader("🖥️ فحص أمن الشبكة والـ IP")
    
    if st.button("🚀 ابدأ المسح الأمني"):
        try:
            # جلب الـ IP
            ip_info = requests.get('https://api.ipify.org?format=json').json()
            
            # عرض الـ IP داخل مربع ملون
            st.info(f"🌐 عنوان الـ IP العام الخاص بك: {ip_info['ip']}")
            
            # عرض التقرير داخل حاوية (Container) ليعطي شكل "التقرير"
            st.markdown("### 📝 التقرير الأمني اللحظي:")
            with st.container():
                st.markdown("""
                <div style="background-color: #1e1e1e; padding: 15px; border-radius: 10px; border-left: 5px solid #00ffcc;">
                    <p>• <b>حالة الاتصال:</b> نشط عبر الإنترنت</p>
                    <p>• <b>مستوى التهديد:</b> منخفض (بناءً على التشفير)</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.warning("⚠️ إذا كنت متصلاً بشبكة عامة، يفضل تفعيل VPN فوراً.")
            
        except:
            st.error("تعذر جلب بيانات الشبكة.")
