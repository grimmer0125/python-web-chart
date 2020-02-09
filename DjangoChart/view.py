# added by grimmer, hello world example
from django.http import HttpResponse
from django.views.generic import TemplateView

from datetime import datetime
from django.shortcuts import render

import plotly.offline as opy
import plotly.graph_objs as go

# def hello(request):
#     return HttpResponse("Hello world ! ")

# template render example:
# https://github.com/twtrubiks/django-tutorial/blob/master/musics/views.py
#     return render(request, 'hello_django.html', {
#         'data': "Hello Django ",
#         'musics': musics,
#     })


# deprecated
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
        context = super(ChartView, self).get_context_data(**kwargs)
        if "time1" in self.request.GET:
            print("time1:" + self.request.GET["time1"])
        if "time2" in self.request.GET:
            print("time2:" + self.request.GET["time2"])
        x = [-2, 0, 4, 6, 7]
        y = [q**2 - q + 3 for q in x]
        trace1 = go.Scatter(x=x,
                            y=y,
                            marker={
                                'color': 'red',
                                'symbol': 104,
                                'size': "10"
                            },
                            mode="lines",
                            name='1st Trace')

        data = go.Data([trace1])
        layout = go.Layout(title="Meine Daten",
                           xaxis={'title': 'x1'},
                           yaxis={'title': 'x2'})
        figure = go.Figure(data=data, layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['graph'] = div

        return context


# deprecated
# TODO: Extract the same code of drawing charts for reuse
class ChartView2(TemplateView):
    template_name = "chart.html"

    def get_context_data(self, **kwargs):
        context = super(ChartView2, self).get_context_data(**kwargs)

        x = [-2, 0, 4, 6, 7]
        y = [q**2 - q + 3 for q in x]
        trace1 = go.Scatter(x=x,
                            y=y,
                            marker={
                                'color': 'green',
                                'symbol': 104,
                                'size': "10"
                            },
                            mode="lines",
                            name='1st Trace')

        data = go.Data([trace1])
        layout = go.Layout(title="Meine Daten",
                           xaxis={'title': 'x1'},
                           yaxis={'title': 'x2'})
        figure = go.Figure(data=data, layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['graph'] = div

        return context
