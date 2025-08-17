from flask import Flask, jsonify, render_template, request, make_response
from routes.user import user_bp
from routes.admin import admin_bp

app = Flask(__name__)

@app.route("/") #사용자로부터 받아온 URL에 해당하는 함수를 매칭해주기 위해서 사용됩니다.
def index():
    return render_template("index.html", name="13기_조교")

@app.route('/set')
def set_cookie():
    #1. "쿠키 설정 완료"라는 내용이 담길 응답(편집)을 먼저 만들겁니다.
    resp = make_response("쿠키 설정 완료")

    #2. 그 응답(편집)에 'username'이라는 이름의 쿠키(도장 카드)를 붙여서 보냅니다.
    resp.set_cookie('username', 'kim')
    return resp

@app.route('/get')
def get_cookie():
    #사용자의 요청(편지)에 붙어있는 쿠키(도장 카드)를 확인합니다.
    username = request.cookies.get('username')
    return f"지갑에서 꺼낸 쿠키: {username}"

if __name__ == '__main__':
    app.run(debug=True)
