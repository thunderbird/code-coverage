# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import absolute_import

import os

PROJECT_NAME = "code-coverage-backend"
APP_NAME = "code_coverage_backend"
DEFAULT_REPOSITORY = os.getenv("REPOSITORY", "mozilla-central")
