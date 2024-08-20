from flask import Flask,render_template
app = Flask(__name__)

#通过访问路径匹配对应函数
@app.route('/')
def welcome():
    return render_template("overview.html")

#渲染html模板

@app.route('/chart.html')
def charts():
    return render_template("chart.html")

@app.route('/empty.html')
def index3():

    return render_template("empty.html")

@app.route('/table.html')
def index5():

    return render_template("table.html")

@app.route('/overview.html')
def welcome1():
    return welcome()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)






#向页面传递变量
# @app.route('/index2')
# def index2():
#     time = datetime.date.today() #一般变量用{{ }}
#     name = ["z","j","w"] #列表用{% %}
#     task = {"任务":"clean","time":"3h"}
#     return render_template("test.html", var = time, list = name, task = task)  #html前端变量 = flask后端变量
