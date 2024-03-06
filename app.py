from flask import Flask, render_template, request
import csv

from static.cv import my_cv


app = Flask(__name__, template_folder='templates', static_url_path='/static')


@app.route("/")
def start():
    return render_template('home.html')


@app.route("/home.html")
def home():
    return render_template('home.html')


@app.route("/cv.html")
def cv():
    return render_template("cv.html", my_cv=my_cv)


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/contact.html", methods=['POST'])
def save_comment():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        fieldnames = ['name', 'email', 'message']

        with open('files/messages.csv', 'a', newline='') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            if inFile.tell() == 0:
                writer.writeheader()

            writer.writerow({'name': name, 'email': email, 'message': message})

        return render_template('thanks.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
