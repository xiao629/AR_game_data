from re import I
from django.shortcuts import render
from .models import kstest
from plotly.offline import plot
from plotly.graph_objs import Scatter
import pandas as pd
# import matplotlib.pyplot as plt


def home(request):                                      #主頁
    return render(request, 'posts/home.html')

def test(request):
    #讀取一個CSV檔案的 data並給予變數
    Global=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
    totalCount=Global[Global.columns[-1]].sum()         #加總全球各區域、國家的感染人數
    barPlotData=Global[['Country/Region',Global.columns[-1]]].groupby('Country/Region').sum()       #選擇國家、及其感染數量兩筆資料，給顯示上各感染數 － 國家,感染數量
    barPlotData=barPlotData.reset_index()               #輸出上面設定的數值後，若沒reset會有兩個值導致錯誤
    barPlotData.columns=['Country/Region','values']     #將國家,感人數排成列
    barPlotData=barPlotData.sort_values(by='values',ascending=False)        #將值排序sort，反過來排序
    barPlotvals=barPlotData['values'].values.tolist()                      #抓感染值並以list方式顯示
 
    countryNames=barPlotData['Country/Region'].values.tolist()              
    context={'totalCount':totalCount,'countryNames':countryNames,'barPlotvals':barPlotvals,}

    return render(request,'posts/test.html',context)

def piechart(request):
    world=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
    ttc=world[world.columns[-1]].sum()
    piedata=world[['Country/Region',world.columns[-1]]].groupby('Country/Region').sum()
    piedata=piedata.reset_index()
    piedata.columns=['Country/Region','values']
    piedata=piedata.sort_values("values",ascending=False).head(10)
    pievalu=piedata['values'].values.tolist()
    # autopct=piedata['values'/'']

    cNames=piedata['Country/Region'].values.tolist()
    context={'ttc':ttc,'cNames':cNames,'pievalu':pievalu}
    return render(request,'posts/DTPick.html',context)



def TPS(request):
    if request.method=="POST":
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        searchresult=kstest.objects.raw('select ks_id,ks_name,ks_time from posts_kstest where ks_time between "'+fromdate+'" AND "'+todate+'" ')
        return render(request,'posts/temp_search.html',{"data":searchresult})   
    else:
        x_data = [0,1,2,3]
        y_data = [x**2 for x in x_data]
        data = Scatter(x=x_data,y=y_data,mode='lines',name='Line',opacity=0.8,marker_color='red')
        plot_div = plot([data],output_type='div')
        # context = {'plot_div':plot_div}
        displaydb=kstest.objects.all()
        return render(request,'posts/temp_search.html',{'data':displaydb,'plot_div':plot_div})

def linechart(request):
    x_data = [0,1,2,3]
    y_data = [0,1,2,3]
    data = Scatter(x=x_data,y=y_data,mode='lines',name='Line',opacity=1,marker_color='red')
    plot_div = plot([data],output_type='div')
    return render(request,'posts/linechart.html',{'plot_div':plot_div})

