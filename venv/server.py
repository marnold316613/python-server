from flask import Flask, render_template

app= Flask(__name__)
app.debug=True

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/hello')
def hello_world():
  return 'Hello World!'

@app.route('/favicon.ico')
def favicon():
  pass


if __name__=="__main__":
  app.run()
