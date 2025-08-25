import streamlit as st

st.set_page_config(page_title="날씨와 호르몬", page_icon="🌤️")
st.markdown(
    """
    <style>
    /* 앱 전체 폰트와 여백 */
    .stApp {
        font-family: 'Pretendard', sans-serif;
    }
    /* 메인 컨텐츠 영역에 배경 오버레이 적용 */
    .content {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 20px;
        max-width: 600px;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("☁️ 날씨와 기분, 그리고 호르몬 🍀")
st.write("날씨를 선택하면 그에 따른 기분과 관련 호르몬을 귀엽게 확인할 수 있어요!")

weather = st.selectbox(
    "오늘의 날씨를 선택하세요:",
    [
        "맑음 ☀️",
        "맑음 - 무더움 🔥",
        "흐림 - 쌀쌀 ☁️",
        "흐림 - 습함 🌫️",
        "비 - 소나기 🌦️",
        "비 - 폭우 🌧️",
        "눈 - 폭설 🌨️"
    ]
)

weather_data = {
    "맑음 ☀️": {
        "기분": "상쾌, 에너제틱",
        "호르몬": ["세로토닌 (Serotonin)", "도파민 (Dopamine)"],
        "이미지": "https://cdn-icons-png.flaticon.com/512/3222/3222800.png",
        "배경": "https://cdn.pixabay.com/photo/2017/04/06/16/32/sunny-2203664_960_720.png"
    },
    "맑음 - 무더움 🔥": {
        "기분": "피로, 짜증 증가",
        "호르몬": ["코르티솔 (Cortisol)", "세로토닌 변동"],
        "이미지": "https://cdn-icons-png.flaticon.com/512/869/869869.png",
        "배경": "https://cdn.pixabay.com/photo/2016/03/31/20/51/sun-1295053_960_720.png"
    },
    "흐림 - 쌀쌀 ☁️": {
        "기분": "차분, 다소 우울",
        "호르몬": ["멜라토닌 (Melatonin)", "세로토닌 감소"],
        "이미지": "https://cdn-icons-png.flaticon.com/512/2938/2938105.png",
        "배경": "https://cdn.pixabay.com/photo/2014/04/03/10/28/cloud-311595_960_720.png"
    },
    "흐림 - 습함 🌫️": {
        "기분": "무기력, 답답함",
        "호르몬": ["코르티솔 (Cortisol)", "세로토닌 감소"],
        "이미지": "https://cdn-icons-png.flaticon.com/512/414/414974.png",
        "배경": "https://cdn.pixabay.com/photo/2014/04/03/10/21/drop-311547_960_720.png"
    },
    "비 - 소나기 🌦️": {
        "기분": "차분, 안정",
        "호르몬": ["옥시토신 (Oxytocin)", "세로토닌"],
        "이미지": "https://cdn-icons-png.flaticon.com/512/1163/1163657.png",
        "배경": "https://cdn.pixabay.com/photo/2016/09/22/09/30/rain-1686331_960_720.png"
    },
    "비 - 폭우 🌧️": {
        "기분": "피로, 우울감 가능",
        "호르몬": ["코르티솔 (Cortisol)", "멜라토닌 (Melatonin)"],
        "이미지": "https://cdn-icons-png.flaticon.com/512/1146/1146860.png",
        "배경": "https://cdn.pixabay.com/photo/2016/09/22/09/30/rain-1686332_960_720.png"
    },
    "눈 - 폭설 🌨️": {
        "기분": "고립감, 스트레스 가능",
        "호르몬": ["코르티솔 (Cortisol)", "세로토닌 변동"],
        "이미지": "https://cdn-icons-png.flaticon.com/512/642/642102.png",
        "배경": "https://cdn.pixabay.com/photo/2014/04/02/10/20/snow-304260_960_720.png"
    }
}

selected = weather_data[weather]

# 배경 스타일 적용
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("{selected['배경']}") no-repeat center center fixed;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 내용은 반투명 박스 안에 넣기
st.markdown('<div class="content">', unsafe_allow_html=True)

st.image(selected["이미지"], width=150)
st.subheader("기분")
st.write(f"**{selected['기분']}**")

st.subheader("관련 호르몬")
for h in selected["호르몬"]:
    st.write(f"- {h}")

st.markdown('</div>', unsafe_allow_html=True)
