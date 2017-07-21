Django web service for generating rapid-prototype static pages
--------------------------------------------------------------
easily add pages and generate interactive prototype for iterative development of web application

Usage:
---

1. put prototype html pages in /pages

2. edit templates/base.html for navigation


3. run the server to use the prototype @ localhost:8000

* python prototypes.py runserver

* or

* gunicorn prototypes

4. (optional) generate static site for distribution:

* run: python prototypes.py build

* static site will be saved in _build directory

A working instance of this web service can be found here:

https://prototype-gen.herokuapp.com/

p.s. It will take a few seconds to load when it's visited after a long period of idle. Heroku host goes into hiberanation when not visited.





Dependencies:
---
  Django==1.11.3

  gunicorn==19.7.1

  whitenoise==3.2
