**Introduction:** The data package provided for the Barrios-ASU ISS
Consumables project contains the following data sets:

-   Food US

-   Food RS

-   EDV

-   KTO

-   ACY Filter

-   Filter Inserts

-   Pretreat Tanks

-   Water US

-   Water RS

-   Gas US (O2/N2)

-   Gas RS (O2/N2)

-   Flight Plan Vehicles

-   Flight Plan EVA

-   Flight Plan Crew

-   Definition Tables

-   Historical Usage Rate Parameters

-   Data Dictionary

Those data are provided in CSV files in the CSV folder of this data
package directory. The table below indicates which file contains a given
data item.

**Data Package Contents and File Location**

| Item       | Location                                                |
| ---------- | ------------------------------------------------------- |
| Food US    | inventory_mgmt_system_consumables_20220101-20230905.csv |
|            |                                                         |
|            | stored_items_only_                                      |
|            | inventory_mgmt_system_consumables_20220101-20230905.csv |
| -------    | ------------------------------------------------------- |
| Food RS    | inventory_mgmt_system_consumables_20220101-20230905.csv |
|            |                                                         |
|            | stored_items_only_                                      |
|            | inventory_mgmt_system_consumables_20220101-20230905.csv |
| -------    | ------------------------------------------------------- |
| EDV        | inventory_mgmt_system_consumables_20220101-20230905.csv |
|            |                                                         |
|            | stored_items_only_                                      |
|            | inventory_mgmt_system_consumables_20220101-20230905.csv |
| -------    | ------------------------------------------------------- |
| KTO        | inventory_mgmt_system_consumables_20220101-20230905.csv |
|            |                                                         |
|            | stored_items_only_                                      |
|            | inventory_mgmt_system_consumables_20220101-20230905.csv |
| -------    | ------------------------------------------------------- |
| ACY Filter | inventory_mgmt_system_consumables_20220101-20230905.csv |
|            |                                                         |
|            | stored_items_only_                                      |
|            | inventory_mgmt_system_consumables_20220101-20230905.csv |
| -------    | ------------------------------------------------------- |
| Filter     | inventory_mgmt_system_consumables_20220101-20230905.csv |
| Inserts    |                                                         |
|            | stored_items_only_                                      |
|            | inventory_mgmt_system_consumables_20220101-20230905.csv |
| -------    | ------------------------------------------------------- |
| Pretreat   | inventory_mgmt_system_consumables_20220101-20230905.csv |
| Tanks      |                                                         |
|            | stored_items_only_                                      |
|            | inventory_mgmt_system_consumables_20220101-20230905.csv |
| -------    | ------------------------------------------------------- |
| Water US   | u                                                       |
|            | s_weekly_consumable_water_summary_20220102-20230903.csv |
| -------    | ------------------------------------------------------- |
| Water RS   | rsa_consumable_water_summary_20220103-20230828.csv      |
| -------    | ------------------------------------------------------- |
| Gas US     | us                                                      |
|            | _rs_weekly_consumable_gas_summary_20220102-20230903.csv |
| -------    | ------------------------------------------------------- |
| Gas RS     | us                                                      |
|            | _rs_weekly_consumable_gas_summary_20220102-20230903.csv |
| -------    | ------------------------------------------------------- |
| Flight     | iss_flight_plan_20220101-20251231.csv                   |
| Plan       |                                                         |
| Vehicles   |                                                         |
| -------    | ------------------------------------------------------- |
| Flight     | iss_flight_plan_20220101-20251231.csv                   |
| Plan EVAs  |                                                         |
| -------    | ------------------------------------------------------- |
| Flight     | iss_flight_plan_crew_20220101-20251321.csv              |
| Plan Crew  |                                                         |
| -------    | ------------------------------------------------------- |
| Definition | thresholds_limits_definition.csv                        |
| Tables     |                                                         |
|            | ims_consumables_category_lookup.csv                     |
|            |                                                         |
|            | iss_flight_plan_crew_nationality_lookup.csv             |
|            |                                                         |
|            | rates_definition.csv                                    |
| -------    | ------------------------------------------------------- |
| Historical | rates_definition.csv                                    |
| Usage Rate |                                                         |
| Parameters |                                                         |
| -------    | ------------------------------------------------------- |
| Historical | USOS On Orbit O2 Example Analysis.png                   |
| Analysis   |                                                         |
| Samples    |                                                         |
| -------    | ------------------------------------------------------- |
| Data       | Data Dictionary.xlsx                                    |
| Dictionary |                                                         |
| -------    | ------------------------------------------------------- |

**Assumptions:**

-   Data which is associated with a past date is an "actual" - a
    > measured factual value

-   Data which is associated with a future date (in the case of the
    > Flight Plan data) is a planned value -- these are variable and can
    > change as strategic planning updates the ISS Program's
    > necessities, but will remain static in the data set provided
    > herein

-   In the IMS data sets, many dimensional values are erroneous. A
    > corrected volume value is applied, and those values can be seen in
    > the data set, in fields as defined by the Data Dictionary

-   The following Flight Plan vehicles are available for consumables
    > resupply

    -   NG

    -   SpX Cargo

    -   Progress

    -   Axiom

    -   HTV-X

**Focus**

Remember the following prompts for analysis, and center all of the
effort around deriving insights into these prompts:

Questions:

1.  What is the percent difference between historical consumable usage
    > rate assumptions and actual calculated usage rates in mission time
    > frames between resupply?

2.  What resupply quantities are necessary, considering planned resupply
    > vehicle traffic from the ISS Flight Plan, planned On-Orbit Crew
    > counts, and historical usage rates to sustain minimum supply
    > thresholds, plus a 10% safety factor, through the next two years?

3.  What resupply quantities meet the requirements of question #2 while
    > minimizing launch vehicle quantity? (e.g., launching 10,000
    > granola bars would ensure the minimum thresholds are not violated,
    > but is not a realistic or optimal strategy for balancing launch
    > mass requirements with supply requirements)

Predictive modeling:

1.  What month in the next two years of the Flight Plan timeline is most
    > likely to incur a violation of minimum supply thresholds?

2.  Which consumables item(s) are most likely to incur a violation of
    > minimum supply thresholds in the next two years of the future
    > Flight Plan timeline?
