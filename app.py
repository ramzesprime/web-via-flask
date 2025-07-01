from flask import Flask, render_template, request, redirect, url_for, session, make_response, session
from SQL_handler import SQL_handler

app = Flask(__name__)
app.secret_key = "porno"

sql = SQL_handler()
sql.table_create()

def check_form(email, password) -> bool:
    return bool(email and password)

@app.route('/')
def index():
    login = session.get('username',None)
    return render_template('home.html',user = login)

@app.route('/FAQ')
def FAQ():
    print(session.get('username',None))
    login = session.get('username',None)
    return render_template('FAQ.html',user = login)

@app.route('/reg', methods=["GET", "POST"])
def reg():
        login = session.get('username',None)
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")
            sql.commit_start()
            if check_form(email,password) is True:
                print("Yeah there is data in form")
                if sql.check_duplicate(email):
                    error902 = True
                    return render_template('reg.html',error902=error902,user = login)
                sql.add_new_values(email,password)
            else:
                error901 = True
                return render_template('reg.html',error901=error901,user = login)
        return render_template('reg.html',user = login)

@app.route('/log', methods=["GET", "POST"])
def log():
    login = session.get('username',None)
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        sql.commit_start()
        if check_form(email,password) is True:
            if sql.check_login(email,password):
                succes = True
                res = make_response(render_template('log.html',succes=succes,user = login))
                session['username'] = email
                return res
        else:
            error901 = True
            return render_template('log.html',error901=error901,user = login)
    user = session.get('user', '')
    return render_template('log.html',user = login)

@app.route('/unlog', methods=["GET", "POST"])
def unlog():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/image/<img_name>')
def image_detail(img_name):
    img_new_name = (img_name)
    sql.commit_start()
    sql.cur.execute(f"""SELECT Description FROM Products WHERE image LIKE ?""",(img_new_name,))
    q = str(sql.cur.fetchone())
    description = q[2:-3:1]
    sql.cur.execute(f"""SELECT Name FROM Products WHERE image LIKE ?""",(img_new_name,))
    q2 = str(sql.cur.fetchone())
    name_pr = q2[2:-3:1]
    print (f"!!!!! for {img_name} we got a pair {description} and {name_pr}!!!!!")
    return render_template("sn.html",name=img_name,data=description,name_pr=name_pr)

if __name__ == "__main__":
    app.run(debug=True)