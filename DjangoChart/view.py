# added by grimmer, hello world example
from django.http import HttpResponse
from django.views.generic import TemplateView

from datetime import datetime,timedelta
from django.shortcuts import render

import plotly.offline as opy
import plotly.graph_objs as go

import numpy as np
import pandas as pd

import psycopg2

# def hello(request):
#     return HttpResponse("Hello world ! ")

def get_seconds(time_delta):
    return time_delta.seconds

def selectdata(early, later):
    #connect DB
    con = None
    con_str = "dbname=%s user=%s password=%s" %( , , )
    try:
        con = psycopg2.connect(con_str)
        cur = con.cursor()

        early_str = early.strftime('%Y-%m-%d %H:%M:%S')
        later_str = later.strftime('%Y-%m-%d %H:%M:%S')

    except psycopg2.DatabaseError as e:
        print('Error %s' % e)
        con.commit()
        return None

    sql = "SELECT * FROM belle2grid WHERE time >= TO_TIMESTAMP('%s','YYYY-MM-DD HH24:MI:SS') AND time <= TO_TIMESTAMP('%s','YYYY-MM-DD HH24:MI:SS');" %(early_str, later_str)
    print(sql)
    try:
        df_byte = pd.read_sql(sql,con)
        df_byte.sort_values(by='time',ascending=True)

    except psycopg2.DatabaseError as e:
        print("Error {}".format(e))
        con.commit()

    finally:
        if cur:
            cur.close()
        if con:
            con.close()

    return df_byte

def flowratedf(df_hour):
    #sort by time again
    df_hour.sort_values(by='time', ascending=True)
    #calculate flow rate and return a dataframe
    df_hour['dbyte'] = df_hour['flowbyte'] - df_hour['flowbyte'].shift(1)
    df_hour['dtime'] = df_hour['time'] - df_hour['time'].shift(1)
    df_hour['dtimes'] = df_hour['dtime'].apply(get_seconds)
    df_hour = df_hour.ix[1:,['time','dbyte','dtimes']] #throw away
    df_hour['flowrate'] = pd.eval("df_hour.dbyte/(df_hour.dtimes+0.0001)")
    df_ = df_hour[['time','flowrate']]
    return df_

def mean_hour_rate(df, avghour):
    df = df.set_index('time')
    #df_h = df.resample('H').mean()
    if (avghour is True):
        df_h = df.asfreq('H')   # frequenlt sample data of each hour
    else:
        df_h = df.asfreq('10T')   # frequenlt sample data of each 10 minutes
    return df_h.reset_index()



# template render example:
# https://github.com/twtrubiks/django-tutorial/blob/master/musics/views.py
#     return render(request, 'hello_django.html', {
#         'data': "Hello Django ",
#         'musics': musics,
#     })

def hello(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })


