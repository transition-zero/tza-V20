
<img src="https://github.com/transition-zero/V20/blob/main/data/images/readme-banner.png" alt="" width="650" align="center">

# The Vulnerable Twenty (V20)

TransitionZero has partnered with the [V20 group](https://www.v-20.org/) to produce electricity sector data and modelling for a set of developing countries that are acutely vulnerable to climate change. The outputs of this modelling will be used in [Climate Prosperity Plans (CPP)](https://www.v-20.org/climate-prosperity-plans) to be published by V20. We have developed customised scenarios based on each country’s CPP and in conjunction with [Financial Futures Center (FCC)](https://financialfutures.ngo/), as well as regional stakeholders.

Specifically, we have collated data and developed models for:

1. 🇲🇬 [Madagascar](https://github.com/transition-zero/tza-V20/tree/HTI/models/MDG)
2. 🇭🇹 [Haiti](https://github.com/transition-zero/tza-V20/tree/HTI/models/HTI)
3. 🇵🇭 [Philippines](https://github.com/transition-zero/tza-V20/tree/HTI/models/PHL)
4. 🇵🇰 [Pakistan](https://github.com/transition-zero/tza-V20/tree/HTI/models/PAK)
5. 🇬🇦 [Gabon](https://github.com/transition-zero/tza-V20/tree/HTI/models/GAB)
6. 🇬🇲 [The Gambia](https://github.com/transition-zero/tza-V20/tree/HTI/models/GMB)
7. 🇷🇼 [Rwanda](https://github.com/transition-zero/tza-V20/tree/HTI/models/RWA) 

# Contributors
The data and code provided here was developed by the following modellers/analysts at TransitionZero:

- [Aman Majid](https://www.transitionzero.org/team/aman-majid)
- [Handriyanti Diah Puspitarini](https://www.transitionzero.org/team/handriyanti-diah-puspitarini)
- [Abhishek Shivakumar](https://www.transitionzero.org/team/abhishek-shivakumar)
- [Dan Welsby]()
- [Irfan Mohamed]()

# Getting started

## Setup

Firstly, clone or download this repository (or an older version). 

Next, create a project environment using the yaml file in the repository as below.

conda:

```
conda env create --name V20 --file env/V20.yml
conda activate V20
```

mamba:

```
mamba env create --name V20 --file env/V20.yml
mamba activate V20
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