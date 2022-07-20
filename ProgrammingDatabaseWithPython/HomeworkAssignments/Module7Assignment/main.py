from flask import Flask, render_template, request
import dbcalls as mydb

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/view')
def view():

    # VIEW ENTIRE DATABASE
    view_result = mydb.view()
    return render_template("view.html", rows=view_result)

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/delete')
def delete():
    return render_template("delete.html")

@app.route('/updaterec', methods=['POST', 'GET'])
def updaterec():
    if request.method == 'POST':
        nm = request.form['nm']
        addr = request.form['add']
        city = request.form['city']
        id = request.form['id']

        # INSERT INTO TABLE
        insert_query = f"""
            INSERT INTO students(name, addr, city, id)
            VALUES ('{nm}', '{addr}', '{city}', '{id}')"""

        mydb.insert(nm, addr, city, id)
        msg = f"Record with {nm}, {addr}, {city}, {id} successfully added"
        return render_template("updateresult.html", message=msg)

@app.route('/seachrec', methods=['POST', 'GET'])
def searchrec():
    if request.method == 'POST':
        nm = request.form['nm']
        addr = request.form['add']
        city = request.form['city']

        # SEARCH FOR A RECORD
        search_result = mydb.searching(nm, addr, city)
        return render_template("searchresult.html", rows=search_result)

@app.route('/deleterec', methods=['POST', 'GET'])
def deleterec():
    if request.method == 'POST':
        nm = request.form['nm']

        # DELETE FROM TABLE
        mydb.delete(nm)
        msg = f"Record with name {nm} deleted"
        print(msg)
        return render_template("deleteresult.html", message=msg)

if __name__ == '__main__':
    app.run(debug=True)