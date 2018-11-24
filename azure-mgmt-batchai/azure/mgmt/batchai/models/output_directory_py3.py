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


class OutputDirectory(Model):
    """Output directory for the job.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. ID. The ID of the output directory. The job can use
     AZ_BATCHAI_OUTPUT_<id> environment variable to find the directory path,
     where <id> is the value of id attribute.
    :type id: str
    :param path_prefix: Required. Path prefix. The prefix path where the
     output directory will be created. Note, this is an absolute path to
     prefix. E.g. $AZ_BATCHAI_MOUNT_ROOT/MyNFS/MyLogs. The full path to the
     output directory by combining pathPrefix, jobOutputDirectoryPathSegment
     (reported by get job) and pathSuffix.
    :type path_prefix: str
    :param path_suffix: Path suffix. The suffix path where the output
     directory will be created. E.g. models. You can find the full path to the
     output directory by combining pathPrefix, jobOutputDirectoryPathSegment
     (reported by get job) and pathSuffix.
    :type path_suffix: str
    """

    _validation = {
        'id': {'required': True},
        'path_prefix': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'path_prefix': {'key': 'pathPrefix', 'type': 'str'},
        'path_suffix': {'key': 'pathSuffix', 'type': 'str'},
    }

    def __init__(self, *, id: str, path_prefix: str, path_suffix: str=None, **kwargs) -> None:
        super(OutputDirectory, self).__init__(**kwargs)
        self.id = id
        self.path_prefix = path_prefix
        self.path_suffix = path_suffix
