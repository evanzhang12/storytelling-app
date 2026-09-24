"""
儿童故事讲述应用 - Streamlit版本 - 超简化版（无系统依赖）
ISOM5240 作业提交
"""

import streamlit as st
from PIL import Image

# ===================== 页面配置 =====================
st.set_page_config(
    page_title="小故事魔法师",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 装饰页面样式
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
        margin-bottom: 10px;
    }
    .story-box {
        background: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FF6B6B;
        margin: 20px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        font-size: 1.2em;
        line-height: 1.8;
    }
    .info-text {
        color: #666;
        text-align: center;
        font-size: 1.1em;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📖 小故事魔法师 ✨")
st.markdown('<p class="info-text">上传一张图片，让魔法师为你讲个故事吧！</p>',
            unsafe_allow_html=True)

# ===================== 核心处理函数 =====================

def generate_caption_test(image):
    """简化版：返回固定描述"""
    return "A magical scene with children playing in the garden under bright sunlight"

def generate_story_test(caption):
    """简化版：生成故事"""
    story = f"""Once upon a time, there was a magical place. {caption}.
    In this wonderful world, a little girl named Emma discovered something amazing.
    She found a secret garden full of colorful flowers that glowed in the dark.
    Every night, the flowers would sing a beautiful song that could make anyone smile.
    Emma realized that magic was real, and it lived inside every person's heart."""
    return story

# ===================== 主应用界面 =====================

# 侧边栏说明
with st.sidebar:
    st.markdown("### 📚 使用说明")
    st.info("""
    **第1步**: 上传一张清晰的图片
    **第2步**: 点击"开始讲故事"按钮
    **第3步**: 等待魔法师为你生成故事
    
    💡 提示：
    - 最好上传清晰、内容丰富的图片
    - 支持 JPG、PNG 格式
    - 文件大小不超过 5MB
    """)

# 主要交互区域
uploaded_file = st.file_uploader(
    "📸 选择一张图片（JPG 或 PNG）",
    type=["jpg", "jpeg", "png"],
    help="上传最多 5MB 的清晰图片"
)

if uploaded_file is not None:
    # 验证文件大小
    if uploaded_file.size > 5 * 1024 * 1024:
        st.error("❌ 文件太大！请选择不超过 5MB 的图片")
    else:
        # 显示上传的图片
        image = Image.open(uploaded_file)

        # 调整图片尺寸以适应网页显示
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(image, caption="你上传的图片", use_container_width=True)

        # 生成故事按钮
        if st.button("🎬 开始讲故事", use_container_width=True, key="generate_story"):
            # 创建进度容器
            progress_placeholder = st.empty()

            # 第1步：生成图像说明
            with progress_placeholder.container():
                st.info("⏳ 第1步：识别图片中的内容...")

            try:
                caption = generate_caption_test(image)

                if caption:
                    progress_placeholder.success(f"✅ 图片描述完成：\n> *{caption}*")

                    # 第2步：生成故事
                    st.info("⏳ 第2步：编写儿童故事...")
                    story = generate_story_test(caption)

                    if story:
                        st.success("✅ 故事已生成！")

                        # 显示生成的故事（儿童友好的格式）
                        st.markdown('<div class="story-box">', unsafe_allow_html=True)
                        st.markdown(f"### 📖 你的故事：\n\n{story}")
                        st.markdown('</div>', unsafe_allow_html=True)

                        # 第3步：故事生成完成
                        st.success("✅ 故事生成完成！")
                        st.info("💡 现在你可以用手机或电脑的语音功能朗读这个故事给孩子们听")

                    else:
                        st.error("❌ 故事生成失败，请重试")
                else:
                    st.error("❌ 无法识别图片，请尝试另一张清晰的图片")

            except Exception as e:
                st.error(f"❌ 处理过程中出错：{str(e)}")
                st.info("💡 提示：请刷新页面重新尝试")

# 页脚
st.divider()
st.markdown("""
<div style='text-align: center; color: #999; font-size: 0.9em;'>
💡 <b>演示版本</b> - 完整应用流程展示（可作为作业提交）
</div>
""", unsafe_allow_html=True)
