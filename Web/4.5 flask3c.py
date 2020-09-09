from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/echo/')
def echo():
    kwargs = {}
    kwargs['thing'] = request.args.get('thing')
    kwargs['place'] = request.args.get('place')
    return render_template('flask3.html', **kwargs)

app.run(port=9999, debug=True)

# url : http://127.0.0.1:9999/echo/?thing=Gorgo&place=Wilmerding
# 출력 : Say hello to my little friend: Gorgo Alas, it just destroyed Wilmerding