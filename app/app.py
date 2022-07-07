from flask import Flask,render_template, request, redirect
from tinydb import TinyDB, Query
import markdown
from markdown.extensions.toc import TocExtension
import db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", models=db.models().all())

@app.route('/view')
def view():
    slug = request.args.get('model')
    dbModels = db.models()
    Model = Query()
    model = dbModels.search(Model.slug == slug)[0]
    return render_template("view.html", model=model, details=markdown.markdown(model["details"]))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


