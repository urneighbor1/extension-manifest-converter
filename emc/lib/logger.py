# Copyright 2021 Google Inc. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations


class Logger:
    _instance: Logger | None = None
    _log_level = 2  # 0: error, 1: warn, 2: status, 3: verbose

    def __new__(cls) -> Logger:
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._lines: list[str] = []
        return cls._instance

    def log(self, message: str, level: int = 2) -> None:
        if level > self._log_level:
            return
        prefix = ""
        if level == 0:
            prefix = "Error: "
        elif level == 1:
            prefix = "Warn: "
        print("{}{}".format(prefix, message))
