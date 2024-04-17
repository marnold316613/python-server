from flask import Flask, render_template, url_for

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

@app.route('/<username>')
def hello_world2(username=None):
  return render_template('index.html',name=username)

if __name__=="__main__":
  app.run()
