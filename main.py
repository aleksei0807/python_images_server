# -*- coding: utf-8 -*-
"""
    python_images_server.main
    ~~~~~~~~~~~~~~

    Server for react-images-uploader.

    :copyright: (c) 2017 by aleksei0807.
    :license: MIT, see LICENSE.md for more details.
"""
from functools import partial
from flask import Flask
from flask_cors import CORS
import config

app = Flask(__name__, static_url_path='')

CORS(app)

def serve_images(myroute, path):
    """Serve images handler"""
    return app.send_static_file("%s/%s" % (myroute.FILESERVE, path))

for i in range(len(config.routes)):
    myserve = partial(serve_images, config.routes[i])
    app.view_functions['myserve' + `i`] = myserve
    app.add_url_rule(config.routes[i].SERVEPATH + '/<path:path>', 'myserve' + `i`)

if __name__ == "__main__":
    app.run()
