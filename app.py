import streamlit as st


st.set_page_config(
    page_title="MBTI 진로 탐색소",
    page_icon="🧭",
    layout="centered",
)


CAREERS = {
    "ISTJ": {
        "label": "청렴결백한 논리주의자",
        "keywords": ["체계적", "책임감", "정확성"],
        "careers": [
            ("📊", "회계사", "자료를 꼼꼼하게 확인하고 원칙에 따라 정확하게 판단하는 강점을 살릴 수 있어요."),
            ("🗂️", "행정공무원", "정해진 절차를 안정적으로 운영하고 맡은 일을 책임감 있게 완수하는 역량이 중요해요."),
            ("🛡️", "정보보안 전문가", "작은 이상 징후를 놓치지 않고 체계적으로 위험을 점검하는 성향과 잘 맞아요."),
        ],
    },
    "ISFJ": {
        "label": "용감한 수호자",
        "keywords": ["배려심", "성실함", "세심함"],
        "careers": [
            ("🩺", "간호사", "사람의 상태를 세심하게 살피고 꾸준히 돌보는 강점을 발휘할 수 있어요."),
            ("🧸", "유아교사", "상대의 필요를 알아차리고 안정적인 환경을 만드는 능력이 중요해요."),
            ("🤝", "사회복지사", "도움이 필요한 사람의 이야기를 듣고 현실적인 지원을 연결하는 직업이에요."),
        ],
    },
    "INFJ": {
        "label": "선의의 옹호자",
        "keywords": ["통찰력", "공감", "가치지향"],
        "careers": [
            ("💬", "상담심리사", "사람의 말과 감정 속 의미를 이해하고 성장을 돕는 강점을 살릴 수 있어요."),
            ("✍️", "작가", "자신만의 관점과 메시지를 깊이 있는 이야기로 표현할 수 있어요."),
            ("🌱", "사회혁신 기획자", "사회문제를 발견하고 더 나은 변화를 위한 프로젝트를 설계하는 직업이에요."),
        ],
    },
    "INTJ": {
        "label": "용의주도한 전략가",
        "keywords": ["전략적", "독립적", "분석적"],
        "careers": [
            ("🤖", "인공지능 연구원", "복잡한 문제의 원리를 분석하고 새로운 해결 방법을 설계하는 데 강점을 발휘해요."),
            ("🏗️", "건축가", "큰 그림을 구상하면서 기능과 구조를 논리적으로 연결하는 능력이 필요해요."),
            ("📈", "데이터 과학자", "데이터 속 규칙을 찾고 장기적인 의사결정 전략을 제안하는 직업이에요."),
        ],
    },
    "ISTP": {
        "label": "만능 재주꾼",
        "keywords": ["문제해결", "실용적", "침착함"],
        "careers": [
            ("🔧", "기계공학자", "기계가 작동하는 원리를 이해하고 직접 개선하는 과정에서 강점을 살릴 수 있어요."),
            ("💻", "소프트웨어 개발자", "문제를 논리적으로 나누고 효율적인 해결책을 구현하는 직업이에요."),
            ("🚁", "드론 조종·정비 전문가", "상황을 빠르게 판단하고 기기를 정밀하게 다루는 능력이 중요해요."),
        ],
    },
    "ISFP": {
        "label": "호기심 많은 예술가",
        "keywords": ["감각적", "유연함", "따뜻함"],
        "careers": [
            ("🎨", "시각디자이너", "섬세한 감각과 개성을 이미지로 표현하며 사람에게 메시지를 전달할 수 있어요."),
            ("🐾", "동물보건사", "생명을 세심하게 관찰하고 편안하게 돌보는 따뜻한 태도가 중요해요."),
            ("📷", "사진작가", "순간의 분위기와 감정을 자신만의 시선으로 포착하는 직업이에요."),
        ],
    },
    "INFP": {
        "label": "열정적인 중재자",
        "keywords": ["창의성", "공감", "이상추구"],
        "careers": [
            ("📚", "출판 편집자", "좋은 이야기를 발견하고 독자에게 의미 있게 전달하는 과정과 잘 맞아요."),
            ("🎬", "콘텐츠 기획자", "상상력과 가치관을 영상·웹툰·미디어 콘텐츠로 구체화할 수 있어요."),
            ("🫶", "청소년상담사", "학생의 마음을 존중하며 스스로 답을 찾도록 돕는 공감 능력이 중요해요."),
        ],
    },
    "INTP": {
        "label": "논리적인 사색가",
        "keywords": ["호기심", "논리적", "아이디어"],
        "careers": [
            ("🔬", "과학 연구원", "궁금한 현상의 원리를 탐구하고 가설을 검증하는 과정을 즐길 수 있어요."),
            ("🧑‍💻", "백엔드 개발자", "복잡한 시스템의 구조를 논리적으로 설계하고 개선하는 직업이에요."),
            ("🎮", "게임 시스템 기획자", "규칙과 구조를 설계해 새롭고 균형 잡힌 경험을 만드는 데 강점을 발휘해요."),
        ],
    },
    "ESTP": {
        "label": "모험을 즐기는 사업가",
        "keywords": ["실행력", "순발력", "도전적"],
        "careers": [
            ("🚒", "소방관", "빠르게 변하는 현장에서 침착하게 판단하고 행동하는 역량이 중요해요."),
            ("📣", "스포츠 마케터", "사람들과 활발하게 소통하며 현장의 반응을 전략으로 연결할 수 있어요."),
            ("🚀", "창업가", "기회를 빠르게 발견하고 아이디어를 실제 서비스로 실행하는 강점을 살릴 수 있어요."),
        ],
    },
    "ESFP": {
        "label": "자유로운 영혼의 연예인",
        "keywords": ["사교적", "낙천적", "표현력"],
        "careers": [
            ("🎤", "방송인", "풍부한 표현력으로 사람들과 에너지를 나누는 강점을 발휘할 수 있어요."),
            ("🎉", "행사 기획자", "현장 분위기를 읽고 많은 사람이 즐길 경험을 만드는 직업이에요."),
            ("🧳", "여행 콘텐츠 크리에이터", "새로운 경험을 생생하게 전달하고 사람들과 소통하는 능력이 중요해요."),
        ],
    },
    "ENFP": {
        "label": "재기발랄한 활동가",
        "keywords": ["열정적", "창의적", "소통"],
        "careers": [
            ("💡", "광고 기획자", "다양한 아이디어를 사람의 마음을 움직이는 메시지로 발전시킬 수 있어요."),
            ("📺", "콘텐츠 크리에이터", "새로운 주제를 발견하고 개성 있게 표현하며 대중과 소통하는 직업이에요."),
            ("🏫", "진로교육 전문가", "여러 사람의 가능성을 발견하고 새로운 도전을 응원하는 강점을 살릴 수 있어요."),
        ],
    },
    "ENTP": {
        "label": "뜨거운 논쟁을 즐기는 변론가",
        "keywords": ["도전적", "발상력", "토론"],
        "careers": [
            ("⚖️", "변호사", "여러 관점에서 논리를 검토하고 설득력 있게 주장을 펼치는 역량이 중요해요."),
            ("🧪", "제품 기획자", "기존 방식에 질문을 던지고 새로운 제품이나 서비스를 구상할 수 있어요."),
            ("🏢", "경영 컨설턴트", "다양한 문제를 빠르게 분석하고 창의적인 해결 전략을 제시하는 직업이에요."),
        ],
    },
    "ESTJ": {
        "label": "엄격한 관리자",
        "keywords": ["조직력", "결단력", "현실적"],
        "careers": [
            ("📋", "프로젝트 매니저", "목표와 일정을 정리하고 구성원이 성과를 내도록 이끄는 강점을 살릴 수 있어요."),
            ("👮", "경찰관", "원칙을 바탕으로 상황을 판단하고 공동체의 질서를 지키는 역할이에요."),
            ("🏭", "생산관리 전문가", "사람과 자원을 체계적으로 배치해 효율적으로 운영하는 능력이 중요해요."),
        ],
    },
    "ESFJ": {
        "label": "사교적인 외교관",
        "keywords": ["협력적", "친절함", "책임감"],
        "careers": [
            ("👩‍🏫", "교사", "학생과 꾸준히 소통하며 성장을 돕고 교실 공동체를 만드는 직업이에요."),
            ("🏥", "의료 코디네이터", "사람의 불편을 세심하게 파악하고 필요한 의료 서비스를 연결해요."),
            ("✈️", "항공 객실승무원", "다양한 사람을 친절하게 응대하고 협력해 안전을 지키는 역량이 중요해요."),
        ],
    },
    "ENFJ": {
        "label": "정의로운 사회운동가",
        "keywords": ["리더십", "공감", "동기부여"],
        "careers": [
            ("🧭", "진로상담교사", "학생의 강점을 발견하고 목표를 세워 성장하도록 돕는 역할과 잘 맞아요."),
            ("🌍", "국제기구 활동가", "다양한 사람과 협력하며 공동체의 문제를 해결하는 데 기여할 수 있어요."),
            ("👥", "인사·교육 담당자", "구성원의 가능성을 파악하고 함께 성장하는 조직문화를 만드는 직업이에요."),
        ],
    },
    "ENTJ": {
        "label": "대담한 통솔자",
        "keywords": ["목표지향", "전략적", "리더십"],
        "careers": [
            ("💼", "경영전략가", "목표를 세우고 자원을 효과적으로 활용할 장기 전략을 설계할 수 있어요."),
            ("⚙️", "기술 프로젝트 책임자", "전문가들과 협업하며 복잡한 기술 프로젝트를 이끄는 역할이에요."),
            ("⚖️", "검사", "사실과 논리를 바탕으로 판단하고 책임 있게 결정을 내리는 역량이 중요해요."),
        ],
    },
}


