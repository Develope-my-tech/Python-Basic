from flask import Flask

app = Flask(__name__)

@app.route('/echo/<thing>')
def echo(thing):
    return "Say hello to my little friend: %s" % thing

app.run(port=9999, debug=True)


# url 입력 : http://127.0.0.1:9999/echo/Gamera
# 출력 : Say hello to my little friend: Gamera!
