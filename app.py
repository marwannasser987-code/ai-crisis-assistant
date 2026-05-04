import streamlit as st
from gtts import gTTS
import tempfile
import os

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(page_title="Crisis Assistance Tool", page_icon="🚨")

# ---------------------------------------------------
# LANGUAGE SELECTOR (Arabic default)
# ---------------------------------------------------
language = st.selectbox("اختر اللغة / Choose Language", ["العربية", "English"])

# ---------------------------------------------------
# TEXT VARIABLES (FULL BILINGUAL SYSTEM)
# ---------------------------------------------------
if language == "العربية":
    title = "🚨 مساعد الطوارئ"
    description = "أداة لمساعدتك في الوصول إلى الإرشادات والخدمات أثناء الأزمات"
    scenario_label = "اختر حالتك"
    input_label = "اشرح حالتك"
    button_label = "الحصول على المساعدة"
    guidance_label = "📋 الإرشادات"
    audio_label = "🔊 الصوت"
    image_label = "🖼️ توضيح"
    resources_label = "📍 المصادر"
    contacts_label = "📞 أرقام الطوارئ"
    disclaimer_top = "⚠️ هذه الأداة تقدم إرشادات عامة فقط ولا تغني عن الجهات المختصة أو خدمات الطوارئ."
    disclaimer_bottom = "⚠️ هذه الأداة تقدم إرشادات عامة فقط ولا تغني عن الجهات المختصة."

else:
    title = "🚨 Crisis Assistance Tool"
    description = "Helping you access guidance and services during crises"
    scenario_label = "Select your situation"
    input_label = "Describe your situation"
    button_label = "Get Help"
    guidance_label = "📋 Guidance"
    audio_label = "🔊 Audio"
    image_label = "🖼️ Visual"
    resources_label = "📍 Resources"
    contacts_label = "📞 Emergency Contacts"
    disclaimer_top = "⚠️ This tool provides general guidance only and does not replace professional or emergency services."
    disclaimer_bottom = "⚠️ This tool provides general guidance only and does not replace professional services."

# ---------------------------------------------------
# DISCLAIMER
# ---------------------------------------------------
st.warning(disclaimer_top)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title(title)
st.write(description)

# ---------------------------------------------------
# SCENARIOS
# ---------------------------------------------------
st.subheader(scenario_label)

col1, col2, col3, col4, col5 = st.columns(5)

if "scenario" not in st.session_state:
    st.session_state.scenario = ""

if col1.button("🏠 نزوح" if language == "العربية" else "🏠 Displacement"):
    st.session_state.scenario = "displacement"

if col2.button("🍞 غذاء" if language == "العربية" else "🍞 Food"):
    st.session_state.scenario = "food"

if col3.button("⚠️ حماية" if language == "العربية" else "⚠️ Safety"):
    st.session_state.scenario = "safety"

if col4.button("🏥 صحة" if language == "العربية" else "🏥 Health"):
    st.session_state.scenario = "health"

if col5.button("🧠 دعم نفسي" if language == "العربية" else "🧠 Mental Health"):
    st.session_state.scenario = "mhpss"

# ---------------------------------------------------
# INPUT
# ---------------------------------------------------
user_input = st.text_area(input_label, value=st.session_state.scenario)

