from flask import Flask, render_template # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fotos1')
def fotos1():
    return render_template('fotos1.html')


@app.route('/fotos3')
def fotos3():
    return render_template('fotos3.html')

@app.route('/fotos4')
def fotos4():
    return render_template('fotos4.html')

@app.route('/fotos5')
def fotos5():
    return render_template('fotos5.html')

if __name__ == '__main__':
    app.run(debug=True)
