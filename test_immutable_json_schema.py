# -*- coding: utf-8 -*-

import os

from unittest import TestCase
from json_schema_generator import Validator
from six.moves.urllib.request import urlopen

SERVICE_URL = "https://www.airq.org.tw/Home/realtime10m"


class TestHomogate(TestCase):

    def test_immutable_should_match_json_schema(self):
        json_data = urlopen(SERVICE_URL).read()
        json_schema_file_path = os.path.join("json_schemas", "immutable.json_schema")
        validator = Validator.from_path(json_schema_file_path)
        is_valid = validator.assert_json(json_data)

        self.assertTrue(is_valid, validator.error_message)

