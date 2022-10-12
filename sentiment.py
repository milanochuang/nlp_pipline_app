from snownlp import SnowNLP
import seaborn as sns
from matplotlib.font_manager import FontProperties


def get_sent_score(inputSTR):
    result = SnowNLP(inputSTR)
    sentiment_score = result.sentiments
    return sentiment_score

def plot(inputDF):
    sns.set(font=['sans-serif'])
    sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})   
    sent_plot = sns.lineplot(x='Date', y='Average', data=inputDF)
    sent_plot.set_title('社會情緒波動圖')
    return sent_plot