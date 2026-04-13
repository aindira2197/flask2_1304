from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ismlar')
def ismlar():
    ismlar = ["Ali", "Vali", "Gul"]
    return render_template('ismlar.html', ismlar=ismlar)

if __name__ == "__main__":
    app.run(debug=True)
