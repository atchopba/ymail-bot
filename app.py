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
import config as cfg

web = Browser()

web.go_to(cfg.YMAIL_URL)
web.type(cfg.YMAIL_USER, id="login-username")
web.press(web.Key.ENTER) #

time.sleep(5)

web.type(cfg.YMAIL_PWD, id="login-passwd", classname="password")
web.press(web.Key.ENTER) #
