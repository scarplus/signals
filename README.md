# Signals
signals generated based on algorithms for paper trading
None of these are intended to be correct. It is just a fun project.


This project is to use various trading algorithms and generate python based output for each algorithm indicating which ticker to hold at the time of run for each algorithm. Algorithm are identified as symphony and the outputs as tickers or signals.

Any changes in links will be updated here going forward.

Mappings of various composer symphony and the short names used in output sheet -- https://docs.google.com/spreadsheets/d/1duub-kYJIrBrEEbuytyWt7L7xuD-BmkwCTH86usd4oI/edit#gid=0

Link to output file -
aggregated view in a column of last run [mind end up using this one for tda bot trading] - https://drive.google.com/file/d/13ER4Rvm9vo0b-LvPvSwjgs0PwTROJuMa/view?usp=sharing

Link to Current Percentage Gain Report for various symfs in mapping file. This file will show symfs, symfs value at buy most recent 4pm(price,tickers used is as per the 4pm run data from the Signal file) and symf value at the recent run of this report. Then percentage change is displayed. (today-yesterday)*100/yesterday. This will run almost everytime signal job runs.
https://drive.google.com/file/d/13h8Rxx8h-k5n9YFAJzF_QZ54sZdaEwnx/view?usp=sharing

Above data is stored for history in this file. Above data can be for any sell time of report run time of day, but buy data will be recent 4pm's sheet data. Historical data will be saved only for 4pm job run.
Link to Historical Performances of symf in mapping file = https://drive.google.com/file/d/13s3WmrpppMV79UKWMteC07YOxl2rN7Ws/view?usp=sharing
Each row is the today's percentage gain(sell value) from most recent 4pm values (buy data). 

Ideally most recent 4pm will refer to previous day 4pm. but if the report is run later in evening around 8pm, then the report data will be today's 8pm vs today's 4pm .


unaggregated, row view of last run - https://drive.google.com/file/d/13btAxPPNm1nYvzzJ0prTW3kFsY6Vd99o/view?usp=sharing

historical data [unaggregated row view] - https://drive.google.com/file/d/13Et8KRpCO9eyzGo9TDkYv_WnAP7-M3ON/view?usp=sharing

historical metrrics data - https://drive.google.com/file/d/13WFpiU4bUJ2yfdUSHha1PgWZuUo-Ekui/view?usp=sharing

Gist file that shows code, where line number can be mapped in Singal2/Signal historical file to find the branch which triggered the signal
bb304a- https://gist.github.com/scarplus/5d3f2a2c3d9c61d47f697e901e5ff8f3



