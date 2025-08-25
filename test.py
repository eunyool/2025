import streamlit as st

st.set_page_config(page_title="날씨와 호르몬", page_icon="🌤️")
st.title("☁️ 날씨와 기분, 그리고 호르몬 🍀")
st.write("날씨를 선택하면 그에 따른 기분과 관련 호르몬을 귀엽고 직관적으로 확인할 수 있어요!")

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
        "배경": "https://images.unsplash.com/photo-1501973801540-537f08ccae7b"  # 맑은 하늘
    },
    "맑음 - 무더움 🔥": {
        "기분": "피로, 짜증 증가",
        "호르몬": ["코르티솔 (Cortisol)", "세로토닌 변동"],
        "이미지": "https://cdn-icons-png.flaticon.com/512/869/869869.png",
        "배경": "https://images.unsplash.com/photo-1561489427-bd9fafd4d74a"  # 뜨거운 햇살
    },
    "흐림 - 쌀쌀 ☁️": {
        "기분": "차분, 다소 우울",
        "호르몬": ["멜라토닌 (Melatonin)", "세로토닌 감소"],
        "이미지": "https://cdn-icons-png.flaticon.com/512/2938/2938105.png",
        "배경": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d"  # 흐린 날씨
    },
    "흐림 - 습함 🌫️": {
        "기분": "무기력, 답답함",
        "호르몬": ["코르티솔 (Cortisol)", "세로토닌 감소"],
        "이미지": "https://cdn-icons-png.flaticon.com/512/414/414974.png",  # 눈 결정 아이콘
        "배경": "https://images.unsplash.com/photo-1601924928281-4b66f8da7f8d"  # 습한 날씨 느낌
    },
    "비 - 소나기 🌦️": {
        "기분": "차분, 안정",
        "호르몬": ["옥시토신 (Oxytocin)", "세로토닌"],
        "이미지": "https://cdn-icons-png.flaticon.com/512/1163/1163657.png",
        "배경": "https://images.unsplash.com/photo-1503437313881-503a91226419"  # 비 내리는 모습
    },
    "비 - 폭우 🌧️": {
        "기분": "피로, 우울감 가능",
        "호르몬": ["코르티솔 (Cortisol)", "멜라토닌 (Melatonin)"],
        "이미지": "https://cdn-icons-png.flaticon.com/512/1146/1146860.png",
        "배경": "https://images.unsplash.com/photo-1469474968028-56623f02e42e"  # 폭우 느낌
    },
    "눈 - 폭설 🌨️": {
        "기분": "고립감, 스트레스 가능",
        "호르몬": ["코르티솔 (Cortisol)", "세로토닌 변동"],
        "이미지": "https://cdn-icons-png.flaticon.com/512/642/642102.png",  # 눈이 펑펑 내리는 아이콘
        "배경": "https://images.unsplash.com/photo-1608889179915-25d2d4b0c31a"  # 눈 오는 풍경
    }
}

selected = weather_data[weather]

# 배경 스타일 설정
background_url = selected["배경"]
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("{background_url}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 콘텐츠 출력
st.image(selected["이미지"], width=150)
st.subheader("기분")
st.write(f"**{selected['기분']}**")

st.subheader("관련 호르몬")
for h in selected["호르몬"]:
    st.write(f"- {h}")
