import pyaudio
p = pyaudio.PyAudio()

for index in range(p.get_device_count()):
    desc = p.get_device_info_by_index(index)
    print("DEVICE: {device}, INDEX: {index}, RATE: {rate} ".format(
        device=desc["name"], index=index, rate=int(desc["defaultSampleRate"])))


# 기본 마이크로폰 장치로 스트림 열기
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                input=True,
                frames_per_buffer=1024,
               input_device_index=8)

# 스트림이 제대로 열렸는지 확인
if stream.is_active():
    print("스트림이 성공적으로 열렸습니다.")
else:
    print("스트림 열기에 실패했습니다.")

# 스트림 닫기
stream.stop_stream()
stream.close()
p.terminate()