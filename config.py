# -*- coding: utf-8 -*-
"""
    python_images_server.config
    ~~~~~~~~~~~~~~

    Server for react-images-uploader.

    :copyright: (c) 2017 by aleksei0807.
    :license: MIT, see LICENSE.md for more details.
"""

# pylint: disable=too-few-public-methods
class Route(object):
    """class Route"""
    SERVEPATH = ''
    SAVEPATH = ''
    FULLPATH = ''
    FILESERVE = ''
    MULTIPLE = False
    RENAME = True

class Multiple(Route):
    """route for multiple files"""
    SERVEPATH = '/multiple'
    SAVEPATH = 'static/multipleFiles'
    FULLPATH = '//localhost:5000/multiple'
    FILESERVE = 'multipleFiles'
    MULTIPLE = True
    RENAME = True

class NotMultiple(Route):
    """route for not multiple files"""
    SERVEPATH = '/notmultiple'
    SAVEPATH = 'static/files'
    FULLPATH = '//localhost:5000/notmultiple'
    FILESERVE = 'files'
    MULTIPLE = False
    RENAME = True

routes = [Multiple, NotMultiple]
