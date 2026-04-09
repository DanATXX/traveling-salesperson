# Copyright 2020 D-Wave Systems Inc.
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

## ------- import packages -------
from dwave.optimization.generators import traveling_salesperson
from dwave.system import LeapHybridNLSampler

MATRIX = [
        [0,    2230, 1631, 1566, 1346, 1352, 1204],
        [2230,    0,  845,  707, 1001,  947, 1484],
        [1631,  845,    0,  627,  773,  424,  644],
        [1566,  707,  627,    0,  302,  341, 1027],
        [1346, 1001,  773,  302,    0,  368,  916],
        [1352,  947,  424,  341,  368,    0,  702],
        [1204, 1484,  644, 1027,  916,  702,    0]
        ]

model = traveling_salesperson(distance_matrix=MATRIX)   

sampler = LeapHybridNLSampler()

results = sampler.sample(model, label='NL Using Generator - TSP')

with model.lock():
        
    print(f"For state {0}, {list(sym.state(0) for sym in model.iter_decisions())} results in objective {model.objective.state(0)}") #Access variable values

# For state 0, [array([5., 4., 3., 1., 2., 6., 0.])] 
# results in objective 5422