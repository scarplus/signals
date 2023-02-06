# Signals
#disclaimer 1: Signals are generated using data from yahoo finance. If signals or metrics appear to differ from expected values then it may be due to yahoo finance data. 

#disclaimer 2: None is below links are to any private server. it is either google cloud, google drive or mongodb atlas. So links are not spams.
Signals generated based on algorithms for paper trading
None of these are intended to be correct. It is just a fun project.

This project utilizes various trading algorithms to generate Python-based output for each algorithm, indicating which ticker to hold at the time of execution for each algorithm. These algorithms are referred to as "symphony" and the outputs are referred to as "tickers" or "signals."

The project also includes a Mongo Chart that displays various metrics and performance data. This chart can be accessed at the following link: https://charts.mongodb.com/charts-signal-wuqhd/public/dashboards/8273f444-cea6-482d-b232-d27018c3120b The chart is updated every 15 minutes from 9am EST to 4pm EST, except for the "Gain % since last Market Close" chart, which is updated every 15 minutes.

Additionally, there is a mapping of various symphonies and the short names used in the output sheet, which can be found at the following link: https://docs.google.com/spreadsheets/d/1duub-kYJIrBrEEbuytyWt7L7xuD-BmkwCTH86usd4oI/edit#gid=0

The output file, which is an aggregated view in a column of the last run, can be accessed at the following link: https://drive.google.com/file/d/13ER4Rvm9vo0b-LvPvSwjgs0PwTROJuMa/view?usp=sharing. This file is generated at the following times: 10:15am, 12:30pm, 12:56pm, 2:30pm, 3:01pm, 3:15pm, and every 10 minutes until 4:01pm, 8:30pm.

A similar signal file can be generated on-demand by calling the following Google API URL: https://mainsignal-6rkoj3i67a-uk.a.run.app [auto scheduled to run at 3:50pm weekdays] It is advisable to check the output file before running this as someone might have recently run it. The code behind this URL is hosted on Google Cloud and is not as agile as the Google Drive version, since it is intended to be a stable version and will only be updated with new symphonies on a weekly basis.

It will take around a minute to complete and display a JSON/dictionary format output. The output will not be structured as a meaningful JSON. A proper readable output file will be written to file after the above URL call is completed at the following CSV URL: https://storage.googleapis.com/randomsignals/SignalBV8G0KSWZWKJPK2.csv

Please note that this data is deprecated in favor of the Charts platform and the same information can be found and downloaded there. There is also a link to a Current Percentage Gain Report for various symfs in the mapping file, which can be accessed on charts link above and same can be used to download it. This chart will show symfs, symfs value at buy most recent 4pm (price, tickers used is as per the 4pm run data from the Signal file) and symf value at the recent run of this report. Then percentage change is displayed. (today-yesterday)*100/yesterday. This will run almost every time signal job runs.

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



