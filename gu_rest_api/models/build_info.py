# coding: utf-8

"""
    Golem unlimited low level hub API

    API description in Markdown.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BuildInfo(object):
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
        'ts': 'datetime',
        'target': 'str',
        'commit_hash': 'str'
    }

    attribute_map = {
        'ts': 'ts',
        'target': 'target',
        'commit_hash': 'commitHash'
    }

    def __init__(self, ts=None, target='x86_64-unknown-linux-gnu', commit_hash=None):  # noqa: E501
        """BuildInfo - a model defined in OpenAPI"""  # noqa: E501

        self._ts = None
        self._target = None
        self._commit_hash = None
        self.discriminator = None

        if ts is not None:
            self.ts = ts
        if target is not None:
            self.target = target
        if commit_hash is not None:
            self.commit_hash = commit_hash

    @property
    def ts(self):
        """Gets the ts of this BuildInfo.  # noqa: E501


        :return: The ts of this BuildInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """Sets the ts of this BuildInfo.


        :param ts: The ts of this BuildInfo.  # noqa: E501
        :type: datetime
        """

        self._ts = ts

    @property
    def target(self):
        """Gets the target of this BuildInfo.  # noqa: E501

        target platform triple  # noqa: E501

        :return: The target of this BuildInfo.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this BuildInfo.

        target platform triple  # noqa: E501

        :param target: The target of this BuildInfo.  # noqa: E501
        :type: str
        """

        self._target = target

    @property
    def commit_hash(self):
        """Gets the commit_hash of this BuildInfo.  # noqa: E501

        git commit id  # noqa: E501

        :return: The commit_hash of this BuildInfo.  # noqa: E501
        :rtype: str
        """
        return self._commit_hash

    @commit_hash.setter
    def commit_hash(self, commit_hash):
        """Sets the commit_hash of this BuildInfo.

        git commit id  # noqa: E501

        :param commit_hash: The commit_hash of this BuildInfo.  # noqa: E501
        :type: str
        """

        self._commit_hash = commit_hash

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
        if not isinstance(other, BuildInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
