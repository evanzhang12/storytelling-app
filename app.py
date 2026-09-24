"""
儿童故事讲述应用 - Streamlit版本 - 测试版
ISOM5240 作业提交
"""

import streamlit as st
from PIL import Image
import pyttsx3
import os
import tempfile

st.set_page_config(
    page_title="小故事魔法师",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #FFF8F0 0%, #FFE5D9 100%);
        padding: 20px;
    }
    h1 {
        color: #FF6B6B;
        text-align: center;
        font-size: 2.5em;
    }
    .story-box {
        background: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FF6B6B;
        margin: 20px 0;
        font-size: 1.2em;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📖 小故事魔法师 ✨")

# 核心函数
def generate_caption_test(image):
    return "A magical scene with children playing"

def generate_story_test(caption):
    return f"""Once upon a time, there was a magical place. {caption}. A little girl named Emma discovered something amazing. She found a secret garden full of colorful flowers. Every night, the flowers would sing a beautiful song. Emma realized that magic was real."""

def text_to_speech(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.9)
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            audio_file = f.name
        
        engine.save_to_file(text, audio_file)
        engine.runAndWait()
        
        with open(audio_file, 'rb') as f:
            audio_data = f.read()
        
        if os.path.exists(audio_file):
            os.remove(audio_file)
        
        return audio_data
    except Exception as e:
        st.error(f"❌ 语音转换失败: {str(e)}")
        return None

# 主应用
uploaded_file = st.file_uploader(
    "📸 选择一张图片（JPG 或 PNG）",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(image, caption="你上传的图片", use_container_width=True)
    
    if st.button("🎬 开始讲故事", use_container_width=True):
        st.info("⏳ 第1步：识别图片...")
        caption = generate_caption_test(image)
        st.success(f"✅ 图片描述：{caption}")
        
        st.info("⏳ 第2步：生成故事...")
        story = generate_story_test(caption)
        st.success("✅ 故事已生成！")
        
        st.markdown(f"### 📖 你的故事：\n\n{story}")
        
        st.info("⏳ 第3步：转换为语音...")
        audio_data = text_to_speech(story)
        
        if audio_data:
            st.success("✅ 语音已生成！")
            st.audio(audio_data, format="audio/mp3")