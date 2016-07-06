# -*- coding: utf-8 -*-

from __future__ import absolute_import

from commons.logs import get_logger
from ..base import ExtendedApiResource
from .. import decorators as decorate

logger = get_logger(__name__)


@decorate.custom_response
def fedapp_response(defined_content=None, code=None, headers={}, errors={}):
    """
    Define my response that will be used
    from any custom endpoint inside any file
    """
    if len(errors) > 0:
        defined_content = errors
    return ExtendedApiResource.flask_response(
        defined_content, status=code, headers=headers)
