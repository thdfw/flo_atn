import uuid
import time
from flo import DGraph
from named_types import FloParamsHouse0

# TODO read a FloParamsHouse0 object from journaldb
flo_params = FloParamsHouse0(
    GNodeAlias = 'oak.oak',
    StartUnixS = int(time.time()),
    # Initial state
    InitialTopTempF = 140,
    InitialThermocline = 12,
    # Forecasts
    LmpForecast = [1]*48,
    DistPriceForecast = [1]*48,
    RegPriceForecast = [1]*48,
    PriceForecastUid = str(uuid.uuid4()),
    OatForecastF = [30]*48,
    WindSpeedForecastMph = [0]*48,
    WeatherUid = str(uuid.uuid4()),
    # House parameters
    AlphaTimes10 = 120,
    BetaTimes100 = -22,
    GammaEx6 = 0,
    IntermediatePowerKw = 1.5,
    IntermediateRswtF = 110,
    DdPowerKw = 12,
    DdRswtF = 160,
    DdDeltaTF = 20,
    MaxEwtF = 170,
)

print("Running Dijkstra and saving analysis to excel...")
g = DGraph(flo_params)
g.solve_dijkstra()
g.export_to_excel()
print("Done.")