**Introduction:** The data package provided for the Barrios-ASU ISS
Consumables project contains the following data sets:

- Food US

- Food RS

- EDV

- KTO

- ACY Filter

- Filter Inserts

- Pretreat Tanks

- Water US

- Water RS

- Gas US (O2/N2)

- Gas RS (O2/N2)

- Flight Plan Vehicles

- Flight Plan EVA

- Flight Plan Crew

- Definition Tables

- Historical Usage Rate Parameters

- Data Dictionary

Those data are provided in CSV files in the CSV folder of this data
package directory. The table below indicates which file contains a given
data item.

**Data Package Contents and File Location**

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Location</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Food US</td>
<td><p>inventory_mgmt_system_consumables_20220101-20230905.csv</p>
<p>stored_items_only_inventory_mgmt_system_consumables_20220101-20230905.csv</p></td>
</tr>
<tr class="even">
<td>Food RS</td>
<td><p>inventory_mgmt_system_consumables_20220101-20230905.csv</p>
<p>stored_items_only_inventory_mgmt_system_consumables_20220101-20230905.csv</p></td>
</tr>
<tr class="odd">
<td>EDV</td>
<td><p>inventory_mgmt_system_consumables_20220101-20230905.csv</p>
<p>stored_items_only_inventory_mgmt_system_consumables_20220101-20230905.csv</p></td>
</tr>
<tr class="even">
<td>KTO</td>
<td><p>inventory_mgmt_system_consumables_20220101-20230905.csv</p>
<p>stored_items_only_inventory_mgmt_system_consumables_20220101-20230905.csv</p></td>
</tr>
<tr class="odd">
<td>ACY Filter</td>
<td><p>inventory_mgmt_system_consumables_20220101-20230905.csv</p>
<p>stored_items_only_inventory_mgmt_system_consumables_20220101-20230905.csv</p></td>
</tr>
<tr class="even">
<td>Filter Inserts</td>
<td><p>inventory_mgmt_system_consumables_20220101-20230905.csv</p>
<p>stored_items_only_inventory_mgmt_system_consumables_20220101-20230905.csv</p></td>
</tr>
<tr class="odd">
<td>Pretreat Tanks</td>
<td><p>inventory_mgmt_system_consumables_20220101-20230905.csv</p>
<p>stored_items_only_inventory_mgmt_system_consumables_20220101-20230905.csv</p></td>
</tr>
<tr class="even">
<td>Water US</td>
<td>us_weekly_consumable_water_summary_20220102-20230903.csv</td>
</tr>
<tr class="odd">
<td>Water RS</td>
<td>rsa_consumable_water_summary_20220103-20230828.csv</td>
</tr>
<tr class="even">
<td>Gas US</td>
<td>us_rs_weekly_consumable_gas_summary_20220102-20230903.csv</td>
</tr>
<tr class="odd">
<td>Gas RS</td>
<td>us_rs_weekly_consumable_gas_summary_20220102-20230903.csv</td>
</tr>
<tr class="even">
<td>Flight Plan Vehicles</td>
<td>iss_flight_plan_20220101-20251231.csv</td>
</tr>
<tr class="odd">
<td>Flight Plan EVAs</td>
<td>iss_flight_plan_20220101-20251231.csv</td>
</tr>
<tr class="even">
<td>Flight Plan Crew</td>
<td>iss_flight_plan_crew_20220101-20251321.csv</td>
</tr>
<tr class="odd">
<td>Definition Tables</td>
<td><p>thresholds_limits_definition.csv</p>
<p>ims_consumables_category_lookup.csv</p>
<p>iss_flight_plan_crew_nationality_lookup.csv</p>
<p>rates_definition.csv</p></td>
</tr>
<tr class="even">
<td>Historical Usage Rate Parameters</td>
<td>rates_definition.csv</td>
</tr>
<tr class="odd">
<td>Historical Analysis Samples</td>
<td>USOS On Orbit O2 Example Analysis.png</td>
</tr>
<tr class="even">
<td>Data Dictionary</td>
<td>Data Dictionary.xlsx</td>
</tr>
</tbody>
</table>

**Assumptions:**

- Data which is associated with a past date is an “actual” - a measured
  factual value

- Data which is associated with a future date (in the case of the Flight
  Plan data) is a planned value – these are variable and can change as strategic planning updates the ISS Program’s necessities, but will remain static in the data set provided herein

- In the IMS data sets, many dimensional values are erroneous. A corrected volume value is applied, and those values can be seen in the data set, in fields as defined by the Data Dictionary

- The following Flight Plan vehicles are available for consumables resupply

  - NG

  - SpX Cargo

  - Progress

  - Axiom

  - HTV-X

**Focus**

Remember the following prompts for analysis, and center all of the
effort around deriving insights into these prompts:

Questions:

1.  What is the percent difference between historical consumable usage rate assumptions and actual calculated usage rates in mission time frames between resupply?

2.  What resupply quantities are necessary, considering planned resupply vehicle traffic from the ISS Flight Plan, planned On-Orbit Crew counts, and historical usage rates to sustain minimum supply thresholds, plus a 10% safety factor, through the next two years?

3.  What resupply quantities meet the requirements of question \#2 while minimizing launch vehicle quantity? (e.g., launching 10,000 granola bars would ensure the minimum thresholds are not violated, but is not a realistic or optimal strategy for balancing launch mass requirements with supply requirements)

Predictive modeling:

1.  What month in the next two years of the Flight Plan timeline is most likely to incur a violation of minimum supply thresholds?

2.  Which consumables item(s) are most likely to incur a violation of minimum supply thresholds in the next two years of the future Flight Plan timeline?
