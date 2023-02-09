from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return render_template('home.html')

def about():
    return render_template('about.html')

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


app.add_url_rule('/', 'hello', hello_world)
app.add_url_rule('/about','about',about)

if __name__ == '__main__':
# run() method of Flask class runs the application
# on the local development server.
    app.run()