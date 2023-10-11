|     | Field        | Definition                                                                                                                                                               |
|-----|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0   | datedim      | Indicates the date of an event or record. Many dates have no associated events, as this table is created as a timeline table, making it easier to plot on a time series. |
| 1   | vehicle_name | Indicates the vehicle that is incurring an event in the flight plan                                                                                                      |
| 2   | port_name    | Indicates the docking/berthing location at which a vehicle will attach to ISS                                                                                            |
| 3   | vehicle_type | Indicates the category of vehicle of a given record                                                                                                                      |
| 4   | eva_name     | Indicates the name of an EVA event, if applicable on a given date                                                                                                        |
| 5   | eva_accuracy | Indicates whether an EVA is planned, estimated, or actual (has already occurred)                                                                                         |
| 6   | event        | Indicates event type (EVA, Vehicle Dock, Vehicle Landing, etc.)                                                                                                          |
