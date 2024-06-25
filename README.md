
<img src="https://github.com/transition-zero/V20/blob/main/data/images/readme-banner.png" alt="" width="650" align="center">

# The Vulnerable Twenty (V20)

TransitionZero has partnered with the [V20 group](https://www.v-20.org/) to produce electricity sector data and modelling for a set of developing countries that are acutely vulnerable to climate change. The outputs of this modelling will be used in [Climate Prosperity Plans (CPP)](https://www.v-20.org/climate-prosperity-plans) to be published by V20. We have developed customised scenarios based on each country’s CPP and in conjunction with [Financial Futures Center (FCC)](https://financialfutures.ngo/), as well as regional stakeholders.

Specifically, we have collated data and developed models for:

1. 🇬🇦 [Gabon]()
2. 🇬🇲 [The Gambia]()
3. 🇭🇹 [Haiti]()
4. 🇲🇬 [Madagascar]()
5. 🇵🇰 [Pakistan](https://github.com/transition-zero/V20/tree/main/models/PAK)
6. 🇵🇭 [Philippines]()
7. 🇷🇼 [Rwanda]() 

# Contributors
The data and code provided here was developed by the following modellers/analysts at TransitionZero:

- [Aman Majid](https://www.transitionzero.org/team/aman-majid)
- [Handriyanti Diah Puspitarini](https://www.transitionzero.org/team/handriyanti-diah-puspitarini)
- [Abhishek Shivakumar](https://www.transitionzero.org/team/abhishek-shivakumar)
- [Dan Welsby]()

# Getting started

## Setup

Firstly, clone or download this repository (or an older version). 

Next, create a project environment using the yaml file in the repository as below.

conda:

```
conda env create --prefix ./env --file environment_v20.yml
conda activate ./env
```

mamba:

```
mamba env update -n V20 --file environment_v20.yml
conda activate ./env
```

Additionally, install a solver for optimisation. We recommend using [HiGHS](https://highs.dev/), which is free and open source.

## Usage (running a model)
You can run a model with just three lines of `python` code. For instance, you can run the Pakistan model as below:

```python
from tz.osemosys import Model
model = Model.from_yaml( path/to/pakistan/directory )
model.solve()
```

More information can be found in the [example notebook here](https://github.com/transition-zero/V20/blob/main/notebooks/run_model.ipynb).

# Contributing and Support

We strongly welcome anyone interested in contributing to this project. If you have any ideas, suggestions or encounter problems, feel invited to file issues or make pull requests on GitHub.

To discuss ideas for the project, please contact [@amanmajid](mailto:aman.m@transitionzero.org)

<!-- # Relevant outputs -->

# Licence

Copyright 2020-2023 [TransitionZero](https://www.transitionzero.org/)

This repository is licensed under the open source [XXX](...).