st.markdown(
    """
    <style>
    .block-container {max-width: 850px; padding-top: 2.2rem; padding-bottom: 3rem;}
    .hero {
        padding: 2rem 1.5rem;
        border-radius: 24px;
        text-align: center;
        background: linear-gradient(135deg, #EEF2FF 0%, #FDF2F8 100%);
        border: 1px solid #E0E7FF;
        margin-bottom: 1.5rem;
    }
    .hero h1 {margin: 0; color: #312E81; font-size: 2.25rem;}
    .hero p {margin: .7rem 0 0; color: #4B5563; font-size: 1.05rem;}
    .type-box {
        padding: 1.25rem 1.4rem;
        border-radius: 18px;
        background: #FFFFFF;
        border-left: 6px solid #8B5CF6;
        box-shadow: 0 6px 22px rgba(76, 29, 149, .08);
        margin: 1.1rem 0 1.4rem;
    }
    .type-box h2 {margin: 0 0 .3rem; color: #4C1D95;}
    .type-box p {margin: 0; color: #6B7280;}
    .tag {
        display: inline-block;
        padding: .25rem .65rem;
        margin: .7rem .25rem 0 0;
        border-radius: 999px;
        background: #EDE9FE;
        color: #5B21B6;
        font-size: .88rem;
        font-weight: 700;
    }
    .career-card {
        min-height: 235px;
        padding: 1.2rem;
        border-radius: 18px;
        background: #FAFAFF;
        border: 1px solid #EDE9FE;
        box-shadow: 0 4px 14px rgba(17, 24, 39, .05);
    }
    .career-icon {font-size: 2rem;}
    .career-card h3 {margin: .45rem 0 .6rem; color: #3730A3;}
    .career-card p {color: #4B5563; line-height: 1.65;}
    .footer-note {
        margin-top: 1.8rem;
        padding: 1rem 1.2rem;
        border-radius: 14px;
        background: #FFFBEB;
        border: 1px solid #FDE68A;
        color: #78350F;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <h1>🧭 MBTI 진로 탐색소</h1>
        <p>나의 성향을 힌트 삼아 미래의 가능성을 가볍게 탐색해 보세요! ✨</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.subheader("🔎 나의 MBTI를 선택해 주세요")
selected_mbti = st.selectbox(
    "MBTI 유형",
    options=list(CAREERS.keys()),
    index=None,
    placeholder="MBTI를 선택하면 직업을 추천해 드려요 👇",
    label_visibility="collapsed",
)

if selected_mbti:
    info = CAREERS[selected_mbti]
    tags = "".join(f'<span class="tag">#{word}</span>' for word in info["keywords"])
    st.markdown(
        f"""
        <div class="type-box">
            <h2>{selected_mbti} · {info['label']}</h2>
            <p>이 유형이 자주 보이는 강점을 중심으로 살펴봤어요.</p>
            {tags}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("🌟 추천 직업 3가지")
    columns = st.columns(3)
    for column, (icon, job, reason) in zip(columns, info["careers"]):
        with column:
            st.markdown(
                f"""
                <div class="career-card">
                    <div class="career-icon">{icon}</div>
                    <h3>{job}</h3>
                    <p>{reason}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
        <div class="footer-note">
            💡 <b>상담 선생님의 한마디</b><br>
            MBTI는 나를 이해하는 여러 도구 중 하나일 뿐, 진로를 결정하는 정답은 아니에요.
            추천 결과와 함께 내가 좋아하는 활동, 잘하는 과목, 중요하게 생각하는 가치도 살펴보세요.
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.info("👆 먼저 MBTI를 선택해 주세요. 나에게 어울리는 진로 힌트가 나타나요!")

st.caption("🌈 오늘의 선택이 평생의 직업을 정하지는 않아요. 다양한 경험으로 나만의 길을 찾아가세요.")
