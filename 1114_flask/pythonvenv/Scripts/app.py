from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/home')
def sub():
    return 'hello, my home'


if __name__ == '__main__':
# 현재 작성된 파이썬 파일이 메인으로 실행되는 파일이면, app.run을 수행해라.
    app.run(debug=True)
# app.run() 괄호안에 debug=True 라고 명시하면 해당 파일의 코드가 수정될때마다, flask가 변경된것을 인식하고 다시 시작한다.
