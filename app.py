from flask import Flask, render_template

from util.db_util import DbUtil

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
# def hello_world():
#     return 'Hello World!'



@app.route('/test')
def test():
    dbUtil = DbUtil();

    sql = "SELECT * FROM abitree.tbl_test";
    res = dbUtil.exeQuery(sql, None );
    print(res);
    return "hello";


if __name__ == '__main__':
    app.run()