# Embed plotly charts in html
# ref: https://stackoverflow.com/a/38334121/7354486
# or embed this ChartView in normal funciton viewsself.
# g = Graph() context = g.get_context_data()
# return render(request, 'app/stats.html', context)
class ChartView(TemplateView):
    template_name = "chart.html"

    def get_context_data(self, **kwargs):
        days = 30
        context = super(ChartView, self).get_context_data(**kwargs)

        date = np.array('2017-09-12',dtype=np.datetime64)
        date = date+np.random.randint(300,size=1)
        x = date+np.arange(days-1)
        #x = np.array([q**2-q+3 for q in x])
        y1 = np.random.randint(120,size=days)
        y2 = np.random.randint(200,size=days)
        trace1 = go.Scatter(x=x, y=y1, marker={'color': 'red', 'symbol': 104, 'size': 10},
                            mode="lines",  name='1st Trace')
        trace2 = go.Scatter(x=x, y=y2, marker={'color': 'blue', 'symbol': 106, 'size': 10},
                            mode="lines+markers",  name='2nd Trace')
        data=go.Data([trace1,trace2])
        layout=go.Layout(title="Meine Daten", xaxis={'title':'x'}, yaxis={'title':'y'})
        figure=go.Figure(data=data,layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['graph'] = div

        return context

# TODO: Extract the same code of drawing charts for reuse
class ChartView2(TemplateView):
    template_name = "chart.html"

    def get_context_data(self, **kwargs):
        context = super(ChartView2, self).get_context_data(**kwargs)
        # get 4 hours data from database
        now = datetime.now()
        time_interval = timedelta(hours=4) #4 hours
        before = now - time_interval
        df_min = selectdata(before, now)
        if (df_min is not None):
            df = flowratedf(df_min)
            # plus 0.0001 for preventing zero division
            trace1 = go.Scatter(x=df.time, y=df['flowrate'], marker={'color': 'green', 'symbol': 104, 'size': 10},
                                mode="lines",  name='belle2grid2')
            yrange = [0.0, df['flowrate'].max()*1.3]
        else:
            x = [0]
            y = [0]
            trace1 = go.Scatter(x=x, y=y, marker={'color': 'green', 'symbol': 104, 'size': 10},
                                mode="lines",  name='read error')
            yrange= [0.0,1.0]

        data=go.Data([trace1])
        layout=go.Layout(title="Network flowing in 4 hours", xaxis={'title':'Date time'}, yaxis={'title':'byte/s','range':yrange})
        figure=go.Figure(data=data,layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['graph'] = div

        return context

# TODO: Extract the same code of drawing charts for reuse
class ChartView3(TemplateView):
    template_name = "chart.html"

    def get_context_data(self, **kwargs):
        context = super(ChartView3, self).get_context_data(**kwargs)
        # get 12 hours data from database
        now = datetime.now()
        time_interval = timedelta(hours=12) #12 hours
        before = now - time_interval
        df_min = selectdata(before, now)
        if (df_min is not None):
            df = flowratedf(df_min)
            # plus 0.0001 for preventing zero division
            trace1 = go.Scatter(x=df.time, y=df['flowrate'], marker={'color': 'green', 'symbol': 104, 'size': 10},
                                mode="lines",  name='belle2grid2')
            yrange = [0.0, df['flowrate'].max()*1.3]
        else:
            x = [0]
            y = [0]
            trace1 = go.Scatter(x=x, y=y, marker={'color': 'green', 'symbol': 104, 'size': 10},
                                mode="lines",  name='read error')
            yrange=[0.0,1.0]

        data=go.Data([trace1])
        layout=go.Layout(title="Network flowing in 12 hours", xaxis={'title':'Date time'}, yaxis={'title':'byte/s','range':yrange})
        figure=go.Figure(data=data,layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['graph'] = div

        return context

# TODO: Extract the same code of drawing charts for reuse
class ChartView4(TemplateView):
    template_name = "chart.html"

    def get_context_data(self, **kwargs):
        context = super(ChartView4, self).get_context_data(**kwargs)
        # get 1 day data from database
        now = datetime.now()
        time_interval = timedelta(days=1) #1 day
        before = now - time_interval
        df_min = selectdata(before, now)
        if (df_min is not None):
            # avg flowbyte for each hour
            df_tenmin = mean_hour_rate(df_min, False)
            df = flowratedf(df_tenmin)
            # plus 0.0001 for preventing zero division
            trace1 = go.Scatter(x=df.time, y=df['flowrate'], marker={'color': 'green', 'symbol': 104, 'size': 10},
                                mode="lines",  name='belle2grid2')

            yrange = [0.0, df['flowrate'].max()*1.3]
        else:
            x = [0]
            y = [0]
            race1 = go.Scatter(x=x, y=y, marker={'color': 'green', 'symbol': 104, 'size': 10},
                                mode="lines",  name='read error')
            yrange = [0,1]

        data=go.Data([trace1])
        layout=go.Layout(title="Network flowing in 1 day", xaxis={'title':'Date time'}, yaxis={'title':'avg (10 mins) byte/s','range':yrange})
        figure=go.Figure(data=data,layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['graph'] = div

        return context

# TODO: Extract the same code of drawing charts for reuse
class ChartView5(TemplateView):
    template_name = "chart.html"

    def get_context_data(self, **kwargs):
        context = super(ChartView5, self).get_context_data(**kwargs)
        # get 7 days data from database
        now = datetime.now()
        time_interval = timedelta(days=7) #7 day
        before = now - time_interval
        df_min = selectdata(before, now)
        if (df_min is not None):
            # avg flowbyte for each hour
            df_hour = mean_hour_rate(df_min, True)

            df = flowratedf(df_hour)
            # plus 0.0001 for preventing zero division
            trace1 = go.Scatter(x=df.time, y=df['flowrate'], marker={'color': 'green', 'symbol': 104, 'size': 10},
                                mode="lines",  name='belle2grid2')
            yrange = [0.0, df['flowrate'].max()*1.3]
        else:
            x = [0]
            y = [0]
            race1 = go.Scatter(x=x, y=y, marker={'color': 'green', 'symbol': 104, 'size': 10},
                                mode="lines",  name='read error')
            yrange = [0.0,1.0]

        data=go.Data([trace1])
        layout=go.Layout(title="Network flowing in 7 days", xaxis={'title':'Date time'}, yaxis={'title':'avg (hour) byte/s','range':yrange})
        figure=go.Figure(data=data,layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['graph'] = div

        return context

# TODO: Extract the same code of drawing charts for reuse
class ChartView6(TemplateView):
    template_name = "chart.html"

    def get_context_data(self, **kwargs):
        context = super(ChartView6, self).get_context_data(**kwargs)
        # get 7 days data from database
        now = datetime.now()
        time_interval = timedelta(days=10) #10 day
        before = now - time_interval
        df_min = selectdata(before, now)
        if (df_min is not None):
            # avg flowbyte for each hour
            df_hour = mean_hour_rate(df_min, True)

            df = flowratedf(df_hour)
            # plus 0.0001 for preventing zero division
            trace1 = go.Scatter(x=df.time, y=df['flowrate'], marker={'color': 'green', 'symbol': 104, 'size': 10},
                                mode="lines",  name='belle2grid2')
            yrange = [0.0, df['flowrate'].max()*1.3]
        else:
            x = [0]
            y = [0]
            race1 = go.Scatter(x=x, y=y, marker={'color': 'green', 'symbol': 104, 'size': 10},
                                mode="lines",  name='read error')
            yrange=[0.0,1.0]
        data=go.Data([trace1])
        layout=go.Layout(title="Network flowing in 10 days", xaxis={'title':'Date time'}, yaxis={'title':'avg (hour) byte/s','range':yrange})
        figure=go.Figure(data=data,layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['graph'] = div

        return context
