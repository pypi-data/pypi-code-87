#! /usr/bin/env python
# coding=utf-8
# Copyright (c) 2021 Uber Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from ludwig.datasets.base_dataset import DEFAULT_CACHE_LOCATION
from ludwig.datasets.kdd_dataset import KDDCup2009Dataset


def load(cache_dir=DEFAULT_CACHE_LOCATION, split=False):
    dataset = KDDAppetency(cache_dir=cache_dir)
    return dataset.load(split=split)


class KDDAppetency(KDDCup2009Dataset):
    """
    The KDD Cup 2009 Appetency dataset

    Additional Details:

    https://www.kdd.org/kdd-cup/view/kdd-cup-2009/Data
    """

    def __init__(self, cache_dir=DEFAULT_CACHE_LOCATION):
        super().__init__(task_name="appetency", cache_dir=cache_dir)
