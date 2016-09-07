#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import flaskr
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp() # mkstemp: returns a low-level file handle and a random file name
        flaskr.app.config['TESTING'] = True # disable the error catching during request handling
        self.app = flaskr.app.test_client()
        with flaskr.app.app_context():
            flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()