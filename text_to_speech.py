from gtts import gTTS
from playsound import playsound

file_name = 'sample.mp3'

# 영어 문장
# text = 'We like to think of ourselves as an "interactive online textbook" with a built-in "certification engine" that can be used in either remote or physical classrooms. The course is delivered through a standard web browser and will work on any desktop, laptop, tablet, or mobile phone with an Internet connection.'
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)
# playsound(file_name) # .mp3 파일 재생

# 한글 문장
# text = '파이썬을 배우면 이런 것도 할 수 있어요!'
# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save(file_name)
# playsound(file_name) # .mp3 파일 재생

# 긴 문장 (파일에서 불러와서 처리)
with open('sample.txt', 'r', encoding='utf8') as f:
    text = f.read()

tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)
playsound(file_name) # .mp3 파일 재생