import pandas as pd

from tz.osemosys import (
    Model,
    Technology,
    TimeDefinition,
    Commodity,
    Region,
    Impact,
    OperatingMode,
)

time_definition = TimeDefinition(id="years-only", years=range(2020, 2051))

# ---
# REGIONS

nodes = pd.read_csv('../models/PAK/nodes.csv')

regions = []
for i, row in nodes.iterrows():
    r = Region( id=row['ADM1_PCODE'], long_name=row['ADM1_EN'] )
    regions.append(r)

# ---
# DEMAND

demand = pd.read_csv('../data/demand/pak-demand.csv')
demand.year = demand.year.astype('str')
demand.set_index('year', inplace=True)

demand_annual = {}
for i, row_nodes in nodes.iterrows():
    demand_annual[ row_nodes['ADM1_PCODE'] ] = demand[ row_nodes['ADM1_PCODE'] ].to_dict()

basic_demand_profile = dict(
    id="electricity",
    demand_annual=demand_annual,
    #demand_profile={"*": {"0h": 0.0, "6h": 0.2, "12h": 0.3, "18h": 0.5}},
)

commodities = [Commodity(**basic_demand_profile)]

# ---
# TECHNOLOGIES

technologies = [
    Technology(
        id="coal-gen",
        operating_life=40,  # years
        capex=800,  # mn$/GW
        # straight-line reduction to 2040
        residual_capacity={
            yr: 25 * max((1 - (yr - 2020) / (2040 - 2020), 0))
            for yr in range(2020, 2051)
        },
        operating_modes=[
            OperatingMode(
                id="generation",
                # $mn20/Mt.coal / 8.14 TWh/Mt coal * 8760 GWh/GW / 0.3 /1000 GWh/TWh (therm eff)
                opex_variable=20 / 8.14 * 8760 / 0.3 / 1000,  # $71/GW/yr
                output_activity_ratio={"electricity": 1.0 * 8760},  # GWh/yr/GW
                emission_activity_ratio={
                    "CO2": 0.354 * 8760 / 1000
                },  # Mtco2/TWh * 8760GWh/Gw/yr /1000 GWh/TWh
            )
        ],
    ),
    Technology(
        id="solar-pv",
        operating_life=25,
        capex=1200,
        capacity_factor=0.3,
        operating_modes=[
            OperatingMode(
                id="generation",
                opex_variable=0,
                output_activity_ratio={"electricity": 1.0 * 8760},  # GWh/yr/GW
            )
        ],
    ),
]

# ---
# SETUP MODEL

impacts = [Impact(id="CO2", penalty=60)]  # 60 $mn/Mtonne

model = Model(
    id="simple-pakistan-model",
    time_definition=time_definition,
    regions=regions,
    commodities=commodities,
    technologies=technologies,
    impacts=impacts,
    #cost_of_capital=({region:{technology:float}}),
    #discount_rate=({region:float}),
)

model.solve()