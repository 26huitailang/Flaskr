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
        
    def test_empty_db(self):
        # By using self.app.get we can send an HTTP GET request to the application with the given path. 
        rv = self.app.get('/')
        assert b'No entries here so far' in rv.data
        
    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password),
            follow_redirects=True)
            
    def logout(self):
        return self.app.get('/logout', follow_redirects=True)
        
    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login('adminxxx', 'default')
        assert 'Invalid username' in rv.data
        rv = self.login('admin', 'defaultxxx')
        assert 'Invalid password' in rv.data

    """Here we check that HTML is allowed in the text but not in the title, which is the intended behavior.
    """
    def test_messages(self):
        self.login('admin', 'default')
        rv = self.app.post('/add', data=dict(
            title='<Hello>',
            text='<strong>HTML</strong> allowed here'
            ), follow_redirects=True)
        assert 'No entries here so far' not in rv.data
        assert '&lt;Hello&gt;' in rv.data
        assert '<strong>HTML</strong> allowed here' in rv.data
        
if __name__ == '__main__':
    unittest.main()