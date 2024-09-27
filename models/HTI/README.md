This is the model for [Haiti](https://www.v-20.org/members/haiti/), using data sources from: 

| Variable | Sources |
| -------- | ------- |
| Annual electricity demand | Global interconnector study |
| Demand profile | [Global interconnector study](https://github.com/transition-zero/feo-esmod-osemosys/blob/master/resources/data/All_Demand_UTC_2015.csv)
| Existing and planned capacities | [V20 shared dataset](https://docs.google.com/spreadsheets/d/1FT6Orao0IHLY0VnN8gmvvY4xLiX6nlxM/edit?usp=sharing&ouid=111674383854079489042&rtpof=true&sd=true)
| Carbon emission intensity per technology | [V20 shared dataset](https://docs.google.com/spreadsheets/d/1FT6Orao0IHLY0VnN8gmvvY4xLiX6nlxM/edit?usp=sharing&ouid=111674383854079489042&rtpof=true&sd=true)
| Efficiency per technology | [V20 shared dataset](https://docs.google.com/spreadsheets/d/1FT6Orao0IHLY0VnN8gmvvY4xLiX6nlxM/edit?usp=sharing&ouid=111674383854079489042&rtpof=true&sd=true)
| Technology cost | [V20 shared dataset](https://docs.google.com/spreadsheets/d/1FT6Orao0IHLY0VnN8gmvvY4xLiX6nlxM/edit?usp=sharing&ouid=111674383854079489042&rtpof=true&sd=true)
| Carbon budgets | [V20 shared dataset](https://docs.google.com/spreadsheets/d/1FT6Orao0IHLY0VnN8gmvvY4xLiX6nlxM/edit?usp=sharing&ouid=111674383854079489042&rtpof=true&sd=true)
| Power sector emission pathways | [V20 shared dataset](https://docs.google.com/spreadsheets/d/1FT6Orao0IHLY0VnN8gmvvY4xLiX6nlxM/edit?usp=sharing&ouid=111674383854079489042&rtpof=true&sd=true)
| Solar PV profile - for CF | [Global interconnector study](https://github.com/transition-zero/feo-esmod-osemosys/blob/master/resources/data/SolarPV%202015.csv)
| Windonshore profile - for CF | [Global interconnector study](https://github.com/transition-zero/feo-esmod-osemosys/blob/master/resources/data/Won%202015.csv)
| Hydropower profile - for CF | [Global interconnector study](https://github.com/transition-zero/feo-esmod-osemosys/blob/master/resources/data/Hydro_Monthly_Profiles%20(15%20year%20average).csv)

Current status: 
- Preliminary results and main assumptions taken for this model are presented [here](https://docs.google.com/document/d/1GXqUIXt5V5av3VLGAI0_97Uj_d9T1w-um76w8KUeUnY/edit#heading=h.p7vg52juaqd2). 
- 3 scenarios for this model are [BAU](models/HTI/BAU), [NDC](models/HTI/NDC) and [CPP](models/HTI/CPP)
- Coal and gas are not used (preferably) due to the non-existence of those plans in the national plans, meaning that there are no plans to import gas and coal to the country for the purpose of electricity generation

TO DO:
- [ ] Check hydropower capacity factor because it is too high now affecting huge share of hydropower in the generation mix
- [ ] Ensure the (non)existence of coal and gas in the system
- [ ] Recheck assumptions [here](https://docs.google.com/document/d/1GXqUIXt5V5av3VLGAI0_97Uj_d9T1w-um76w8KUeUnY/edit#heading=h.p7vg52juaqd2)

