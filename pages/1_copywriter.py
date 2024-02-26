import streamlit as st
from common import request_chat_completion, print_streaming_response


st.set_page_config(
    page_title = "chatGPT API 서비스 개발",
    page_icon="🧠"
)

st.title("AI 카피라이터")
st.subheader("AI를 이용해서 손쉽게 마케팅 문구를 작성해보세요!")
auto_complete = st.toggle("예시로 채우기")

example = {
    "product_name":"카누",
    "product_desc":"집에서도 카페 맛이 나는 커피믹스",
    "keywords":["브라질", "향기", "공유"],
}

prompt_template = """
제품 혹은 브랜드를 SNS에 광고하기 위한 문구를 {num}개 생성해주세요.
자극적이고 창의적으로 작성해주세요.
명사 위주로 간결하게 작성해주세요.
반드시 {max_length} 단어 이내로 작성해주세요.
키워드가 주어질 경우, 반드시 키워드 중 하나를 포함해야 합니다.
이모지를 적절하게 사용해주세요.
---
제품명: {product_name}
제품설명: {product_desc}
키워드: {keywords}
---
""".strip()

with st.form("form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        product_name = st.text_input(
            "제품명",
            placeholder=example["product_name"],
            value=example["product_name"] if auto_complete else ""
        )
    with col2:
        max_length = st.number_input(
            label="최대 단어 수",
            min_value=5,
            max_value=20,
            step=1,
            value=10
        )
    with col3:
        num = st.number_input(
            label="생성할 문구 수",
            min_value=1,
            max_value=10,
            step=1,
            value=5
        )    
    product_desc = st.text_input(
        "제품 설명",
        placeholder=example["product_desc"],
        value=example["product_desc"] if auto_complete else ""
    )
    st.text("포함할 키워드를 최대 3개까지 입력해주세요.")
    col1, col2, col3 = st.columns(3)
    with col1:
        keyword_1 = st.text_input(
            label="keyword_1",
            label_visibility="collapsed",
            placeholder="키워드 1",
            value=example["keywords"][0] if auto_complete else ""
        )
    with col2:
        keyword_2 = st.text_input(
            label="keyword_2",
            label_visibility="collapsed",
            placeholder="키워드 2",
            value=example["keywords"][1] if auto_complete else ""
        )
    with col3:
        keyword_3 = st.text_input(
            label="keyword_3",
            label_visibility="collapsed",
            placeholder="키워드 3",
            value=example["keywords"][2] if auto_complete else ""
        )
    
    
    submit = st.form_submit_button("Submit")
if submit:
    if not product_name:
        st.error("제품명을 추가해주세요.")
    elif not product_desc:
        st.error("제품 설명을 추가해주세요.")
    else:
        keywords = [keyword_1, keyword_2, keyword_3]
        keywords = [x for x in keywords if x]
        prompt = prompt_template.format(            
            product_name=product_name,
            product_desc=product_desc,
            max_length=max_length,
            num=num,
            keywords=keywords
        )
        system_role = "당신은 전문 카피라이터입니다."
        with st.spinner("마케팅 문구를 생성 중입니다."):
            response = request_chat_completion(
                prompt=prompt,
                system_role=system_role,
                stream=True
            )
        print_streaming_response(response)