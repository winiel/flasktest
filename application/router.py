from flask import Flask, render_template, request

from application.controller.push_mail import PushMail


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
# def hello_world():
#     return 'Hello World!'



@app.route('/test')
def test():
    # dbUtil = DbUtil();
    # dbUtil = DbUtil();
    #
    # sql = "SELECT * FROM abitree.tbl_test";
    # res = dbUtil.exeQuery(sql, None );
    # print(res);
    return "hello";




@app.route('/mail', methods=['post'])
def PostMail():

    pushMail = PushMail();
    pushMail.push(request);

    return "post_mail";


if __name__ == '__main__':
    app.run()
