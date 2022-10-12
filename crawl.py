import os

def crawler(index_from, index_to):
    # os.system("cd ptt-crawler && pip install -r requirements.txt")
    os.system("cd ptt-crawler && scrapy crawl ptt -a boards=Gossiping -a index_from={} -a index_to={}".format(index_from, index_to))
    """
    This drives the terminal to crawl ptt, and index_from must not less than 16500
    """