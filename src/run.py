import os
import matplotlib.pyplot as plt

import osemoviz as viz
from tz.osemosys import Model

# ---------
# CONFIGS
# ---------

output_path = '../outputs/results/'

countries_to_run = [
    # 'GAB',
    # 'GMB',
    # 'HTI',
    # 'MDG',
    # 'PAK',
    'PHL',
    # 'RWA',
]

scenarios_to_run = [
    'BAU',
    'CPP',
    'NDC',
]

# ---------
# RUN MODELS
# ---------

print('-'*50)
print('STARTING MODEL RUN')
print('')

for country in countries_to_run:
    for scenario in scenarios_to_run:
        print(f'Running: {country}-{scenario}')
        # define path
        path_to_model = f'../models/{country}/{country}-{scenario}/'
        # load model from folder
        model = Model.from_yaml(path_to_model)
        # solve
        model.solve(solver='gurobi')
        
        # ---------
        # SAVE RESULTS
        # ---------
        fname = 'model-solution' + model.id + '.nc'

        dir_path = os.path.join(
            output_path, 
            country, 
            country + '-' + scenario
        )

        # check if path exists
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        model.solution.to_netcdf(
            os.path.join(
                dir_path,
                fname,
            )
        )

        print('saved solution to: ' + dir_path + '/' + fname)

        # ---------
        # POST PROCESSING
        #
        #   - There are 9 essential outputs we produce here as requested by the V20 group.
        #   - We also produce some extra outputs that not required by the grant but useful for context.
        #   - We produce all outputs using the tza-osemoviz package.
        #
        # ---------

        # ---
        # (1) Energy demand by sector and energy source (energy balance/year)

        # make csv
        (
            viz
            .get
            .AnnualDemandByRegion(model)
            .to_csv(
                os.path.join(
                    dir_path,
                    'AnnualDemandByRegion.csv',
                )
            )
        )

        # export figure
        ax = viz.plot.DemandByRegion(model)
        plt.savefig(
            os.path.join(
                dir_path,
                'AnnualDemandByRegion.pdf'
            )
        )

        # ---
        # (2) Power generation capacity by technology (MW in each year)

        # make csv
        (
            viz
            .get
            .AnnualCapacityByTechnology(model)
            .to_csv(
                os.path.join(
                    dir_path,
                    'AnnualCapacityByTechnology.csv',
                )
            )
        )

        # export figure
        ax = viz.plot.CapacityByTechnology(model)
        plt.savefig(
            os.path.join(
                dir_path,
                'AnnualCapacityByTechnology.pdf'
            )
        )

        # ---
        # (3) Power generation by technology (MWh/year)

        # make csv
        (
            viz
            .get
            .AnnualGenerationByTechnology(model)
            .to_csv(
                os.path.join(
                    dir_path,
                    'AnnualGenerationByTechnology.csv',
                )
            )
        )

        # export figure
        ax = viz.plot.GenerationByTechnology(model)
        plt.savefig(
            os.path.join(
                dir_path,
                'AnnualGenerationByTechnology.pdf'
            )
        )

        # ---
        # (4) Cost of technology (capital and O&M, per MW in each year)
        # TODO
        
        # ---
        # (5) Total investment required (timeframe) per year for new capacity plus grid and storage
        # TODO

        # ---
        # (6) LCOE by technology (incl. timeframe)
        # TODO

        # ---
        # (7) Average electricity price at the country level
        # TODO

        # ---
        # (8) Energy access (access to electricity, % of population)
        # TODO

        # ---
        # (9) Number of new jobs in power generation and grid
        # TODO

        # ---------
        # ADDITIONAL OUTPUTS
        # ---------

        # ---
        # (1) Emissions by technology

        # export to csv
        (
            viz
            .get
            .AnnualEmissionsByTechnology(model)
            .to_csv(
                os.path.join(
                    dir_path,
                    'AnnualEmissionsByTechnology.csv',
                )
            )
        )

        # export figure figure
        ax = viz.plot.EmissionsByTechnology(model)
        plt.savefig(
            os.path.join(
                dir_path,
                'AnnualEmissionsByTechnology.pdf'
            )
        )

        

print('-'*50)