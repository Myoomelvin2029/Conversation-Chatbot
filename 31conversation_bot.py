import streamlit as st
import re

eng_to_kor = {"q": "ㅂ","w": "ㅈ","e": "ㄷ","r": "ㄱ","t": "ㅅ","y": "ㅛ","u": "ㅕ","i": "ㅑ","o": "ㅐ",
    "p": "ㅔ","a": "ㅁ","s": "ㄴ","d": "ㅇ","f": "ㄹ","g": "ㅎ","h": "ㅗ","j": "ㅓ","k": "ㅏ","l": "ㅣ",
    "z": "ㅋ","x": "ㅌ","c": "ㅊ","v": "ㅍ","b": "ㅠ","n": "ㅜ","m": "ㅡ"} 
# 세션 상태 
if 'messages' not in st.session_state: 
    st.session_state.messages = []
if 'num_reply' not in st.session_state:
    st.session_state.num_reply = 0
# 제목 
st.title("Conversation Chat Bot")
for message in st.session_state.messages : 
    with st.chat_message(message['role']) :
        st.markdown(message['content'])
if prompt := st.chat_input("메세지를 입력하세요.") :
    st.session_state.messages.append({'role' : 'user', 'content' : prompt})
    with st.chat_message("user") : 
        st.markdown(prompt)
    # AI 응답 생성
    with st.chat_message("assistant") :
        st.session_state.num_reply += 1 
        response = f'{st.session_state.num_reply} 번째 답변 : '
        # 연산자가 문자열에 입력되면 제외시키기 
        try: 
            eval(prompt)
        except: 
            pattern = r'[+/*\-]'
            prompt = re.sub(pattern," ",prompt) # 패턴, 바꾸는 값, 대상
        else:
            pass  
        # 간단한 인사
        if '안녕' in prompt : 
            response += '안녕하셍요!'
        elif '시간' in prompt :
            from datetime import datetime 
            time = datetime.now()
            response += time.strftime("%m 월 %d 일 %H 시 %M 분 %p  %a 요일")
        elif re.search(r'[+\-/*]',prompt) :
            response += str(eval(prompt))  
        elif re.match('[a-zA-z]', prompt):  
                word = ''
                for i in prompt :
                    word +=  eng_to_kor[i]
                    response = word
        # 시간 -> 현재시간, 날짜, 요일 정보를 response 해주는 기능 추가하기 
        else :  
            response += f'당신의 질문은 {prompt} 입니다'
        st.markdown(response)
        

    st.session_state.messages.append({'role' : "assistant", 'content' : response})