# Flask class 임포트하기
from flask import Flask
# 참고로, Flask의 첫번째 인자는 이 어플리케이션의 이름이다.

# 인스턴스 생성하기
# 단일모듈이기에 __name__을 사용한다
# (어플리케이션으로 시작되는지, 모듈로 임포트되는지에 따라 달라진다)
app = Flask(__name__)

# route() 데코레이터.
# 어떤 URL이 작성한 함수를 실행시키는지 알려준다
@app.route('/')
# 함수는 접속시 나타낼 메시지를 리턴한다
def hello_world():
    return 'Hello World!'

# 현재 실행한 서버가 동작되는 유일한 서버라는 것을 보장한다는 것을 의미
if __name__=='__main__':

    # 어플리케이션을 로컬서버로 실행
    # app.run()

    # 디버그 모드를 켜는 방법 두 가지
    # 1)
    # app.debug = True
    # 2)
    # app.run(debug=True)

    app.run(debug=True)