#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "Albin TCHOPBA"
# __copyright__ = "Copyright 2020 Albin TCHOPBA and contributors"
# __credits__ = ["Albin TCHOPBA and contributors"]
# __license__ = "GPL"
# __version__ = "3"
# __maintainer__ = "Albin TCHOPBA"
# __email__ = "Albin TCHOPBA <atchopba @ gmail dot com"
# __status__ = "Production"

from webbot import Browser

import time
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

web = Browser()

web.go_to(environ.get("YMAIL_URL"))
web.type(environ.get("YMAIL_USER"), id="login-username")
web.press(web.Key.ENTER) #

time.sleep(5)

web.type(environ.get("YMAIL_PWD"), id="login-passwd", classname="password")
web.press(web.Key.ENTER) #
