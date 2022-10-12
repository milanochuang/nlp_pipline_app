import json
import os
import re

def file_exists():
    if os.listdir("./ptt-crawler/data/Gossiping/2022"):
        return True
    else:
        return False

def read_json():
    resultLIST = []
    for filename in os.listdir("./ptt-crawler/data/Gossiping/2022"):
        resultDICT = {}
        with open(os.listdir("./ptt-crawler/data/Gossiping/2022", filename), 'r') as f:
            article = json.load(f)
        resultDICT['id'] = article['post_id']
        resultDICT['date'] = re.search("2022-\d{1,2}-\d{1,2}", article['date']).group()
        resultDICT['article'] = article['body'].replace("\n", "")
        resultLIST.append(resultDICT)
    return resultLIST