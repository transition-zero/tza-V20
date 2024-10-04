import os

from tz.osemosys import Model

# ---------
# CONFIGS
# ---------

output_path = '../outputs/solved_models/'

countries_to_run = [
    # 'GAB',
    'GMB',
    # 'HTI',
    # 'MDG',
    # 'PAK',
    # 'PHL',
    # 'RWA',
]

scenarios_to_run = [
    'BAU',
    'CPP',
    'NDC',
]



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
        # save
        fname = model.id + '.nc'

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

print('-'*50)