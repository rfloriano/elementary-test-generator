#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of elementary-test-generator.
# https://github.com/rflorianobr/elementary-test-generator

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Rafael Floriano da Silva <rflorianobr@gmail.com>

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "elementary_test_generator.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
