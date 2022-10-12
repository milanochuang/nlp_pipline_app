# 國立政治大學 語言所碩二 莊昊耘
# url: https://milanochuang-nlp-pipline-app-app-b3k6vm.streamlitapp.com/

from asyncore import read
from sys import api_version
import streamlit as st
import json
import os
from crawl import crawler
from read import file_exists, read_json
from sentiment import get_sent_score
from threading import Thread
import pandas as pd
import shutil


st.title("社會情緒波動感測器")
index_from = st.number_input('這裡輸入開始的頁數（不得小於 16500）')
index_to = st.number_input('這裡輸入結束的頁數（不得大於 39115）')
st.write("兩者相差最好不要太大，不然會跑很久很久喔！")
if index_from and index_to:
    index_from = int(index_from)
    index_to = int(index_to)
    st.write("你所輸入的頁數為{}到{}".format(index_from, index_to))
    bash_code = "cd ptt-crawler && scrapy crawl ptt -a boards=Gossiping -a index_from={} -a index_to={}".format(index_from, index_to)
    thread = Thread(group=None, target=lambda:os.system(bash_code))
    thread.run()
    # Later
    if thread.is_alive():
        pass
    else:
        if file_exists:
            resultLIST = read_json()
            resultDICT = {}
            for post in resultLIST:
                date = post['date']
                article = post['article']
                score = get_sent_score(article)
                if date in resultDICT:
                    resultDICT[date].append(score)
                else:
                    resultDICT[date] = []
                    resultDICT[date].append(score)
            resultDF = pd.DataFrame(resultDICT.items(), columns=['Date', 'Score'])
            average_list = []
            for value in resultDF['Score']:
                average = sum(value)/len(value)
                average_list.append(average)
            resultDF['Average'] = average_list
            st.line_chart(resultDF, x='Date', y='Average')
            shutil.rmtree("./ptt-crawler/data")
            
    
# with open("./ptt-crawler/data/Soft_Job/2022/M.1661432028.A.2E0.json", 'r') as f:
#     test = json.load(f)
# st.write(test)

# if __name__ == "__main__":
#     # os.system("cd ptt-crawler && pip install -r requirements.txt")
#     # os.system("cd ptt-crawler && scrapy crawl ptt -a boards=Soft_Job -a index_from=1722 -a index_to=1723")
#     for filename in os.listdir("./ptt-crawler/data/Soft_Job/2022"):
#         # print(filename)
#         with open(os.listdir("./ptt-crawler/data/Soft_Job/2022", filename), 'r') as f:


            
