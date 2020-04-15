# coding: utf-8

"""
    Timeline events

    This feature allows an app to create and configure custom events that can show up in the timelines of certain CRM object like contacts, companies, or deals. You'll find multiple use cases for this API in the sections below.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.timeline.configuration import Configuration


class TimelineEventTemplateUpdateRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'name': 'str',
        'header_template': 'str',
        'detail_template': 'str',
        'tokens': 'list[TimelineEventTemplateToken]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'header_template': 'headerTemplate',
        'detail_template': 'detailTemplate',
        'tokens': 'tokens'
    }

    def __init__(self, id=None, name=None, header_template=None, detail_template=None, tokens=None, local_vars_configuration=None):  # noqa: E501
        """TimelineEventTemplateUpdateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._header_template = None
        self._detail_template = None
        self._tokens = None
        self.discriminator = None

        self.id = id
        self.name = name
        if header_template is not None:
            self.header_template = header_template
        if detail_template is not None:
            self.detail_template = detail_template
        self.tokens = tokens

    @property
    def id(self):
        """Gets the id of this TimelineEventTemplateUpdateRequest.  # noqa: E501

        The template ID.  # noqa: E501

        :return: The id of this TimelineEventTemplateUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TimelineEventTemplateUpdateRequest.

        The template ID.  # noqa: E501

        :param id: The id of this TimelineEventTemplateUpdateRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this TimelineEventTemplateUpdateRequest.  # noqa: E501

        The template name.  # noqa: E501

        :return: The name of this TimelineEventTemplateUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TimelineEventTemplateUpdateRequest.

        The template name.  # noqa: E501

        :param name: The name of this TimelineEventTemplateUpdateRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def header_template(self):
        """Gets the header_template of this TimelineEventTemplateUpdateRequest.  # noqa: E501

        This uses Markdown syntax with Handlebars and event-specific data to render HTML on a timeline as a header.  # noqa: E501

        :return: The header_template of this TimelineEventTemplateUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._header_template

    @header_template.setter
    def header_template(self, header_template):
        """Sets the header_template of this TimelineEventTemplateUpdateRequest.

        This uses Markdown syntax with Handlebars and event-specific data to render HTML on a timeline as a header.  # noqa: E501

        :param header_template: The header_template of this TimelineEventTemplateUpdateRequest.  # noqa: E501
        :type: str
        """

        self._header_template = header_template

    @property
    def detail_template(self):
        """Gets the detail_template of this TimelineEventTemplateUpdateRequest.  # noqa: E501

        This uses Markdown syntax with Handlebars and event-specific data to render HTML on a timeline when you expand the details.  # noqa: E501

        :return: The detail_template of this TimelineEventTemplateUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._detail_template

    @detail_template.setter
    def detail_template(self, detail_template):
        """Sets the detail_template of this TimelineEventTemplateUpdateRequest.

        This uses Markdown syntax with Handlebars and event-specific data to render HTML on a timeline when you expand the details.  # noqa: E501

        :param detail_template: The detail_template of this TimelineEventTemplateUpdateRequest.  # noqa: E501
        :type: str
        """

        self._detail_template = detail_template

    @property
    def tokens(self):
        """Gets the tokens of this TimelineEventTemplateUpdateRequest.  # noqa: E501

        A collection of tokens that can be used as custom properties on the event and to create fully fledged CRM objects.  # noqa: E501

        :return: The tokens of this TimelineEventTemplateUpdateRequest.  # noqa: E501
        :rtype: list[TimelineEventTemplateToken]
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        """Sets the tokens of this TimelineEventTemplateUpdateRequest.

        A collection of tokens that can be used as custom properties on the event and to create fully fledged CRM objects.  # noqa: E501

        :param tokens: The tokens of this TimelineEventTemplateUpdateRequest.  # noqa: E501
        :type: list[TimelineEventTemplateToken]
        """
        if self.local_vars_configuration.client_side_validation and tokens is None:  # noqa: E501
            raise ValueError("Invalid value for `tokens`, must not be `None`")  # noqa: E501

        self._tokens = tokens

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TimelineEventTemplateUpdateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimelineEventTemplateUpdateRequest):
            return True

        return self.to_dict() != other.to_dict()