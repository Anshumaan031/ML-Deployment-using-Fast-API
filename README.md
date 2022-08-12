# Fast-API

![image](https://user-images.githubusercontent.com/67821036/184329245-59db7ba0-9794-4f2d-a7c9-38e1dc6670b6.png)

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

The key features are:

Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.

Fast to code: Increase the speed to develop features by about 200% to 300%. 

Fewer bugs: Reduce about 40% of human (developer) induced errors. 

Intuitive: Great editor support. Completion everywhere. Less time debugging.

Easy: Designed to be easy to use and learn. Less time reading docs.

Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.

Robust: Get production-ready code. With automatic interactive documentation.

Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

Libraries needed for deployemtn model in fast API:

```
pip install fastapi
pip install uvicorn
```

## configuration files for heroku

### procfile

example:
```
web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app
```

### requirements.txt

What is the requirements txt file?
In Python requirement. txt file is a type of file that usually stores information about all the libraries, modules, and packages in itself that are used while developing a particular project.

```
numpy
scipy
scikit-learn
matplotlib
pandas
fastapi
uvicorn
gunicorn==19.9.0
uvloop
httptools
```

These libraries will be used for deploymeny in heroku

<img width="1272" alt="Capture" src="https://user-images.githubusercontent.com/67821036/184329297-d8014672-0c6f-497b-8ec4-787de1a69e91.PNG">

## Documentations

[Fast-API](https://fastapi.tiangolo.com/) 

[Heroku](https://devcenter.heroku.com/categories/reference)

[sklearn](https://devdocs.io/scikit_learn/) 

[Flask](https://flask.palletsprojects.com/en/2.1.x/) 

[Pydantic](https://pydantic-docs.helpmanual.io/) 



## Author 

- [@Anshumaan031 - <anshuphukan031@gmail.com>](https://github.com/Anshumaan031)
