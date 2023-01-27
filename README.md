# Signals
signals generated based on algorithms for paper trading
None of these are intended to be correct. It is just a fun project.


This project is to use various trading algorithms and generate python based output for each algorithm indicating which ticker to hold at the time of run for each algorithm. Algorithm are identified as symphony and the outputs as tickers or signals.

Any changes in links will be updated here going forward.

Mongo Chart on various metrtics/performance. https://charts.mongodb.com/charts-signal-wuqhd/public/dashboards/8273f444-cea6-482d-b232-d27018c3120b
Gain % since last Market Close - this chart is updated every 15 minutes from 9am est to 4pm est. Other charts get updated using 3:56pm(~4pm) data everyday.

Mappings of various composer symphony and the short names used in output sheet -- https://docs.google.com/spreadsheets/d/1duub-kYJIrBrEEbuytyWt7L7xuD-BmkwCTH86usd4oI/edit#gid=0

Link to output file -
aggregated view in a column of last run [might end up using this one for tda bot https://github.com/scarplus/signals/wiki/Signal-Trader-for-TDA trading check the wiki page for tdTrader details.  ] - https://drive.google.com/file/d/13ER4Rvm9vo0b-LvPvSwjgs0PwTROJuMa/view?usp=sharing
This file will be generated at 10:15am, 12:30pm, 12:56pm, 2:30pm, 3:01pm, 3:15pm.. every 10 minutes then until 4:01pm, 8:30pm

Similar Signal file can be generated on-demand by calling this google api url https://mainsignal-6rkoj3i67a-uk.a.run.app

The code behind this url hosted on Google Cloud is not as agile as the google drive version, since I plan to keep the google api code as stable version and update it with new symphonies only weekly.
It will take around a minute (so if needed browser can be closed after triggering it) to complete and display a json/dictionary format output . It  it is not structured as a meaningful json. A proper readable output file will be written to file after the above url call is completed at this url csv url
https://storage.googleapis.com/randomsignals/SignalBV8G0KSWZWKJPK2.csv

Depricated in lieu of charts - Link to Current Percentage Gain Report for various symfs in mapping file. This file will show symfs, symfs value at buy most recent 4pm(price,tickers used is as per the 4pm run data from the Signal file) and symf value at the recent run of this report. Then percentage change is displayed. (today-yesterday)*100/yesterday. This will run almost everytime signal job runs.
https://drive.google.com/file/d/13h8Rxx8h-k5n9YFAJzF_QZ54sZdaEwnx/view?usp=sharing

Above data is stored for history in this file. Above data can be for any sell time of report run time of day, but buy data will be recent 4pm's sheet data. Historical data will be saved only for 4pm job run.
Link to Historical Performances of symf in mapping file = https://drive.google.com/file/d/13s3WmrpppMV79UKWMteC07YOxl2rN7Ws/view?usp=sharing
Each row is the today's percentage gain(sell value) from most recent 4pm values (buy data). 

Ideally most recent 4pm will refer to previous day 4pm. but if the report is run later in evening around 8pm, then the report data will be today's 8pm vs today's 4pm .


unaggregated, row view of last run - https://drive.google.com/file/d/13ciEIPwTFsCArVO0HMpfQq_fvtOIdOse/view?usp=drivesdk
This view will have entries in row format. one row for eash symph. Here is how to read signal value in this file [Signal="Ticker1_<Allocation_in_decimal_percent>.<number indicating line number that generated this ticker/allocation in my code for debug purpose>"] It may have some entries that are not in main Symph_Signal.csv file in cases where total allocation adds up to be more than 105%. It is possible in situations where some branches have a list of tickers without explicitly specifying percentage alloaction or if inverse volatility is used.

historical data [unaggregated row view] - https://drive.google.com/file/d/13Et8KRpCO9eyzGo9TDkYv_WnAP7-M3ON/view?usp=sharing

historical metrics data - https://drive.google.com/file/d/13WFpiU4bUJ2yfdUSHha1PgWZuUo-Ekui/view?usp=sharing

Gist file that shows code, where line number can be mapped in Singal2/Signal historical file to find the branch which triggered the signal
bb304a- https://gist.github.com/scarplus/5d3f2a2c3d9c61d47f697e901e5ff8f3



