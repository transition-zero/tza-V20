
<img src="https://github.com/transition-zero/V20/blob/main/data/assets/readme-banner.png" alt="" width="650" align="center">

# The Vulnerable Twenty (V20)

TransitionZero has partnered with the [V20 group](https://www.v-20.org/) to produce electricity sector data and modelling for a set of developing countries that are acutely vulnerable to climate change. The outputs of this modelling will be used in Climate Prosperity Plans (CPP) to be published by V20. We have developed customised scenarios based on each country’s CPP and in conjunction with Financial Futures Center (FCC), as well as regional stakeholders.

Specifically, we have collated data and developed models for:

- 🇭🇹 Haiti
- 🇲🇬 Madagascar
- 🇰🇬 Kyrgyzstan
- 🇬🇲 The Gambia
- 🇳🇦 Namibia 
- 🇬🇦 Gabon
- 🇵🇰 Pakistan

# Contributors
The data and code provided here was developed by the following modellers/analysts at TransitionZero:

- [Aman Majid](https://www.transitionzero.org/team/aman-majid)
- [Handriyanti Diah Puspitarini](https://www.transitionzero.org/team/handriyanti-diah-puspitarini)
- [Abhishek Shivakumar](https://www.transitionzero.org/team/abhishek-shivakumar)

# Getting started

## Setup
Firstly, clone or download this repository (or an older version). 

Next, create a project environment using the yaml file in the repository as below.

conda:

```
conda env create --prefix ./env --file environment.yml
conda activate ./env
```

mamba:

```
mamba env update -n GPO --file environment.yml
conda activate ./env
```

Additionally, install a solver for optimisation. We recommend using [Gurobi](https://www.gurobi.com/downloads/), which is free for academic use.

## Usage (running a model)

# Contributing and Support

We strongly welcome anyone interested in contributing to this project. If you have any ideas, suggestions or encounter problems, feel invited to file issues or make pull requests on GitHub.

To discuss ideas for the project, please contact one of the main contributors. 

# Relevant outputs

# Licence

Copyright 2020-2023 [TransitionZero](https://www.transitionzero.org/)

This repository is licensed under the open source [XXX](...).
