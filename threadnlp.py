# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 17:31:47 2018

@author: Yosiyoshi
"""
import jieba.analyse
import pythainlp as ptn
from janome.tokenizer import Tokenizer
import threading
import time
def segjp():
    while True:
        txt="清水寺は、京都府京都市東山区清水にある寺院。山号は音羽山。"
        t=Tokenizer()
        token = t.tokenize(txt, wakati=True)
        print(token)
        time.sleep(1)
        print("Thread 1 completed")
def sumth():
    while True:
        txt="""วัดพระศรีรัตนศาสดาราม หรือที่เรียกกันทั่วไปว่า วัดพระแก้ว 
        เป็นวัดที่พระบาทสมเด็จพระพุทธยอดฟ้าจุฬาโลกมหาราชโปรดเกล้าฯให้สร้างขึ้นในพ.ศ.
        2325 เป็นวัดในพระบรมมหาราชวังเช่นเดียวกับวัดพระศรีสรรเพชญ์ ซึ่งเป็นวัดในพระราชวังหลวงในสมัยอยุธยา
        และมีพระราชประสงค์ให้วัดพระศรีรัตนศาสดารามเป็นที่ประดิษฐาน พระพุทธมหามณีรัตนปฏิมากร
        หรือพระแก้วมรกต พระคู่บ้านคู่เมืองของแผ่นดินสยามที่พบ ณ วัดป่าเยี้ยะ(ป่าไผ่) จังหวัดเชียงราย
        และเป็นสถานที่ทรงบำเพ็ญพระราชกุศล วัดพระศรีรัตนศาสดารามเป็นวัดที่ไม่มีพระสงฆ์จำพรรษาอยู่
        เพราะมีแต่ส่วนพุทธาวาสไม่มีส่วนสังฆาวาส"""
        seg=ptn.summarize.summarize_text(txt,n=1,engine='frequency')
        print(seg)
        time.sleep(1)
        print("Thread 2 completed")

if __name__ == "__main__":
    thread1=threading.Thread(target=sumth)
    thread2=threading.Thread(target=segjp)
    thread1.start()
    thread2.start()