import streamlit as st
import random

# MBTI별 직업 추천 데이터 (이모지 포함)
mbti_jobs = {
    "ISTJ": ["📊 회계사", "⚖️ 변호사", "🪖 군인", "🏛️ 행정 공무원"],
    "ISFJ": ["💉 간호사", "📚 교사", "🤝 사회복지사", "🗂️ 비서"],
    "INFJ": ["🧠 상담사", "✍️ 작가", "🔮 심리학자", "🌍 인권운동가"],
    "INTJ": ["📈 전략 컨설턴트", "🧪 데이터 과학자", "🔬 연구원", "⚙️ 엔지니어"],

    "ISTP": ["✈️ 파일럿", "🚒 소방관", "🔧 기계공", "⛑️ 응급 구조원"],
    "ISFP": ["🎨 아티스트", "👗 패션 디자이너", "🎼 작곡가", "👨‍🍳 요리사"],
    "INFP": ["📖 작가", "🧘 상담사", "👩‍🏫 교사", "💬 심리치료사"],
    "INTP": ["🔬 연구원", "💻 개발자", "📜 철학자", "🧬 과학자"],

    "ESTP": ["💼 기업가", "⚽ 스포츠 선수", "🗣️ 세일즈 전문가", "🚔 경찰관"],
    "ESFP": ["🎤 연예인", "🎉 이벤트 플래너", "📢 홍보 담당자", "🌏 여행 가이드"],
    "ENFP": ["💡 광고 기획자", "🚀 창업가", "🎭 배우", "🧑‍⚕️ 심리상담가"],
    "ENTP": ["⚖️ 변호사", "🎙️ 정치가", "📊 마케터", "🏢 벤처 창업가"],

    "ESTJ": ["🏦 경영자", "🪖 군 장교", "📋 프로젝트 매니저", "⚖️ 판사"],
    "ESFJ": ["💉 간호사", "📚 교사", "👥 HR 전문가", "🤲 사회복지사"],
    "ENFJ": ["👩‍🏫 교육자", "💬 심리상담가", "📢 홍보 전문가", "🌟 지도자"],
    "ENTJ": ["💼 CEO", "⚖️ 변호사", "💰 투자은행가", "📈 경영 컨설턴트"],
}

# MBTI별 랜덤 색상 팔레트 (시각적으로 화려하게)
colors = [
    "#FF6B6B", "#FFD93D", "#6BCB77", "#4D96FF", 
    "#BC6FF1", "#FF914D", "#2EC4B6", "#FF5D8F"
]

st.set_page_config(page_title="MBTI 진로 추천", page_icon="🎯", layout="centered")

st.title("🎯 MBTI 기반 진로 추천 웹앱")
st.write("당신의 MBTI를 선택하면, ✨화려한 직업 추천✨을 보여드려요!")

# MBTI 선택
selected_mbti = st.selectbox("👉 당신의 MBTI를 선택하세요:", list(mbti_jobs.keys()))

# 추천 직업 카드 스타일 표시
if selected_mbti:
    st.markdown(f"## 🌟 {selected_mbti} 유형에게 어울리는 직업 🌟")

    jobs = mbti_jobs[selected_mbti]
    color = random.choice(colors)

    for job in jobs:
        st.markdown(
            f"""
            <div style="
                background-color:{color};
                padding:15px;
                margin:10px 0;
                border-radius:15px;
                box-shadow: 3px 3px 10px rgba(0,0,0,0.2);
                font-size:20px;
                font-weight:bold;
                color:white;
                text-align:center;">
                {job}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.success(f"💡 {selected_mbti} 유형은 성향과 강점을 살려 위와 같은 직업에서 크게 성장할 수 있어요!")
    st.balloons()
