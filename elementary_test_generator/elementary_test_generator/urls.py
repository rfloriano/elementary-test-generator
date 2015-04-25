#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of elementary-test-generator.
# https://github.com/rflorianobr/elementary-test-generator

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Rafael Floriano da Silva <rflorianobr@gmail.com>

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'elementary_test_generator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
