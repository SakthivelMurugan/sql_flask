from flask import Flask,render_template,request
import sqlite3 as sql

app=Flask("__name__")

@app.route("/")
def fun():
    conn=sql.connect("student.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()

    cur.execute("select * from stu")
    data=cur.fetchall()

    return render_template("index.html",data=data)

@app.route("/one",methods=["POST","GET"])
def fun1():
    a=request.form.get("id")
    conn=sql.connect("student.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()

    cur.execute("select * from stu where id=?",(a,))
    data=cur.fetchall()

    return render_template("one.html",data=data)


if __name__=="__main__":
    app.run(debug=True)
