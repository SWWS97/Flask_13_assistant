from flask import Flask, jsonify, render_template, session
from routes.user import user_bp
from routes.admin import admin_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)
app.secret_key = "ssd232929d9sds9293sd9" # 직접 작성하지는 않고 난수 발생시키는 기능을 이용해서 만듬

@app.route("/") #사용자로부터 받아온 URL에 해당하는 함수를 매칭해주기 위해서 사용됩니다.
def index():
    return render_template("index.html", name="지수")

@app.route('/login')
def login():
    session['username'] = 'a1818291919' # 키와 벨류 => 딕트 / username 키가 있으면 값이 바뀌는 거구요, 없으면 키값으 생성하고 거기다가 값을 넣는거
    return '로그인 완료 : 세션에 저장됨'

@app.route('/status')
def status():
    username = session.get('username') #임의 값을 넣습니다.
    return f"현재 사용자 : {username}"

@app.route('/logout')
def logout():
    session.pop('username', None) # session.pop을 실행하면 key이 session.pop에 없으면 에러 발생
    return "로그아웃 완료 : 세션에서 제거됨"

@app.route('/check')
def check():
    #스크패핑 -> 후드가 있는지 없는지 확인했습니다.
    if 'username' in session:
        return f"{session['username']}님이 로그인 중입니다."
    return '로그인 해주세요'

if __name__ == '__main__':
    app.run(debug=True)
