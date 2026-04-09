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
from dwave.optimization import Model
import numpy as np

from dwave.system import LeapHybridNLSampler

model = Model()

matrix = np.array([
        [0,    2230, 1631, 1566, 1346, 1352, 1204],
        [2230,    0,  845,  707, 1001,  947, 1484],
        [1631,  845,    0,  627,  773,  424,  644],
        [1566,  707,  627,    0,  302,  341, 1027],
        [1346, 1001,  773,  302,    0,  368,  916],
        [1352,  947,  424,  341,  368,    0,  702],
        [1204, 1484,  644, 1027,  916,  702,    0]
        ])
    
D = model.constant(matrix)
x = model.list(7)

model.minimize((D[x[:-1], x[1:]]).sum() + (D[x[-1], x[0]]))

sampler = LeapHybridNLSampler()

results = sampler.sample(model, label='NL Example - TSP')

with model.lock():
        
    '''
    # test initial state
    model.states.resize(1)
    x.set_state(0, [0,6,2,5,3,4,1])
    print(f"For state 0, x={x.state(0)} results in objective {model.objective.state(0)}")
    
    # = 6146
    '''

    '''
    # Lowest possible value
    current_state = 0
    print(f"For state {current_state} results in objective {model.objective.state(current_state)}")
    
    # = 5422
    '''

