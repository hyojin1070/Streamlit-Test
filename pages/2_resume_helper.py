import streamlit as st
from common import request_chat_completion, print_streaming_response


st.set_page_config(
    page_title = "chatGPT API 서비스 개발",
    page_icon="🧠"
)

st.title("자기소개서 도우미")
st.subheader("자기소개서 문항과 지원자의 경험을 바탕으로 초안을 작성해줍니다!")
auto_complete = st.toggle("예제로 채우기")

example = {
    "company": "LG uplus",
    "position": "기업부문 B2B 국내영업",
    "max_length": 500,
    "question": "소속된 조직의 공동과업을 달성하는 과정에서 발생했던 어려움과 그 어려움을 극복하기 위해 기울인 노력에 대해 구체적인 사례를 바탕으로 기술해 주십시오.",
    "experience": "대학교 3학년 때 축구부 주장 역임.\n총장배 대회 우승이라는 공동의 목표로 함께 노력.\n주전 선수진 부상으로 어려움 겪었으나, 극복하고 8강 진출이라는 성과 달성"
}

prompt_template = """
기업 입사용 자기소개서를 작성해야 합니다.
답변해야하는 질문과 이에 관련된 유저의 경험을 참고하여 자기소개서를 작성해주세요.
반드시 {max_length} 단어 이내로 작성해야 합니다.
각 단락마다 소제목을 넣어주세요.

---
지원 회사: {company}
지원 직무: {position} 
질문: {question}
관련 경험: {experience}
---
""".strip()

with st.form("form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        company = st.text_input(
            "지원 기업",
            value=example["company"] if auto_complete else "",
            placeholder=example["company"]
        )
    with col2:
        position = st.text_input(
            "지원 직무",
            value=example["position"] if auto_complete else "",
            placeholder=example["position"]
        )
    with col3:
        max_length = st.number_input(
            "최대 길이",
            min_value=100,
            max_value=2000,
            step=100,
            value=500
        )
    question = st.text_area(
        "질문",
        value=example["question"] if auto_complete else "",
        placeholder=example["question"]
    )
    experience = st.text_area(
        "질문과 관련된 경험",
        value=example["experience"] if auto_complete else "",
        placeholder=example["experience"]
    )
    submit = st.form_submit_button("제출하기")
if submit:
    if not company:
        st.error("지원하는 회사를 입력해주세요.")
    elif not position:
        st.error("지원하는 직무를 입력해주세요.")
    elif not question:
        st.error("자기소개서 문항을 입력해주세요.")
    elif not experience:
        st.error("본인의 경험을 작성해주세요.")
    else:
        prompt = prompt_template.format(
            company=company,
            position=position,
            max_length=max_length // 6,
            question=question,
            experience=experience
        )
        system_role = "당신은 취업 전문 컨설턴트입니다."
        response = request_chat_completion(
            prompt=prompt,
            system_role=system_role,
            stream=True
        )
        message = print_streaming_response(response)
        st.markdown(f"**공백 포함 글자 수: {len(message)}**")