# ---------------------------------------------------
# MAIN BUTTON
# ---------------------------------------------------
if st.button(button_label):

    if user_input:

        user_input_clean = user_input.lower()

        # DETECTION
        if "food" in user_input_clean or "غذاء" in user_input_clean:
            scenario = "food"
        elif "unsafe" in user_input_clean or "خطر" in user_input_clean:
            scenario = "safety"
        elif "health" in user_input_clean or "صحة" in user_input_clean:
            scenario = "health"
        elif "mental" in user_input_clean or "نفسي" in user_input_clean:
            scenario = "mhpss"
        elif "leave" in user_input_clean or "نزوح" in user_input_clean:
            scenario = "displacement"
        else:
            scenario = st.session_state.scenario

        # ---------------------------------------------------
        # RESPONSES
        # ---------------------------------------------------
        if scenario == "displacement":

            if language == "العربية":
                display_response = """🔴 إجراءات فورية:
- التوجه إلى مكان آمن
- حمل الوثائق الأساسية

🟡 خطوات قصيرة المدى:
- التواصل مع المنظمات
- التسجيل للحصول على المساعدة

🟢 الدعم المتوفر:
- مأوى وخدمات أساسية
"""
                audio_response = """إجراءات فورية:
التوجه إلى مكان آمن
حمل الوثائق الأساسية

خطوات قصيرة المدى:
التواصل مع المنظمات
التسجيل للحصول على المساعدة

الدعم المتوفر:
مأوى وخدمات أساسية
"""
            else:
                display_response = """Immediate Actions:
- Move to a safe place
- Carry important documents

Short-term Steps:
- Contact organizations
- Register for assistance

Available Support:
- Shelter and basic services
"""
                audio_response = display_response

            image_path = "images/displacement.jpg"

        elif scenario == "food":

            if language == "العربية":
                display_response = """🔴 إجراءات فورية:
- البحث عن مراكز توزيع الغذاء
- التواصل مع الجهات المحلية

🟡 خطوات قصيرة المدى:
- التسجيل للحصول على مساعدات
- متابعة الإعلانات

🟢 الدعم المتوفر:
- غذاء ومواد أساسية
"""
                audio_response = display_response
            else:
                display_response = """Immediate Actions:
- Find food distribution points
- Contact local organizations

Short-term Steps:
- Register for assistance
- Follow updates

Available Support:
- Food and basic items
"""
                audio_response = display_response

            image_path = "images/food.jpg"

        elif scenario == "safety":

            if language == "العربية":
                display_response = """🔴 إجراءات فورية:
- الابتعاد عن الخطر
- التوجه إلى مكان آمن

🟡 خطوات قصيرة المدى:
- طلب المساعدة
- تجنب المواجهة

🟢 الدعم المتوفر:
- خدمات حماية
"""
                audio_response = display_response
            else:
                display_response = """Immediate Actions:
- Move away from danger
- Find a safe place

Short-term Steps:
- Seek help
- Avoid confrontation

Available Support:
- Protection services
"""
                audio_response = display_response

            image_path = "images/safety.jpg"

        elif scenario == "health":

            if language == "العربية":
                display_response = """🔴 إجراءات فورية:
- التوجه إلى مركز صحي
- طلب استشارة طبية

🟡 خطوات قصيرة المدى:
- متابعة العلاج
- الالتزام بالأدوية

🟢 الدعم المتوفر:
- خدمات صحية
"""
                audio_response = display_response
            else:
                display_response = """Immediate Actions:
- Visit a health center
- Seek medical advice

Short-term Steps:
- Follow treatment
- Take medication

Available Support:
- Health services
"""
                audio_response = display_response

            image_path = "images/health.jpg"

        else:

            if language == "العربية":
                display_response = """🔴 إجراءات فورية:
- التحدث مع شخص موثوق
- أخذ وقت للراحة

🟡 خطوات قصيرة المدى:
- طلب دعم نفسي
- تقليل التوتر

🟢 الدعم المتوفر:
- دعم نفسي واجتماعي
"""
                audio_response = display_response
            else:
                display_response = """Immediate Actions:
- Talk to someone you trust
- Take time to rest

Short-term Steps:
- Seek support
- Reduce stress

Available Support:
- Mental health support
"""
                audio_response = display_response

            image_path = "images/mhpss.jpg"

        # ---------------------------------------------------
        # OUTPUT
        # ---------------------------------------------------
        st.subheader(guidance_label)
        st.write(display_response)

        # AUDIO
        lang_code = "ar" if language == "العربية" else "en"
        tts = gTTS(audio_response, lang=lang_code)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)

        st.subheader(audio_label)
        st.audio(temp_file.name)

        # IMAGE (SAFE LOAD)
        st.subheader(image_label)
        if os.path.exists(image_path):
            try:
                st.image(image_path)
            except:
                st.warning("⚠️ Image error")
        else:
            st.warning("⚠️ Image not found")

        # RESOURCES
        st.subheader(resources_label)

        if scenario == "displacement":
            st.markdown("🔗 خريطة الملاجئ" if language == "العربية" else "🔗 Shelter Map")
            st.markdown("https://experience.arcgis.com/experience/af252d852fd144ad98242eba8b6d60b3")

        elif scenario in ["food", "safety", "health"]:
            st.markdown("🔗 خدمات متعددة" if language == "العربية" else "🔗 Services")
            st.markdown("https://app.powerbi.com/view?r=eyJrIjoiOThhYTMyN2ItMGNjMS00NDIzLWFhM2QtMjkzNmZkNjFiM2E5IiwidCI6ImU1YzM3OTgxLTY2NjQtNDEzNC04YTBjLTY1NDNkMmFmODBiZSIsImMiOjh9")

        else:
            st.markdown("🔗 الصحة النفسية" if language == "العربية" else "🔗 Mental Health Resources")
            st.markdown("https://resources.nmhp-lb.com/")

        # CONTACTS
        st.subheader(contacts_label)

        if language == "العربية":
            st.write("الصليب الأحمر: 140")
            st.write("الدفاع المدني: 125")
        else:
            st.write("Red Cross: 140")
            st.write("Civil Defense: 125")

        # FINAL DISCLAIMER
        st.warning(disclaimer_bottom)
