> ⚠️ **Most symfs are now broken due to a limitation on yfinance from Yahoo.**  
> Discussion: [GitHub Issue #2296](https://github.com/ranaroussi/yfinance/discussions/2296)

# Signals

**http://signals.slowls.com**  [use incognito mode if not working]

Disclaimer 1: The information presented here is for entertainment purposes only and should not be considered as financial advice. Please consult a licensed financial advisor for personalized recommendations. This project uses algorithmic simulations for paper trading and should not be relied upon for actual investment decisions. Any real trading using the information provided here may result in significant financial loss.

Disclaimer 2: Most of the links provided below do not lead to any private servers. They are hosted on either Google Cloud, Google Drive, or MongoDB Atlas. The links are considered safe at the time of writing, but their safety is dependent on the services provided by these third-party providers. My private server url is http://signals.slowls.com for most of same data as of charts but in tabular format and more.

Disclaimer 3: The signals generated in this project are based on data obtained from Yahoo Finance. In the event that the signals or metrics appear to be inconsistent or deviate from expected values, it may be a result of inaccuracies or discrepancies in the data provided by Yahoo Finance. Yahoo says its data should not be used for trading https://help.yahoo.com/kb/exchanges-data-providers-yahoo-finance-sln2310.html

Disclaimer 4: Until further update - all "market cap" weights will be replaced by "equal weight" if it is used in any symf due to parser limitation.


**SIGNALS**

This project utilizes various trading algorithms to generate Python-based output for each algorithm, indicating which ticker to hold at the time of execution for each algorithm. These algorithms are referred to as "symphony" and the outputs are referred to as "tickers" or "signals."

Signal Board: The project also includes a Mongo Chart Dashboard called Signal Board and it displays various metrics and performance data. This chart can be accessed at the following link: https://charts.mongodb.com/charts-signal-wuqhd/public/dashboards/8273f444-cea6-482d-b232-d27018c3120b The chart is updated every 15 minutes from 9am EST to 4pm EST, except for the "Gain % since last Market Close" chart, which is updated every 15 minutes.

Additionally, there is a mapping of various symphonies and the short names used in the output sheet, which can be found at the following link: 
1- https://raw.githubusercontent.com/scarplus/signals/main/symphony%20mappings.xlsx
2- https://docs.google.com/spreadsheets/d/1duub-kYJIrBrEEbuytyWt7L7xuD-BmkwCTH86usd4oI/edit#gid=0

BESTnd symfs:These BESTnd symfs are the result of capturing almost real-time trade data performance of almost all the symfs on the Signal board. The symfs and their past N-day performance are used to determine the selected symfs, which are combined to generate tickers. This is a dynamic group of symfs. The intention is to set it and forget it, as these BESTnd symfs will adjust their input symfs based on the performance of other symfs. Some symfs perform better in a bull market, some in a bear market, and some in a sideways market. We determine which symfs are performing well and invest in them. Look for- "Evolution with time and performance- dynamic symf of symfs" below.

The output file, aka Signals, which is an aggregated view in a column of the last run, can be accessed at the following link: submit acvess request for file 1
1. https://drive.google.com/file/d/1UGLDxTcKSwLrKdBL4_EbDfrTnJARD20C/view?usp=drivesdk         -- with 2 digit float values for allocation percent
2. https://drive.google.com/file/d/1WeCV4a-H7FXcLGO-89hO2xAoPJwrUz7e/view?usp=drive_link       -- with only integers for allocation percent
3. https://github.com/scarplus/signals/tree/main/data
4. https://drive.google.com/file/d/13ER4Rvm9vo0b-LvPvSwjgs0PwTROJuMa/view?usp=sharing. This file is generated at the following times: 10:15am, 12:30pm, 12:56pm, 2:30pm, 3:01pm, 3:15pm, and every 10 minutes until 4:01pm, 8:30pm.

Signal file can be used to auto trade in Alpaca or TD Ameritrade. refer wiki oage here https://github.com/scarplus/signals/wiki/Signal-Trader-for-Alpaca

[temporarily blocked for the month due to abuse]A similar signal file can be generated on-demand by calling the following Google API URL: https://mainsignal-6rkoj3i67a-uk.a.run.app [auto scheduled to run at 3:50pm weekdays] referred to as primary url. It is advisable to check the output file before running this as someone might have recently run it. The code behind this URL is hosted on Google Cloud and is not as agile as the Google Drive version, since it is intended to be a stable version and will only be updated with new symphonies on a weekly basis. A backup url called as "Secondary url" for same thing but for a previous version is https://mainsignalpre-6rkoj3i67a-uk.a.run.app This url will be usefule when primary url csv file seems unexpected or errors out. Whenever primary url will be updated to new code to include new/updated symfs, it older verion will be moved under secondary url to maintain a stable version in secodnary url but not up to date symfs.

It will take around a minute to complete and display a JSON/dictionary format output. The output will not be structured as a meaningful JSON. A proper readable output file will be written to file after the above URL call is completed at the following CSV URL: https://storage.googleapis.com/randomsignals/SignalBV8G0KSWZWKJPK2.csv

Please note that this data is deprecated in favor of the Charts platform and the same information can be found and downloaded there. There is also a link to a Current Percentage Gain Report for various symfs in the mapping file, which can be accessed on charts link above and same can be used to download it. This chart will show symfs, symfs value at buy most recent 4pm (price, tickers used is as per the 4pm run data from the Signal file) and symf value at the recent run of this report. Then percentage change is displayed. (today-yesterday)*100/yesterday. This will run almost every time signal job runs.

Above data is stored for history in this file. Above data can be for any sell time of report run time of day, but buy data will be recent 4pm's sheet data. Historical data will be saved only for 4pm job run.
Link to Historical Performances of symf in mapping file = https://drive.google.com/file/d/13s3WmrpppMV79UKWMteC07YOxl2rN7Ws/view?usp=sharing
Each row is the today's percentage gain(sell value) from most recent 4pm values (buy data). 

Ideally most recent 4pm will refer to previous day 4pm. but if the report is run later in evening around 8pm, then the report data will be today's 8pm vs today's 4pm .


unaggregated, row view of last run - https://drive.google.com/file/d/13ciEIPwTFsCArVO0HMpfQq_fvtOIdOse/view?usp=drivesdk
This view will have entries in row format. one row for eash symph. Here is how to read signal value in this file [Signal="Ticker1_<Allocation_in_decimal_percent>.<number indicating line number that generated this ticker/allocation in my code for debug purpose>"] It may have some entries that are not in main Symph_Signal.csv file in cases where total allocation adds up to be more than 105%. It is possible in situations where some branches have a list of tickers without explicitly specifying percentage alloaction or if inverse volatility is used.

historical Signals data [unaggregated row view] - https://drive.google.com/file/d/1BjFVWJSqDrN8D1R4WU3KlaYe4z9NNQeV/view?usp=sharing

historical metrics data - https://drive.google.com/file/d/13WFpiU4bUJ2yfdUSHha1PgWZuUo-Ekui/view?usp=sharing

Gist file that shows code, where line number can be mapped in Singal2/Signal historical file to find the branch which triggered the signal
bb304a- https://gist.github.com/scarplus/5d3f2a2c3d9c61d47f697e901e5ff8f3


Evolution with time and performance- dynamic symf of symfs ![IMG_1538](https://user-images.githubusercontent.com/112670649/219747214-de01a59c-861a-46f5-a922-693ae1a6958f.PNG)

