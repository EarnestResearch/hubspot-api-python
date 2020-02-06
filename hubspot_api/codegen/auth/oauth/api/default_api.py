# coding: utf-8

"""
    OAuthService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot_api.codegen.auth.oauth.api_client import ApiClient
from hubspot_api.codegen.auth.oauth.exceptions import (
    ApiTypeError,
    ApiValueError
)


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive_refresh_token(self, token, **kwargs):  # noqa: E501
        """archive_refresh_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_refresh_token(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str token: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Error
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.archive_refresh_token_with_http_info(token, **kwargs)  # noqa: E501

    def archive_refresh_token_with_http_info(self, token, **kwargs):  # noqa: E501
        """archive_refresh_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_refresh_token_with_http_info(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str token: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Error, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method archive_refresh_token" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'token' is set
        if self.api_client.client_side_validation and ('token' not in local_var_params or  # noqa: E501
                                                        local_var_params['token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `token` when calling `archive_refresh_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'token' in local_var_params:
            path_params['token'] = local_var_params['token']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/refresh-tokens/{token}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Error',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_token(self, **kwargs):  # noqa: E501
        """create_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_token(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str grant_type:
        :param str code:
        :param str redirect_uri:
        :param str client_id:
        :param str client_secret:
        :param str refresh_token:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TokenResponseIF
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_token_with_http_info(**kwargs)  # noqa: E501

    def create_token_with_http_info(self, **kwargs):  # noqa: E501
        """create_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_token_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str grant_type:
        :param str code:
        :param str redirect_uri:
        :param str client_id:
        :param str client_secret:
        :param str refresh_token:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TokenResponseIF, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['grant_type', 'code', 'redirect_uri', 'client_id', 'client_secret', 'refresh_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_token" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'grant_type' in local_var_params:
            form_params.append(('grant_type', local_var_params['grant_type']))  # noqa: E501
        if 'code' in local_var_params:
            form_params.append(('code', local_var_params['code']))  # noqa: E501
        if 'redirect_uri' in local_var_params:
            form_params.append(('redirect_uri', local_var_params['redirect_uri']))  # noqa: E501
        if 'client_id' in local_var_params:
            form_params.append(('client_id', local_var_params['client_id']))  # noqa: E501
        if 'client_secret' in local_var_params:
            form_params.append(('client_secret', local_var_params['client_secret']))  # noqa: E501
        if 'refresh_token' in local_var_params:
            form_params.append(('refresh_token', local_var_params['refresh_token']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenResponseIF',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_access_token(self, token, **kwargs):  # noqa: E501
        """get_access_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_access_token(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str token: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AccessTokenInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_access_token_with_http_info(token, **kwargs)  # noqa: E501

    def get_access_token_with_http_info(self, token, **kwargs):  # noqa: E501
        """get_access_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_access_token_with_http_info(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str token: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AccessTokenInfoResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_access_token" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'token' is set
        if self.api_client.client_side_validation and ('token' not in local_var_params or  # noqa: E501
                                                        local_var_params['token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `token` when calling `get_access_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'token' in local_var_params:
            path_params['token'] = local_var_params['token']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/access-tokens/{token}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessTokenInfoResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_refresh_token(self, token, **kwargs):  # noqa: E501
        """get_refresh_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_refresh_token(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str token: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: RefreshTokenInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_refresh_token_with_http_info(token, **kwargs)  # noqa: E501

    def get_refresh_token_with_http_info(self, token, **kwargs):  # noqa: E501
        """get_refresh_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_refresh_token_with_http_info(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str token: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(RefreshTokenInfoResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_refresh_token" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'token' is set
        if self.api_client.client_side_validation and ('token' not in local_var_params or  # noqa: E501
                                                        local_var_params['token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `token` when calling `get_refresh_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'token' in local_var_params:
            path_params['token'] = local_var_params['token']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/refresh-tokens/{token}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RefreshTokenInfoResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
