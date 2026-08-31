import streamlit as st


st.set_page_config(page_title="나라별 MBTI 분포", page_icon="🌏", layout="wide")

COUNTRY_DATA = {
    "대한민국 🇰🇷": {"분석가형(NT)": 15, "외교관형(NF)": 40, "관리자형(SJ)": 25, "탐험가형(SP)": 20},
    "미국 🇺🇸": {"분석가형(NT)": 12, "외교관형(NF)": 25, "관리자형(SJ)": 43, "탐험가형(SP)": 20},
    "일본 🇯🇵": {"분석가형(NT)": 14, "외교관형(NF)": 31, "관리자형(SJ)": 37, "탐험가형(SP)": 18},
    "독일 🇩🇪": {"분석가형(NT)": 22, "외교관형(NF)": 24, "관리자형(SJ)": 38, "탐험가형(SP)": 16},
    "브라질 🇧🇷": {"분석가형(NT)": 10, "외교관형(NF)": 33, "관리자형(SJ)": 31, "탐험가형(SP)": 26},
}

GROUP_HELP = {
    "분석가형(NT)": "INTJ · INTP · ENTJ · ENTP",
    "외교관형(NF)": "INFJ · INFP · ENFJ · ENFP",
    "관리자형(SJ)": "ISTJ · ISFJ · ESTJ · ESFJ",
    "탐험가형(SP)": "ISTP · ISFP · ESTP · ESFP",
}

st.title("🌏 나라별 MBTI 분포 비교")
st.write("나라를 선택하고 네 가지 성격유형 그룹의 분포를 비교해 보세요.")

st.warning(
    "아래 수치는 국가별 차이를 탐색하기 위한 교육용 예시 데이터입니다. "
    "온라인 검사는 자발적 참여 자료이므로 국가 전체를 대표하거나 문화적 특성을 단정하는 근거로 사용할 수 없습니다."
)

selected_countries = st.multiselect(
    "비교할 나라를 선택하세요 🗺️",
    options=list(COUNTRY_DATA.keys()),
    default=["대한민국 🇰🇷", "미국 🇺🇸", "일본 🇯🇵"],
    max_selections=5,
)

if selected_countries:
    chart_data = []
    for country in selected_countries:
        row = {"국가": country}
        row.update(COUNTRY_DATA[country])
        chart_data.append(row)

    st.bar_chart(
        chart_data,
        x="국가",
        y=list(GROUP_HELP.keys()),
        height=500,
    )

    st.subheader("📌 선택한 나라의 가장 높은 그룹")
    columns = st.columns(len(selected_countries))
    for col, country in zip(columns, selected_countries):
        group = max(COUNTRY_DATA[country], key=COUNTRY_DATA[country].get)
        with col:
            st.metric(country, group, f"{COUNTRY_DATA[country][group]}%")
else:
    st.info("👆 한 개 이상의 나라를 선택해 주세요.")

with st.expander("🧩 네 가지 그룹에는 어떤 유형이 있을까요?"):
    for group, types in GROUP_HELP.items():
        st.write(f"**{group}**: {types}")

st.subheader("💭 자료를 비판적으로 읽어 보기")
st.markdown(
    """
- 나라별 차이가 개인 한 명의 성격을 설명해 주지는 않아요.
- 번역된 문항의 표현, 검사에 참여한 연령층, 온라인 서비스 이용률도 결과에 영향을 줄 수 있어요.
- 같은 나라 안에서도 지역·세대·표본에 따라 분포가 달라질 수 있어요.
"""
)

st.caption("자료 구성 참고: 16Personalities World Personality Map의 조사 방식 · 수업용 예시 데이터")
