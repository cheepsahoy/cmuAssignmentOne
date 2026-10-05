## Problem Description
We are developing a feature for dashcams that uses dashcam footage to locate children reported missing.

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

Goal_7: Be able to run the model locally with high degree of accuracy.

## User Goals
# Direct User (Direct)
Goal: Avoid excessive/expensive battery and data usage. 

# Bystanders (Indirect)
Goal: Not be falsely identified as the missing person.
Measure: Calculate the number of people falsley identified in ways that impede their day.
Data: (1) False identifications from our model, coupled with (2) Number of police stops / querries on those false cases
Operationalization: Calculate the intersection between: (1) False ID's by the model, that produced (2) Actionable stops by police, only later to be (3) found to be improper. Report the raw number. 

# Authorities (Indirect)
Goal: Recieve timely, credible, actionable sightings 

## Model Goals
Goal_1: Correctly identify missing children.

Goal_2: Avoid false positives of bystanders.

Goal_3: Maintain effectiveness accross genders

Goal_4: Maintain effectiveness accross racial/ethnic groups.
Measurement: Differences in model effectiveness compared accross racial groups.
Data: Test data of children in same age and gender conditions, differentiated by race (East Asian, South Asian, White, Black, Latino, Indigenous).
Operationalization: Calculate both recall and precision accross each racial group in each of the test samples.

Goal_5: Maintain effectiveness in low-light circumstances.

Goal_6: Maintain effectiveness in obscured-vision circumstances (e.g., behind a window, smudge, etc.).

Goal_7: Produce inferences fast enough to be of use. 
## Goal Relationships
Many goals work together, some examples: System_Goal_2, Authories_Goal, Bystanders_Goal, and Model_Goal_1 all want valid identifications with low false positive rates. Org_Goal_2 and Org_Goal_3 are complimentary because if the product works, then more sales means the product is doing more good. These benefits fit with authorities_goal by ensuring greater user-buy-in and help in missing person cases. Org_goal_5 and Model_Goal_4 are relevent as racial bias in our model and its use cases can cause friction with prominent civil rights organziations.

At the same time, there can also be tensions between the goals: not every user that wants to use the dashcam may care about the feature. The ties we built with organizations (org_goal_5) might cause friction with consumers. Any amount of data/battery usage might be not desired, and this can conflict with org_goal_2, and authorities_goal. The higher the model's accuracy in obscured conditions (model_goal_6) might interfere with bystander_goal because it increases the 'actionable' conditions where the model can produce inferences (thereby increasing the possibility there is a false positive). These are just some examples.