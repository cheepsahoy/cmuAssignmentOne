# Key Findings


## Stakeholder: Emergency dispatchers and search-and-rescue teams
**Goal/Value**: Make sound, timely search and response decisions using leads that are sufficiently reliable and actionable.
**Loss**: A false or poorly localized lead redirects teams away from the child’s actual location, delaying recovery.
**Requirement**: Leads available to responders have adequate location precision, recency, and evidential confidence for the decisions they may inform.

**Assumption:** Dashcams or paired devices can obtain a location estimate with a timestamp, and that estimate has a measurable uncertainty or quality indicator.
**Specification**: For each candidate sighting exposed to responders, provide the location estimate, its capture time, and the available location-accuracy/uncertainty information; identify when location data is unavailable or too imprecise to support localization.

**Assumption:** Dashcams, paired devices, and communication links provide enough timing information to determine when footage was captured and whether it is stale when delivered.
**Specification**: Associate each lead with the footage capture time and the lead creation or transmission time, and expose its age or freshness status to responder-facing systems.

**Assumption:** Responders have a means to receive lead metadata and evidence, and can act on explicit uncertainty and provenance information.
**Specification**: Expose a confidence or uncertainty indication together with the basis and provenance of the lead, including source device and relevant processing or report version, and mark leads that are unverified or below configured decision-use thresholds rather than presenting them as confirmed sightings.




## Stakeholder: Law enforcement agencies
**Goal / Value**: Protect children and support timely, effective missing-child investigations.
**Loss**: A potentially helpful lead cannot be acted upon because investigators cannot establish its credibility or chain of custody.
**Requirement:** Evidence used in investigations has traceable provenance, integrity, and handling records suitable for review under applicable evidentiary standards.

**Assumption**: Dashcams and connected devices have legal backing that provide trustworthy time information or indicate time uncertainty.
**Specification**: Record originating device ID, capture time/time-confidence, and associated case/alert reference with each evidence item and preserve them during transfer.

**Assumption**: Investigators and other handlers can authenticate themselves and report custody/handling actions.
**Specification**: Record authenticated receipt, access, transfer, export, and disposition events with the handler, time, and evidence item.

**Assumption**: Investigative procedures identify authorized reviewers and required records/formats.
**Specification**: Provide authorized investigators with evidence, provenance, integrity, and custody records while clearly identifying missing or uncertain records.

## Stakeholder: Child-protection and missing-person organizations
**Goal / Value**: Protect children’s safety, dignity, and privacy while coordinating public assistance and investigations.
**Loss:** An alert remains active after a child is found or a case is withdrawn, leading to continued exposure or unwanted encounters.
**Requirement**: Organizations can communicate status changes promptly, and participating parties have clear responsibilities for stopping outdated outreach.    

**Assumption**: Authorized organizations can provide authenticated case-specific status updates such as found, withdrawn, or reopened.
**Specification**: Accept and record authenticated updates containing case ID, status, effective time, and issuing organization, and forward identifications only if search is still valid.

**Assumption**: Participants can act on stop notices and report whether outreach stopped.
**Specification**: Provide acknowledgment/stoppage controls and show outstanding recipients and delivery failures.

## Stakeholder: Vehicle passengers
**Goal/Value**: Protect passengers’ privacy, dignity, and control over their personal information while traveling.
**Loss:** A passenger’s face, voice, or other identifying details are captured without their awareness, exposing them to unwanted surveillance.
**Requirement:** Passengers have reasonable notice that recording and missing-child detection may occur in the vehicle.

**Assumption**: Passengers can see or hear an in-vehicle notice before or when they enter the vehicle, and the notice remains accessible during the trip.
**Specification:** The software exposes a clear, concise notice in an in-vehicle display or audio interface before recording or missing-child detection begins, stating that recording and detection may occur and identifying the relevant data types at a high level.
