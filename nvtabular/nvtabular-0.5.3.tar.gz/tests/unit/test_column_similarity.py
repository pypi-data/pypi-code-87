#
# Copyright (c) 2021, NVIDIA CORPORATION.
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
#
import cudf
import cupy
import pytest
from cupyx.scipy.sparse import coo_matrix

import nvtabular
from nvtabular.ops.column_similarity import ColumnSimilarity


@pytest.mark.parametrize("on_device", [True, False])
@pytest.mark.parametrize("metric", ["tfidf", "cosine", "inner"])
def test_column_similarity(on_device, metric):
    categories = coo_matrix(
        (
            cupy.ones(14),
            (
                cupy.array([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 4, 4, 5, 5]),
                cupy.array([0, 1, 2, 1, 2, 3, 3, 4, 5, 1, 1, 2, 0, 1]),
            ),
        )
    )

    input_df = cudf.DataFrame({"left": [0, 0, 0, 0, 4], "right": [0, 1, 2, 3, 5]})

    sim_features = [["left", "right"]] >> ColumnSimilarity(
        categories, metric=metric, on_device=on_device
    )
    workflow = nvtabular.Workflow(sim_features)

    df = workflow.transform(nvtabular.Dataset(input_df)).to_ddf().compute()
    output = df["left_right_sim"].values
    if metric in ("tfidf", "cosine"):
        # distance from document 0 to itself should be 1, since these metrics are fully normalized
        assert float(output[0]) == pytest.approx(1)

    # distance from document 0 to document 2 should be 0 since they have no features in common
    assert output[2] == 0

    # distance from document 4 to 5 should be non-zero (have category 1 in common)
    assert output[4] != 0

    # make sure that we can operate multiple times on the same matrix correctly
    sim_features = [["left", "right"]] >> ColumnSimilarity(
        categories, metric="inner", on_device=on_device
    )
    workflow = nvtabular.Workflow(sim_features)

    df = workflow.transform(nvtabular.Dataset(input_df)).to_ddf().compute()

    assert float(df["left_right_sim"].values[0]) == pytest.approx(3)
