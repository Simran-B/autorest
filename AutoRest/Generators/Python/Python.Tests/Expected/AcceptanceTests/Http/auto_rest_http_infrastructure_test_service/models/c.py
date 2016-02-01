# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class C(Model):
    """C

    :param str http_code
    """

    _required = []

    _attribute_map = {
        'http_code': {'key': 'httpCode', 'type': 'str'},
    }

    def __init__(self, *args, **kwargs):
        self.http_code = None

        super(C, self).__init__(*args, **kwargs)
