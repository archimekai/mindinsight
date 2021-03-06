# Copyright 2019 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Constant module."""


from enum import Enum


class MindInsightModules(Enum):
    """
    Enum definition for MindInsight error types.

    Note:
        Each enum value, excluding GENERAL, has an Errors class name starting with the enum value
        in Camel-Case referring to specific module.
    """
    GENERAL = 0
    LINEAGEMGR = 2
    DATAVISUAL = 5


class GeneralErrors(Enum):
    """Enum definition for general errors."""
    UNKNOWN_ERROR = 0
    PARAM_TYPE_ERROR = 1
    PARAM_VALUE_ERROR = 2
    PARAM_MISSING_ERROR = 3
    PATH_NOT_EXISTS_ERROR = 4
    FILE_SYSTEM_PERMISSION_ERROR = 8
    PORT_NOT_AVAILABLE_ERROR = 9


class LineageMgrErrors(Enum):
    """Enum definition for lineage errors."""


class DataVisualErrors(Enum):
    """Enum definition for datavisual errors."""
    RESTFUL_API_NOT_EXIST = 1
    REQUEST_METHOD_NOT_ALLOWED = 2
    SUMMARY_LOG_CONTENT_INVALID = 3
    CRC_FAILED = 4
    TRAIN_JOB_NOT_EXIST = 5
    SUMMARY_LOG_PATH_INVALID = 6
    SUMMARY_LOG_IS_LOADING = 7
    SUMMARY_LOG_LOAD_FAILED = 8
    NODE_NOT_IN_GRAPH_ERROR = 9
    PATH_NOT_DIRECTORY_ERROR = 10
