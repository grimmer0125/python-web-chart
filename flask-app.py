from flask import Flask
import plotly.offline as opy
import plotly.graph_objs as go

app = Flask(__name__)

@app.route("/") # ~ app.add_url_rule('/', view_func=hello)
def index():
    return "index!"

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('flask-hello.html', name=name)

@app.route('/chart/')
def chart():
    x = [-2,0,4,6,7]
    y = [q**2-q+3 for q in x]
    trace1 = go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': "10"},
                        mode="lines",  name='1st Trace')

    data=go.Data([trace1])
    layout=go.Layout(title="Meine Daten", xaxis={'title':'x1'}, yaxis={'title':'x2'})
    figure=go.Figure(data=data,layout=layout)
    graph = opy.plot(figure, auto_open=False, output_type='div')

    return render_template('flask-chart.html', graph=graph)

# $ export FLASK_ENV=development (live debug server, <-not work)
# $ FLASK_APP=hello.py flask run or the below
if __name__ == "__main__":
    app.run(debug = True) # True works
