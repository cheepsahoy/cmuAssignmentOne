## Problem Description
We are developing a feature for dashcams that dashcam footage to locate children reported missing. We need to ensure that t

## System Considerations
--Dashcams don't have internet access, but can communicate over USB, Bluetooth or Wifi with phones, cars, and wifi-hotspots.
--Dashcams are powered by the car's battery power supply.
--Dashcam processing power varies model by model.
--Users may be cautious about privacy and network data costs.
--Computation may be possible on dashcam through edge computing.

## Organizational Goals
Goal_1: Customers should identify this feature as a distinct offering for our product compared to competitors.

Goal_2: Contribute meaningfully to child safety.
Measure: Abducted/lost children are found due in part to our dashcam.
Data: System detection records and confirmed case outcomes from authorities/non-profits.
Operationalization: Calculate number of cases where: (1) a child is reported identified by our dashcam, (2) authorities verify that the child was correctly identified, and (3) the child was eventually returned. Report raw number of these cases.

Goal_3: Sell more dashcams.

Goal_4: Keep the feature economically viable to develop and sell.

Goal_5: Further our connections/reputation with nonprofits. 

## System Goals
Goal_1: Detect possible sightings of missing children using dashcam footage.

Goal_2: Minimize false reports to authorities.

Goal_3: Ensure timely communication of positive reports to authorities.
Measure: Total time from raw-dasham time footage to report of positive sighting delivered to authorities.
Data: (1) The timestamp of the initial dashcam footage, (2) timestamp of successful delivery of possible sighting to authorities.
Operationalization: (1) Normalize and standardize internal dashcam footage time, (2) Ensure 'delivery' of relevent data to authorities includes a timestamp once all data was successfully delivered. Compute the difference (deliveryTimestamp - sightingTimestamp). This computes raw reporting, and includes model calculation and other latency / transmission factors.

Goal_4: Minimize unnecessary transmission of raw footage.

Goal_5: Function accross distinct dashcam models.

Goal_6: Prevent unauthorized searches for people not reported missing. 

## User Goals
# Direct User (Direct)
Goal: Avoid excessive/expensive battery and data usage. 

# Bystanders (Indirect)
Goal: Not be falsely identified as the missing person.

# Authorities (Indirect)
Goal: Recieve timely, credible, actionable sightings 

## Model Goals
