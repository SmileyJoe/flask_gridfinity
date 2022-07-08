from flask import Flask,render_template, request, redirect
from tinydb import TinyDB, Query
import markdown
from markdown.extensions.toc import TocExtension
import db

app = Flask(__name__)

@app.route('/')
def index():
    tags = request.args.get('tags')
    Model = Query()
    tags_list = None
    models = None

    if not tags:
        # id there are not tags, we want an empty string and not None
        tags = ""
    else:
        # if there are tags, split them into a list
        tags_list = tags.split(',')

    if tags_list:
        models = db.models().search(Model.tags.all(tags_list))
    else:
        models = db.models().all()

    return render_template("index.html", models=models, tags=db.tags().all()[0]['tags'], tags_current=tags)

@app.route('/view')
def view():
    slug = request.args.get('model')
    dbModels = db.models()
    Model = Query()
    model = dbModels.search(Model.slug == slug)[0]
    return render_template("view.html", model=model, details=markdown.markdown(model["details"]))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


