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


class Command(object):
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
        '_exec': 'ExecCommand',
        'open': 'object',
        'wait': 'object',
        'close': 'object',
        'start': 'StartCommand',
        'stop': 'StopCommand',
        'add_tags': 'list[str]',
        'del_tags': 'list[str]',
        'download_file': 'DownloadFileCommand',
        'upload_file': 'UploadFileCommand'
    }

    attribute_map = {
        '_exec': 'exec',
        'open': 'open',
        'wait': 'wait',
        'close': 'close',
        'start': 'start',
        'stop': 'stop',
        'add_tags': 'addTags',
        'del_tags': 'delTags',
        'download_file': 'downloadFile',
        'upload_file': 'uploadFile'
    }

    def __init__(self, _exec=None, open=None, wait=None, close=None, start=None, stop=None, add_tags=None, del_tags=None, download_file=None, upload_file=None):  # noqa: E501
        """Command - a model defined in OpenAPI"""  # noqa: E501

        self.__exec = None
        self._open = None
        self._wait = None
        self._close = None
        self._start = None
        self._stop = None
        self._add_tags = None
        self._del_tags = None
        self._download_file = None
        self._upload_file = None
        self.discriminator = None

        if _exec is not None:
            self._exec = _exec
        if open is not None:
            self.open = open
        if wait is not None:
            self.wait = wait
        if close is not None:
            self.close = close
        if start is not None:
            self.start = start
        if stop is not None:
            self.stop = stop
        if add_tags is not None:
            self.add_tags = add_tags
        if del_tags is not None:
            self.del_tags = del_tags
        if download_file is not None:
            self.download_file = download_file
        if upload_file is not None:
            self.upload_file = upload_file

    @property
    def _exec(self):
        """Gets the _exec of this Command.  # noqa: E501


        :return: The _exec of this Command.  # noqa: E501
        :rtype: ExecCommand
        """
        return self.__exec

    @_exec.setter
    def _exec(self, _exec):
        """Sets the _exec of this Command.


        :param _exec: The _exec of this Command.  # noqa: E501
        :type: ExecCommand
        """

        self.__exec = _exec

    @property
    def open(self):
        """Gets the open of this Command.  # noqa: E501


        :return: The open of this Command.  # noqa: E501
        :rtype: object
        """
        return self._open

    @open.setter
    def open(self, open):
        """Sets the open of this Command.


        :param open: The open of this Command.  # noqa: E501
        :type: object
        """

        self._open = open

    @property
    def wait(self):
        """Gets the wait of this Command.  # noqa: E501


        :return: The wait of this Command.  # noqa: E501
        :rtype: object
        """
        return self._wait

    @wait.setter
    def wait(self, wait):
        """Sets the wait of this Command.


        :param wait: The wait of this Command.  # noqa: E501
        :type: object
        """

        self._wait = wait

    @property
    def close(self):
        """Gets the close of this Command.  # noqa: E501


        :return: The close of this Command.  # noqa: E501
        :rtype: object
        """
        return self._close

    @close.setter
    def close(self, close):
        """Sets the close of this Command.


        :param close: The close of this Command.  # noqa: E501
        :type: object
        """

        self._close = close

    @property
    def start(self):
        """Gets the start of this Command.  # noqa: E501


        :return: The start of this Command.  # noqa: E501
        :rtype: StartCommand
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this Command.


        :param start: The start of this Command.  # noqa: E501
        :type: StartCommand
        """

        self._start = start

    @property
    def stop(self):
        """Gets the stop of this Command.  # noqa: E501


        :return: The stop of this Command.  # noqa: E501
        :rtype: StopCommand
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """Sets the stop of this Command.


        :param stop: The stop of this Command.  # noqa: E501
        :type: StopCommand
        """

        self._stop = stop

    @property
    def add_tags(self):
        """Gets the add_tags of this Command.  # noqa: E501


        :return: The add_tags of this Command.  # noqa: E501
        :rtype: list[str]
        """
        return self._add_tags

    @add_tags.setter
    def add_tags(self, add_tags):
        """Sets the add_tags of this Command.


        :param add_tags: The add_tags of this Command.  # noqa: E501
        :type: list[str]
        """

        self._add_tags = add_tags

    @property
    def del_tags(self):
        """Gets the del_tags of this Command.  # noqa: E501


        :return: The del_tags of this Command.  # noqa: E501
        :rtype: list[str]
        """
        return self._del_tags

    @del_tags.setter
    def del_tags(self, del_tags):
        """Sets the del_tags of this Command.


        :param del_tags: The del_tags of this Command.  # noqa: E501
        :type: list[str]
        """

        self._del_tags = del_tags

    @property
    def download_file(self):
        """Gets the download_file of this Command.  # noqa: E501


        :return: The download_file of this Command.  # noqa: E501
        :rtype: DownloadFileCommand
        """
        return self._download_file

    @download_file.setter
    def download_file(self, download_file):
        """Sets the download_file of this Command.


        :param download_file: The download_file of this Command.  # noqa: E501
        :type: DownloadFileCommand
        """

        self._download_file = download_file

    @property
    def upload_file(self):
        """Gets the upload_file of this Command.  # noqa: E501


        :return: The upload_file of this Command.  # noqa: E501
        :rtype: UploadFileCommand
        """
        return self._upload_file

    @upload_file.setter
    def upload_file(self, upload_file):
        """Sets the upload_file of this Command.


        :param upload_file: The upload_file of this Command.  # noqa: E501
        :type: UploadFileCommand
        """

        self._upload_file = upload_file

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
        if not isinstance(other, Command):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
