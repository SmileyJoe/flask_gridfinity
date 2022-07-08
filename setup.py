from pathlib import Path
from tinydb import Query
import app.db as db
import yaml

DIR_MODELS = 'app/static/files'
FILE_META = 'meta.yml'
FILE_DETAILS = 'details.md'

db.setup()

dbModels = db.models()
dbTags = db.tags()
Model = Query()

tags = dbTags.all()
tags_new = []

# cycle all the meta files that are found
for meta_path in Path(DIR_MODELS).rglob(FILE_META):
    # get the parent directory name as the slug
    slug = str(meta_path.parents[0]).replace(str(meta_path.parents[1]), "").strip("/").strip("\\")
    # get the model by the slug from the db
    model = dbModels.search(Model.slug == slug)
    # read in and parse the meta data
    meta = yaml.load(meta_path.read_text(), Loader=yaml.FullLoader)
    # if the model is not in the db, or it is an older version
    if (not model) or (model[0]['version'] < meta['version']):
        # get all the tags, lower case them, and replace all spaces with underscores
        tags_meta = [tag.lower().replace(" ", "_") for tag in meta['tags']]
        for tag in tags_meta:
            # only add unique tags to the db, so make sure the tag is not already saved
            # and hasn't been set to be saved
            if (tag not in tags) and (tag not in tags_new):
                tags_new.append(tag)
        meta['tags'] = tags_meta
        # read in the details file and add it to the meta
        meta['details'] = meta_path.parent.joinpath(FILE_DETAILS).read_text()
        # add the slug
        meta['slug'] = slug
        # add the directory path
        meta['path'] = str(meta_path.parent)
        # read in all the stl files in the directory
        models=[]
        for model in meta_path.parent.glob('*.stl'):
            # add the details to the list
            models.append({
                # the path minus "app"
                "path": str(model)[3:],
                # the name of the file without the extension
                "name": model.stem
            })
        # add the models
        meta['models'] = models
        # insert or update the model in the db
        dbModels.upsert(meta, Model.slug == slug)

# if there are new tags, save the tags
if tags_new:
    dbTags.insert({'tags':tags_new})