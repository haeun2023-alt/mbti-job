import streamlit as st


st.set_page_config(page_title="나의 진로 가치관", page_icon="💎", layout="centered")

VALUES = {
    "성장 🌱": {
        "description": "새로운 것을 배우고 능력을 발전시키는 것을 중요하게 생각해요.",
        "jobs": ["연구원", "소프트웨어 개발자", "교사"],
        "question": "이 직업에서 나는 무엇을 새롭게 배우고 성장할 수 있을까?",
    },
    "안정 🏡": {
        "description": "예측 가능한 환경과 꾸준한 생활을 중요하게 생각해요.",
        "jobs": ["공무원", "회계사", "품질관리 전문가"],
        "question": "이 직업의 근무 환경과 생활 방식은 얼마나 안정적일까?",
    },
    "창의성 🎨": {
        "description": "새로운 아이디어를 표현하고 나만의 결과물을 만드는 것을 중요하게 생각해요.",
        "jobs": ["콘텐츠 기획자", "디자이너", "게임 기획자"],
        "question": "이 직업에서 내 아이디어를 얼마나 자유롭게 표현할 수 있을까?",
    },
    "사회적 기여 🤝": {
        "description": "사람과 사회에 긍정적인 변화를 만드는 것을 중요하게 생각해요.",
        "jobs": ["상담사", "사회복지사", "환경정책 연구원"],
        "question": "이 일을 통해 누구에게 어떤 도움을 줄 수 있을까?",
    },
    "도전 🚀": {
        "description": "어려운 목표에 도전하고 성취감을 느끼는 것을 중요하게 생각해요.",
        "jobs": ["창업가", "프로젝트 매니저", "항공우주공학자"],
        "question": "이 직업에서는 어떤 새로운 문제와 도전을 만날 수 있을까?",
    },
    "자율성 🕊️": {
        "description": "내 방식대로 계획하고 스스로 결정할 수 있는 환경을 중요하게 생각해요.",
        "jobs": ["프리랜서 개발자", "작가", "사진작가"],
        "question": "이 직업에서 내가 결정할 수 있는 범위는 얼마나 넓을까?",
    },
}

st.title("💎 나의 진로 가치관 찾기")
st.write("MBTI와 함께 **내가 직업에서 중요하게 생각하는 것**도 살펴보세요.")

st.info("정답은 없어요. 지금의 나에게 더 중요한 정도를 솔직하게 선택하면 됩니다. 😊")

scores = {}
with st.form("career_value_form"):
    for value, info in VALUES.items():
        scores[value] = st.slider(
            f"{value} — {info['description']}",
            min_value=1,
            max_value=5,
            value=3,
            help="1점: 중요하지 않다 · 5점: 매우 중요하다",
        )
    submitted = st.form_submit_button("✨ 나의 핵심 가치관 확인하기", use_container_width=True)

if submitted:
    ranked = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    top_score = ranked[0][1]
    top_values = [value for value, score in ranked if score == top_score]

    st.success(f"나의 핵심 진로 가치관은 **{' · '.join(top_values)}** 입니다!")
    st.bar_chart(
        [{"가치관": value, "점수": score} for value, score in ranked],
        x="가치관",
        y="점수",
        color="#EC4899",
        height=360,
    )

    st.subheader("🔭 진로 탐색 힌트")
    for value in top_values:
        info = VALUES[value]
        st.markdown(f"### {value}")
        st.write(info["description"])
        st.write("**탐색해 볼 직업:** " + " · ".join(info["jobs"]))
        st.write(f"**직업인에게 물어볼 질문:** {info['question']}")

    st.warning(
        "추천 직업은 예시예요. 같은 가치관도 매우 다양한 직업에서 실현할 수 있으니, "
        "직업 이름보다 실제로 하는 일과 근무 환경을 함께 조사해 보세요."
    )
else:
    st.caption("각 항목을 선택한 뒤 결과 확인 버튼을 눌러 주세요. 👆")

with st.expander("📝 진로 노트"):
    st.write("핵심 가치관을 확인한 뒤 아래 문장을 완성해 보세요.")
    st.text_area(
        "나에게 좋은 직업이란?",
        placeholder="예: 새로운 기술을 배우면서 사람들의 불편을 해결할 수 있는 직업",
        height=110,
    )

st.caption("진로 가치관은 경험에 따라 달라질 수 있어요. 새로운 활동을 경험한 뒤 다시 확인해 보세요. 🌈")
