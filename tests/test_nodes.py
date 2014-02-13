# coding: utf-8
from __future__ import unicode_literals

import pytest
from django import template

from forme import nodes
from forme.parser import FormeParser


def test_node_factory():
    for tag in FormeParser.valid_tags:
        assert tag in nodes.node_classes
        assert isinstance(nodes.node_factory(tag), template.Node)

    with pytest.raises(KeyError):
        nodes.node_factory('42_fish')