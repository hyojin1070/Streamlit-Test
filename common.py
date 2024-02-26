from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def request_chat_completion(
    prompt,
    system_role="당신은 유용한 도우미입니다.",
    model="gpt-3.5-turbo",
    stream=False
):
    messages = [
        {"role": "system", "content": system_role},
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=stream
    )
    return response


def print_streaming_response(response):
    message = ""
    placeholder = st.empty()
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            message += chunk.choices[0].delta.content
            placeholder.markdown(message + "▌ ")
        else:
            break
    placeholder.markdown(message)
    return message


def print_streaming_response_console(response):
    message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            message += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="")
        else:
            break
    return message