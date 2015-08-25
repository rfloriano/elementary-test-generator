#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of elementary-test-generator.
# https://github.com/rflorianobr/elementary-test-generator

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Rafael Floriano da Silva <rflorianobr@gmail.com>

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/wizard/', permanent=False), name='index'),
    url(r'^wizard/$', 'general.views.wizard', name='wizard'),
    url(r'^template/(?P<id>[0-9]+)/$', 'general.views.template', name='template'),
    url(r'^questions/template/(?P<template_id>[0-9]+)/$', 'general.views.questions', name='questions'),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
