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

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .operations.lr_os_operations import LROsOperations
from .operations.lro_retrys_operations import LRORetrysOperations
from .operations.lrosa_ds_operations import LROSADsOperations
from .operations.lr_os_custom_header_operations import LROsCustomHeaderOperations
from . import models


class AutoRestLongRunningOperationTestServiceConfiguration(AzureConfiguration):
    """Configuration for AutoRestLongRunningOperationTestService

    :param credentials: Gets Azure subscription credentials.
    :type credentials: credentials
    :param accept_language: Gets or sets the preferred language for the
     response.
    :type accept_language: str or None
    :param long_running_operation_retry_timeout: Gets or sets the retry
     timeout in seconds for Long Running Operations. Default value is 30.
    :type long_running_operation_retry_timeout: int or None
    :param generate_client_request_id: When set to true a unique
     x-ms-client-request-id value is generated and included in each request.
     Default is true.
    :type generate_client_request_id: bool or None
    :param str base_url: Service URL
    :param str filepath: Existing config
    """

    def __init__(
            self, credentials, accept_language='en-US', long_running_operation_retry_timeout=30, generate_client_request_id=True, base_url=None, filepath=None):

        if credentials is None:
            raise ValueError('credentials must not be None.')
        if not base_url:
            base_url = 'http://localhost'

        super(AutoRestLongRunningOperationTestServiceConfiguration, self).__init__(base_url, filepath)

        self.user_agent = 'auto_rest_long_running_operation_test_service/1.0.0'

        self.credentials = credentials
        self.accept_language = accept_language
        self.long_running_operation_retry_timeout = long_running_operation_retry_timeout
        self.generate_client_request_id = generate_client_request_id


class AutoRestLongRunningOperationTestService(object):
    """Long-running Operation for AutoRest

    :param config: Configuration for client.
    :type config: AutoRestLongRunningOperationTestServiceConfiguration
    """

    def __init__(self, config):

        self._client = ServiceClient(config.credentials, config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer()
        self._deserialize = Deserializer(client_models)

        self.config = config
        self.lr_os = LROsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.lro_retrys = LRORetrysOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.lrosa_ds = LROSADsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.lr_os_custom_header = LROsCustomHeaderOperations(
            self._client, self.config, self._serialize, self._deserialize)
