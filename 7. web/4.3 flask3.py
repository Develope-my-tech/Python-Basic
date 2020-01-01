# url 확장
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/echo/<thing>/<place>')
def echo(thing, place):
    return render_template('flask3.html', thing=thing, place=place)

app.run(port=9999, debug=True)

# render_template는 templates 폴더를 만들어야함.

# url : http://127.0.0.1:9999/echo/Gamera/McKessports
# 출력 : Say hello to my little friend: Gamera Alas, it just destroyed McKessports