import time
import re
import speech_recognition as sr

start_time = None  # เก็บเวลาเริ่ม
elapsed_time = 0   # เก็บเวลาที่ผ่านไป

# สร้างฟังก์ชันเริ่มจับเวลา
def start_stopwatch():
    global start_time
    start_time = time.time()
    print("⏱️ เริ่มจับเวลา...")

# สร้างฟังก์ชันหยุดจับเวลา
def stop_stopwatch():
    global start_time
    if start_time is None:
        print("⚠️ ยังไม่ได้เริ่มจับเวลา!")
    else:
        elapsed_time = time.time() - start_time
        print(f"⏹️ เวลาที่ผ่านไป: {elapsed_time:.2f} วินาที")
        start_time = None  # reset

# --- เริ่มการทำงานของ Speech Recognition ---
r = sr.Recognizer()
with sr.Microphone() as mic:
    r.adjust_for_ambient_noise(mic, duration=0.6)
    print("🎤 พูดคำสั่ง เช่น 'สวัสดี', 'สั่งงาน จับเวลา', หรือ 'สั่งงาน หยุดจับเวลา'")

    while True:
        try:
            audio = r.listen(mic, timeout=6, phrase_time_limit=10)
            text = r.recognize_google(audio, language="th-TH").strip().lower()
            print("ได้ยิน :", text)

            if text.startswith("สวัสดี"):
                # แยกข้อความหลังคำว่าสวัสดี (ถ้ามี)
                cmd = text.replace("สวัสดี", "", 1).strip()
                print("👋 สวัสดีครับ คุณธนกร!", end="")
                if cmd:
                    print(f" คุณพูดต่อว่า: {cmd}")
                else:
                    print()

            elif text in ["สั่งงาน จับเวลา", "เริ่มจับเวลา", "start stopwatch"]:
                start_stopwatch()

            elif text in ["สั่งงาน หยุดจับเวลา", "หยุดจับเวลา", "stop stopwatch"]:
                stop_stopwatch()

            elif text in ["ออก", "หยุดโปรแกรม", "exit"]:
                print("👋 จบการทำงาน")
                break

            else:
                # ตรวจจับคำสั่งที่มีตัวเลข (ตัวอย่างที่คุณให้มา)
                m = re.search(r"(\d+)", text)
                if m:
                    angle = int(m.group(1))
                    print(f"📏 ตรวจพบมุม: {angle}")
                else:
                    print("❓ ไม่เข้าใจคำสั่ง ลองใหม่อีกครั้ง")

        except sr.WaitTimeoutError:
            print("⏳ ไม่มีเสียงพูด ตรวจจับไม่ทันเวลา")

        except sr.UnknownValueError:
            print("🤔 ไม่เข้าใจ ลองพูดใหม่อีกครั้ง")
