import streamlit as st
import random

# MBTI별 여행지 추천 데이터 (이모지 폭탄 버전)
mbti_travel = {
    "ISTJ": ["🇨🇭🏔️ 스위스 알프스", "🇯🇵⛩️ 교토 사찰 여행", "🇩🇪🏰 독일 고성 투어", "🇬🇧📜 런던 역사 여행"],
    "ISFJ": ["🇫🇷🌹 파리 카페 거리", "🇰🇷🌸 경주 벚꽃", "🇮🇹🎨 피렌체 미술관", "🇨🇦🍁 캐나다 단풍 여행"],
    "INFJ": ["🇳🇴❄️ 노르웨이 오로라", "🇮🇳🕉️ 인도 리트릿", "🇳🇿🌿 뉴질랜드 자연 탐험", "🇵🇪⛰️ 마추픽추"],
    "INTJ": ["🇺🇸🏙️ 뉴욕 금융가", "🇸🇬🌆 싱가포르", "🇯🇵🔬 도쿄 테크 투어", "🇨🇳🏮 상하이"],

    "ISTP": ["🇦🇺🏄 호주 서핑", "🇿🇦🦁 남아공 사파리", "🇨🇱⛰️ 파타고니아", "🇵🇭🤿 세부 다이빙"],
    "ISFP": ["🇬🇷🏖️ 산토리니", "🇮🇩🌴 발리", "🇪🇸🎶 바르셀로나", "🇯🇲🌞 자메이카"],
    "INFP": ["🇮🇸🔥 아이슬란드 오로라", "🇹🇭🌺 치앙마이 명상 여행", "🇲🇽🎭 멕시코 문화", "🇲🇦🏜️ 모로코 사막"],
    "INTP": ["🇨🇭🔭 CERN 방문", "🇺🇸🛰️ NASA 투어", "🇩🇰🚲 코펜하겐", "🇯🇵📚 아키하바라"],

    "ESTP": ["🇧🇷🎉 리우 카니발", "🇺🇸🎢 라스베가스", "🇲🇨🏎️ 모나코 F1", "🇰🇷🎮 서울 홍대"],
    "ESFP": ["🇮🇹🍝 로마", "🇯🇵🎆 오사카 불꽃놀이", "🇺🇸🎶 LA 헐리우드", "🇦🇺🍷 시드니"],
    "ENFP": ["🇮🇳🕉️ 리시케시", "🇵🇹🌊 포르투", "🇹🇷🕌 이스탄불", "🇨🇴🎶 카르타헤나"],
    "ENTP": ["🇭🇰🏙️ 홍콩", "🇦🇪🌆 두바이", "🇺🇸🗽 뉴욕", "🇩🇪🍺 뮌헨 옥토버페스트"],

    "ESTJ": ["🇯🇵🏯 도쿄", "🇺🇸🏛️ 워싱턴 DC", "🇫🇷🏰 베르사유", "🇰🇷📈 서울 비즈니스 여행"],
    "ESFJ": ["🇹🇭🏝️ 푸켓", "🇲🇾🌴 코타키나발루", "🇪🇸🌞 마드리드", "🇰🇷🎇 부산 불꽃축제"],
    "ENFJ": ["🇨🇳🏮 베이징 자금성", "🇮🇹🎭 베네치아 카니발", "🇬🇧🎓 옥스퍼드", "🇺🇸🎤 브로드웨이"],
    "ENTJ": ["🇺🇸💼 뉴욕 월스트리트", "🇨🇭🏦 취리히", "🇯🇵🚅 신칸센 투어", "🇩🇪⚙️ 베를린"],
}

# 색상 팔레트
colors = [
    "#FF6B6B", "#FFD93D", "#6BCB77", "#4D96FF", 
    "#BC6FF1", "#FF914D", "#2EC4B6", "#FF5D8F", "#845EC2", "#FF9671"
]

st.set_page_config(page_title="MBTI 여행지 추천", page_icon="🌍", layout="centered")

st.title("🌍✨ MBTI 기반 여행지 추천 ✨🌍")
st.write("👉 당신의 MBTI를 선택하면, 🌈이모지 폭발🌈 여행지를 추천해드려요!")

# MBTI 선택
selected_mbti = st.selectbox("✈️ 당신의 MBTI를 선택하세요:", list(mbti_travel.keys()))

# 추천 여행지 카드 출력
if selected_mbti:
    st.markdown(f"## 🗺️ {selected_mbti} 유형에게 어울리는 여행지 🗺️")

    places = mbti_travel[selected_mbti]

    for place in places:
        color = random.choice(colors)
        st.markdown(
            f"""
            <div style="
                background:linear-gradient(135deg, {color}, #ffffff30);
                padding:20px;
                margin:12px 0;
                border-radius:20px;
                box-shadow: 4px 4px 15px rgba(0,0,0,0.3);
                font-size:22px;
                font-weight:bold;
                color:white;
                text-align:center;
                text-shadow:1px 1px 3px black;">
                {place}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.success(f"🌴✨ {selected_mbti} 유형은 위와 같은 여행지에서 에너지를 충전하고 새로운 영감을 얻을 수 있어요! ✨🌴")
    st.balloons()
