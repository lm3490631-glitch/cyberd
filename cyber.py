with tab2:
    st.subheader("🌐 تحليل الروابط (فحص حقيقي)")
    link = st.text_input("ضع الرابط هنا:")
    if st.button("اضغط هنا للتحليل"):
        if link:
            with st.spinner("جاري فحص الرابط عبر سيرفرات VirusTotal..."):
                try:
                    # استبدل YOUR_API_KEY بمفتاحك من VirusTotal
                    vt_key = "YOUR_API_KEY_HERE"
                    url = "https://www.virustotal.com/api/v3/urls"
                    headers = {"x-apikey": vt_key}
                    payload = {"url": link}
                    
                    response = requests.post(url, headers=headers, data=payload)
                    result_id = response.json().get("data", {}).get("id")
                    
                    # جلب التقرير بناءً على ID الفحص
                    report_url = f"https://www.virustotal.com/api/v3/analyses/{result_id}"
                    report = requests.get(report_url, headers=headers).json()
                    
                    stats = report.get("data", {}).get("attributes", {}).get("stats", {})
                    st.success("✅ تم الفحص بنجاح:")
                    st.write(f"📊 التهديدات المكتشفة: {stats.get('malicious', 0)}")
                    st.write(f"🛡️ المواقع التي صنفته كآمن: {stats.get('harmless', 0)}")
                    
                except Exception as e:
                    st.error("حدث خطأ في الاتصال، تأكد من مفتاح الـ API.")
