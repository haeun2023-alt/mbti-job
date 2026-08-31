import streamlit as st


st.set_page_config(page_title="우리나라 MBTI 비율", page_icon="🇰🇷", layout="wide")

KOREA_DATA = [
    {"MBTI": "INFP", "비율(%)": 13.4},
    {"MBTI": "ENFP", "비율(%)": 12.6},
    {"MBTI": "ISFJ", "비율(%)": 8.5},
    {"MBTI": "ISFP", "비율(%)": 8.2},
    {"MBTI": "ESFJ", "비율(%)": 8.0},
    {"MBTI": "INFJ", "비율(%)": 7.8},
    {"MBTI": "ESFP", "비율(%)": 6.9},
    {"MBTI": "ENFJ", "비율(%)": 6.5},
    {"MBTI": "ISTJ", "비율(%)": 5.7},
    {"MBTI": "INTP", "비율(%)": 4.8},
    {"MBTI": "ENTP", "비율(%)": 4.5},
    {"MBTI": "ISTP", "비율(%)": 4.1},
    {"MBTI": "INTJ", "비율(%)": 3.8},
    {"MBTI": "ESTJ", "비율(%)": 2.6},
    {"MBTI": "ENTJ", "비율(%)": 2.0},
    {"MBTI": "ESTP", "비율(%)": 0.6},
]

st.title("🇰🇷 우리나라 MBTI 비율")
st.write("우리나라 온라인 성격유형 검사에서 나타난 유형별 분포를 살펴보세요. 📊")

st.warning(
    "이 그래프는 온라인 자기보고식 검사 자료를 바탕으로 재구성한 교육용 예시입니다. "
    "대한민국 전체 인구의 공식 통계가 아니며, 조사 시기·대상·검사 도구에 따라 결과가 달라질 수 있습니다."
)

st.bar_chart(KOREA_DATA, x="MBTI", y="비율(%)", color="#7C3AED", height=500)

top_three = KOREA_DATA[:3]
cols = st.columns(3)
medals = ["🥇", "🥈", "🥉"]
for col, medal, item in zip(cols, medals, top_three):
    with col:
        st.metric(f"{medal} {item['MBTI']}", f"{item['비율(%)']}%")

st.subheader("🔍 그래프 읽기")
st.markdown(
    """
- 막대가 높을수록 해당 조사에서 그 유형을 선택한 응답자의 비율이 높다는 뜻이에요.
- 비율이 높다고 더 좋은 유형인 것은 아니며, 낮다고 특별하거나 부족한 유형인 것도 아니에요.
- 온라인 검사 참여자는 연령과 관심사가 전체 국민과 다를 수 있으므로 해석할 때 주의해야 해요.
"""
)

with st.expander("📝 수업에서 생각해 볼 질문"):
    st.write("1. 온라인 설문 결과를 우리나라 전체 국민의 특성이라고 말할 수 있을까요?")
    st.write("2. 조사 대상자의 연령에 따라 MBTI 비율은 어떻게 달라질까요?")
    st.write("3. 막대그래프 외에 이 자료를 표현할 수 있는 방법은 무엇일까요?")

st.caption("자료 참고: 16Personalities 국가 프로필의 온라인 자기보고식 조사 방식 · 수업용 재구성")
