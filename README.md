# Gridfinity Viewer

[Zack Freedman](https://www.youtube.com/channel/UCUW49KGPezggFi0PGyDvcvg) came up with a standard for a 3d printable organisation system called **Gridfinity**, which was released as open source.

The original video can be found [here](https://www.youtube.com/watch?v=ra_9zU-mnl8) with an update on the community uptake [here](https://www.youtube.com/watch?v=Bd4NnHvTRAY).

This is a simple self hosted flask website with the aim to easily categorise and find components.

## Adding new models

All models are stored in their own directory inside `app/static/files`, with the following format:

- `meta.yml`: All the meta data for the model, this needs to follow the schema specified in `meta-schema.yml`
- `details.md`: Markdown file with any details, tips etc on the models
- `*.stl`: Any number of stl files for a specified model

While a directory can have multiple models, it can only have 1 meta and details file, this is meant for different versions (eg, multiple sizes) of the same model, and not multiple solutions to the same problem, as those would have different meta data and different descriptions

## Updating models

If a new stl file is added to a directory, or the meta data, or the details markdown is updated, the `version` number in the meta data needs to be updated, and the container needs to be rebuilt.

## Running the app

Run the docker file: `docker-compose up -d`
Rebuild the container after an update: `docker-compose up -d --build web`

## How it works

When the container is run, the `setup.py` file is run, this runs through the `app/static/files` directory and adds the meta, details, and models to the [TinyDb](https://tinydb.readthedocs.io/en/latest/).

Everything is then read from the db, this allows searching etc