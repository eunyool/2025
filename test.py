import streamlit as st

st.set_page_config(page_title="날씨와 호르몬", page_icon="🌤️")
st.title("☁️ 날씨와 기분, 그리고 호르몬 🍀")
st.write("날씨를 선택하면 그에 따른 기분과 관련 호르몬을 귀엽게 확인할 수 있어요!")

weather = st.selectbox(
    "오늘의 날씨를 선택하세요:",
    [
        "맑음 - 쾌청 ☀️", 
        "맑음 - 무더움 🔥",
        "흐림 - 쌀쌀 ☁️", 
        "흐림 - 습함 🌫️",
        "비 - 소나기 🌦️", 
        "비 - 폭우 🌧️",
        "눈 - 폭설 🌨️"
    ]
)

weather_data = {
    "맑음 - 쾌청 ☀️": {
        "기분": "상쾌, 에너제틱",
        "호르몬": ["세로토닌 (Serotonin)", "도파민 (Dopamine)"],
        # 태양/햇살 아이콘
        "이미지": "https://cdn-icons-png.flaticon.com/512/869/869869.png"
    },
    "맑음 - 무더움 🔥": {
        "기분": "피로, 짜증 증가",
        "호르몬": ["코르티솔 (Cortisol)", "세로토닌 변동"],
        # 화창한 하늘 이미지
        "이미지": "https://cdn-icons-png.flaticon.com/512/3222/3222800.png"
    },
    "흐림 - 쌀쌀 ☁️": {
        "기분": "차분, 다소 우울",
        "호르몬": ["멜라토닌 (Melatonin)", "세로토닌 감소"],
        # 기존 무더움 아이콘(불)로 교체
        "이미지": "https://cdn-icons-png.flaticon.com/512/2938/2938105.png"
    },
    "흐림 - 습함 🌫️": {
        "기분": "무기력, 답답함",
        "호르몬": ["코르티솔 (Cortisol)", "세로토닌 감소"],
        "이미지": "https://cdn-icons-png.flaticon.com/512/728/728093.png"
    },
    "비 - 소나기 🌦️": {
        "기분": "차분, 안정",
        "호르몬": ["옥시토신 (Oxytocin)", "세로토닌"],
        "이미지": "https://cdn-icons-png.flaticon.com/512/1163/1163657.png"
    },
    "비 - 폭우 🌧️": {
        "기분": "피로, 우울감 가능",
        "호르몬": ["코르티솔 (Cortisol)", "멜라토닌 (Melatonin)"],
        # 단순 비 아이콘으로 변경
        "이미지": "https://cdn-icons-png.flaticon.com/512/1146/1146860.png"
    },
    "눈 - 폭설 🌨️": {
        "기분": "고립감, 스트레스 가능",
        "호르몬": ["코르티솔 (Cortisol)", "세로토닌 변동"],
        "이미지": "https://cdn-icons-png.flaticon.com/512/642/642102.png"
    }
}

selected = weather_data[weather]

st.image(selected["이미지"], width=150)

st.subheader("기분")
st.write(f"**{selected['기분']}**")

st.subheader("관련 호르몬")
for h in selected["호르몬"]:
    st.write(f"- {h}")
