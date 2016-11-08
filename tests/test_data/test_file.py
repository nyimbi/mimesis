# -*- coding: utf-8 -*-

from unittest import TestCase

import elizabeth._common as common
from elizabeth.elizabeth import File


class FileTestCase(TestCase):
    def setUp(self):
        self.file = File()

    def tearDown(self):
        del self.file

    def test_extension(self):
        text = self.file.extension(file_type='text')
        self.assertIn(text, common.EXTENSIONS['text'])

        source = self.file.extension(file_type='source')
        self.assertIn(source, common.EXTENSIONS['source'])
