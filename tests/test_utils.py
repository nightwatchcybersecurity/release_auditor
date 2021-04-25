#
# Copyright (c) 2021 Nightwatch Cybersecurity.
#
# This file is part of release_auditor
# (see https://github.com/nightwatchcybersecurity/release_auditor).
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
import re

from release_auditor.utils import ReleaseAuditorUtils


# Tests for misc utils methods
class TestUtils(object):
    def test_get_version_format_valid(self):
        pattern = re.compile(r'^(\d+\.)?(\d+\.)?(\*|\d+)$')
        assert pattern.match(ReleaseAuditorUtils.get_version()) is not None