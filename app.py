import streamlit as st
from gtts import gTTS
import tempfile
import os

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------
st.set_page_config(page_title="Crisis Assistance Tool", page_icon="🚨")

# ---------------------------------------------------
# LANGUAGE SELECTION (Arabic default)
# ---------------------------------------------------
language = st.selectbox("اختر اللغة / Choose Language", ["العربية", "English"])

# ---------------------------------------------------
# DISCLAIMER (TOP)
# ---------------------------------------------------
if language == "العربية":
    st.warning("⚠️ هذه الأداة تقدم إرشادات عامة فقط ولا تغني عن الجهات المختصة أو خدمات الطوارئ.")
else:
    st.warning("⚠️ This tool provides general guidance only and does not replace professional or emergency services.")

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
if language == "العربية":
    st.title("🚨 مساعد الطوارئ")
    st.write("أداة لمساعدتك في الوصول إلى الإرشادات والخدمات أثناء الأزمات")
else:
    st.title("🚨 Crisis Assistance Tool")
    st.write("Helping you access guidance and services during crises")

# ---------------------------------------------------
# SCENARIOS (NOW 5)
# ---------------------------------------------------
st.subheader("اختر حالتك / Select your situation")

col1, col2, col3, col4, col5 = st.columns(5)

if "scenario" not in st.session_state:
    st.session_state.scenario = ""

if col1.button("🏠 نزوح"):
    st.session_state.scenario = "displacement"

if col2.button("🍞 غذاء"):
    st.session_state.scenario = "food"

if col3.button("⚠️ حماية"):
    st.session_state.scenario = "safety"

if col4.button("🏥 صحة"):
    st.session_state.scenario = "health"

if col5.button("🧠 دعم نفسي"):
    st.session_state.scenario = "mhpss"

# ---------------------------------------------------
# USER INPUT
# ---------------------------------------------------
user_input = st.text_area(
    "اشرح حالتك / Describe your situation:",
    value=st.session_state.scenario
)

# ---------------------------------------------------
# MAIN BUTTON
# ---------------------------------------------------
if st.button("الحصول على المساعدة / Get Help"):

    if user_input:

        user_input_clean = user_input.lower()

        # ---------------------------------------------------
        # DETECTION
        # ---------------------------------------------------
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
        # RESPONSES (WITH EMOJIS FOR DISPLAY ONLY)
        # ---------------------------------------------------

        if scenario == "displacement":

            display_response = """
🔴 إجراءات فورية:
- التوجه إلى مكان آمن
- حمل الوثائق الأساسية

🟡 خطوات قصيرة المدى:
- التواصل مع المنظمات
- التسجيل للحصول على المساعدة

🟢 الدعم المتوفر:
- مأوى وخدمات أساسية
"""

            audio_response = """
إجراءات فورية:
التوجه إلى مكان آمن
حمل الوثائق الأساسية

خطوات قصيرة المدى:
التواصل مع المنظمات
التسجيل للحصول على المساعدة

الدعم المتوفر:
مأوى وخدمات أساسية
"""

            image_path = "images/displacement.jpg"

        elif scenario == "food":

            display_response = """
🔴 إجراءات فورية:
- البحث عن مراكز توزيع الغذاء
- التواصل مع الجهات المحلية

🟡 خطوات قصيرة المدى:
- التسجيل للحصول على مساعدات
- متابعة الإعلانات

🟢 الدعم المتوفر:
- غذاء ومواد أساسية ودعم نقدي
"""

            audio_response = """
إجراءات فورية:
البحث عن مراكز توزيع الغذاء
التواصل مع الجهات المحلية

خطوات قصيرة المدى:
التسجيل للحصول على مساعدات
متابعة الإعلانات

الدعم المتوفر:
غذاء ومواد أساسية ودعم نقدي
"""

            image_path = "images/food.jpg"

        elif scenario == "safety":

            display_response = """
🔴 إجراءات فورية:
- الابتعاد عن الخطر
- التوجه إلى مكان آمن

🟡 خطوات قصيرة المدى:
- طلب المساعدة
- تجنب المواجهة

🟢 الدعم المتوفر:
- خدمات حماية ودعم قانوني
"""

            audio_response = """
إجراءات فورية:
الابتعاد عن الخطر
التوجه إلى مكان آمن

خطوات قصيرة المدى:
طلب المساعدة
تجنب المواجهة

الدعم المتوفر:
خدمات حماية ودعم قانوني
"""

            image_path = "images/safety.jpg"

        elif scenario == "health":

            display_response = """
🔴 إجراءات فورية:
- التوجه إلى مركز صحي
- طلب استشارة طبية

🟡 خطوات قصيرة المدى:
- متابعة العلاج
- الالتزام بالأدوية

🟢 الدعم المتوفر:
- خدمات صحية
"""

            audio_response = """
إجراءات فورية:
التوجه إلى مركز صحي
طلب استشارة طبية

خطوات قصيرة المدى:
متابعة العلاج
الالتزام بالأدوية

الدعم المتوفر:
خدمات صحية
"""

            image_path = "images/health.jpg"

        else:

            display_response = """
🔴 إجراءات فورية:
- التحدث مع شخص موثوق
- أخذ وقت للراحة

🟡 خطوات قصيرة المدى:
- طلب دعم نفسي
- تقليل التوتر

🟢 الدعم المتوفر:
- دعم نفسي واجتماعي
"""

            audio_response = """
إجراءات فورية:
التحدث مع شخص موثوق
أخذ وقت للراحة

خطوات قصيرة المدى:
طلب دعم نفسي
تقليل التوتر

الدعم المتوفر:
دعم نفسي واجتماعي
"""

            image_path = "images/mhpss.jpg"

        # ---------------------------------------------------
        # DISPLAY TEXT
        # ---------------------------------------------------
        st.subheader("📋 الإرشادات")
        st.write(display_response)

        # ---------------------------------------------------
        # AUDIO (NO EMOJIS)
        # ---------------------------------------------------
        tts = gTTS(audio_response, lang="ar")
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)

        st.subheader("🔊 الصوت")
        st.audio(temp_file.name)

        # ---------------------------------------------------
        # IMAGE
        # ---------------------------------------------------
        st.subheader("🖼️ توضيح")

        if os.path.exists(image_path):
            st.image(image_path)
        else:
            st.warning("⚠️ الصورة غير موجودة")

        # ---------------------------------------------------
        # RESOURCES
        # ---------------------------------------------------
        st.subheader("📍 المصادر")

        if scenario == "displacement":
            st.markdown("🔗 خريطة الملاجئ:")
            st.markdown("https://experience.arcgis.com/experience/af252d852fd144ad98242eba8b6d60b3")

        elif scenario in ["food", "safety", "health"]:
            st.markdown("🔗 خدمات متعددة (غذاء / حماية / صحة):")
            st.markdown("https://app.powerbi.com/view?r=eyJrIjoiOThhYTMyN2ItMGNjMS00NDIzLWFhM2QtMjkzNmZkNjFiM2E5IiwidCI6ImU1YzM3OTgxLTY2NjQtNDEzNC04YTBjLTY1NDNkMmFmODBiZSIsImMiOjh9")

        else:
            st.markdown("🔗 خدمات الصحة النفسية:")
            st.markdown("https://resources.nmhp-lb.com/")

        # ---------------------------------------------------
        # CONTACTS
        # ---------------------------------------------------
        st.subheader("📞 أرقام الطوارئ")
        st.write("الصليب الأحمر: 140")
        st.write("الدفاع المدني: 125")