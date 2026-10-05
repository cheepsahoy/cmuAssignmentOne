# ML Risk Analysis Report

---

## Stakeholder: Dashcam owners and drivers

**Type:** direct

**Why they matter:** They operate or configure the feature and may receive alerts, incur connectivity costs, or have privacy concerns about footage processing.

### Goal / Value

Protect personal privacy and retain control over dashcam footage and any data shared for missing-child detection.

#### Potential Loss

Sensitive footage or location details are exposed to unauthorized parties, revealing drivers’ movements or bystanders’ activities.

##### Requirement

Footage and location information are protected from unauthorized access throughout capture, storage, transfer, and use.

**Engineering implications:**

**1. Assumption**

The dashcam’s hardware and operating environment expose a protected local storage area that is not directly accessible to unauthorized users or unrelated applications.

**Specification**

The software stores captured footage and derived location information only through the protected storage interface, and exposes them only to authorized local users or system components.

**2. Assumption**

Phones, vehicles, hotspots, and remote services that may exchange data with the dashcam can provide authenticated communication endpoints and support confidential data exchange.

**Specification**

For every transfer, the software sends footage or location information only to an authenticated, authorized recipient over a confidential channel, and rejects exchanges when recipient identity or authorization cannot be established.

**3. Assumption**

The detection service and any other software components granted access to footage or location data have defined, enforceable access permissions and are trusted to handle data only for their stated purpose.

**Specification**

The software provides those components only the footage and location information authorized for missing-child detection, and exposes no such data to components lacking permission or outside that purpose.

**4. Assumption**

The dashcam’s physical environment prevents unauthorized parties from bypassing software access controls to read or copy data directly from the device.

**Specification**

The software does not expose footage or location information through user interfaces, ports, or diagnostics unless the requester is authorized, and reports access only through privacy-preserving status information.

**5. Assumption**

Users can be identified to the dashcam and can express or revoke permission for sharing their footage and location information.

**Specification**

The software accepts and records user sharing permissions, transmits footage or location information for detection only while the applicable permission is active, and ceases further sharing when permission is revoked.

#### Potential Loss

Drivers’ footage is used for purposes beyond missing-child searches without their informed agreement.

##### Requirement

Drivers have clear, understandable information about data uses and meaningful choice over participation and secondary use.

**Engineering implications:**

**1. Assumption**

Drivers can access a display or companion-phone interface that can present readable information before participation is enabled.

**Specification**

Before enabling missing-child search participation, the software exposes a concise, understandable notice identifying the footage and derived data collected, the purpose and recipients, when collection occurs, retention duration, and how to opt in or decline.

**2. Assumption**

Drivers have an opportunity to make or change participation choices through the dashcam or a paired phone, and those controls can be communicated to the system.

**Specification**

The software receives and records an explicit participation choice, exposes the current choice and its consequences to the driver, and provides an interface to change or withdraw that choice; footage is not transmitted for searches when the recorded choice is off.

**3. Assumption**

The system can distinguish missing-child search use from other proposed uses and can identify when a new or changed use is requested.

**Specification**

When a proposed use falls outside the disclosed missing-child-search purpose, the software exposes a separate explanation of that use and requests a distinct affirmative choice before transmitting or otherwise making footage or derived data available for it.

**4. Assumption**

Drivers can receive notices when material changes are made to data practices, and can review relevant policy details.

**Specification**

The software exposes updated information describing material changes to data collection, sharing, or retention, identifies the change and effective date, and provides a way to review it and revise or withdraw participation before the changed practice applies.

**5. Assumption**

The software can report whether footage or derived data has been shared and can identify the applicable sharing event to the driver.

**Specification**

The software exposes a privacy activity record showing what footage or derived data was shared, for which stated purpose, with whom, and when, to the extent that information is available to the system.

#### Potential Loss

A driver or passenger is mistakenly identified as a missing child, causing unwanted scrutiny or disclosure of their location.

##### Requirement

Potential matches are sufficiently reliable and are handled with safeguards that limit disclosure and unnecessary intervention.

**Engineering implications:**

**1. Assumption**

A match can be checked against an authoritative, current missing-child report that includes usable identifying information and a clear status, and the service can communicate the report’s provenance and validity.

**Specification**

The software accepts only reports whose source, issue time, identifying fields, and active status are available; it exposes a candidate match only with the report reference and confidence information, and does not label a person as confirmed solely from a candidate match.

**2. Assumption**

The environment provides a reliable way to distinguish the image or other identifying evidence available in dashcam footage, while allowing uncertainty to be represented rather than treating all observations as conclusive.

**Specification**

For each candidate, the software exposes the evidence type, confidence or uncertainty, and time of observation to the authorized review interface, and suppresses or marks observations below a declared reliability threshold as inconclusive rather than actionable matches.

**3. Assumption**

Drivers can be given an understandable, usable choice about participation and data sharing before footage or candidate data leaves the dashcam, and the device can enforce that choice.

**Specification**

The software receives and records the driver's participation and sharing settings, exposes what data will be shared and with whom, and transmits no footage or candidate data beyond the selected scope unless the driver has enabled that sharing.

**4. Assumption**

Only a limited set of authorized recipients can handle candidate alerts, and those recipients can receive a minimal alert without needing continuous location or unrelated footage.

**Specification**

The software transmits candidate alerts only to authenticated, authorized recipients and limits each alert to the minimum information needed for review; it withholds continuous location, unrelated footage, and identifying details from other parties.

**5. Assumption**

Drivers and passengers can be notified of a potential match and have a practical channel to contest, dismiss, or request deletion of associated data before broader disclosure or intervention.

**Specification**

The software exposes a potential-match notice and accessible review or dismissal controls to the driver, supports correction or deletion requests, and does not expand disclosure or trigger an external intervention from an unreviewed candidate alone.

### Goal / Value

Use the feature without undue operational burden, unexpected expense, or disruption to safe driving and normal dashcam use.

#### Potential Loss

Connectivity or data-transfer charges become unexpectedly high for the driver.

##### Requirement

Drivers have access to affordable connectivity options and clear information about likely data use and costs.

**Engineering implications:**

**1. Assumption**

Drivers have access to at least one connectivity option, such as a phone, vehicle connection, or hotspot, with identifiable pricing or data-plan terms.

**Specification**

The software presents the available supported connectivity options and any known associated charges or plan-based costs before transmitting missing-child data, and identifies when pricing information is unavailable.

**2. Assumption**

The system can estimate the amount of data required for a scan or upload from the information being transferred.

**Specification**

Before a transfer begins, the software exposes an estimate of its data use and, where pricing information is available, the likely cost for the selected connection.

**3. Assumption**

The selected connection provides usage limits, remaining allowance, or other data-plan details when the driver or connected device makes those details available.

**Specification**

The software receives and displays available plan limits or allowance information, and warns the driver when the proposed transfer may exceed a stated limit or incur additional charges.

**4. Assumption**

Drivers can choose whether to use a particular connection and whether to proceed with a transfer.

**Specification**

The software exposes connection and transfer choices, including an option to defer or cancel a transfer, and does not start a chargeable transfer without the driver's confirmation.

**5. Assumption**

Drivers may want to restrict background data use to avoid unpredictable costs.

**Specification**

The software exposes controls for limiting or disabling cellular/background transfers and reports data transferred through the feature over a stated period.

#### Potential Loss

Feature processing drains the vehicle battery or interferes with essential dashcam functions.

##### Requirement

Vehicle power capacity and dashcam resources are sufficient for the feature without impairing essential vehicle or recording functions.

**Engineering implications:**

**1. Assumption**

The vehicle or dashcam exposes a reliable indication of available power and low-voltage or engine-off protection status to the feature.

**Specification**

The feature receives the exposed power and protection status and, when power is unavailable or a protection threshold is reached, exposes a paused or unavailable state and ceases requesting feature processing or transmission that could impair essential recording or vehicle functions.

**2. Assumption**

The dashcam platform exposes resource availability and operating-state information, and essential recording functions have identifiable priority or availability status.

**Specification**

The feature receives resource and recording-status information and exposes whether detection is active, deferred, or unavailable; it does not request feature work while the platform reports resources needed to sustain essential recording are unavailable.

**3. Assumption**

The vehicle and dashcam provide sufficient power and processing capacity during at least some operating periods for bounded feature activity without compromising essential functions.

**Specification**

The feature exposes its expected power/resource operating modes and any user-selectable processing schedule, and limits feature activity to the operating periods and resource levels reported as available by the vehicle or dashcam.

**4. Assumption**

Drivers can receive status or alert information through a display or other interface that does not require interaction while driving.

**Specification**

The feature provides non-urgent status and power/resource limitation notices through the available driver interface, and suppresses interaction-demanding prompts while the vehicle is in a driving state reported by the vehicle.

#### Potential Loss

Alerts distract the driver or prompt unsafe interaction while driving.

##### Requirement

Driver attention and road safety take priority, with alerts and any required interaction compatible with safe driving conditions.

**Engineering implications:**

**1. Assumption**

The vehicle can provide a reliable indication of driving state, such as motion, ignition state, or a connected vehicle status signal.

**Specification**

The software receives available driving-state information and, while the vehicle is indicated as moving, limits notifications to a non-interactive, low-distraction form and does not request driver input; it exposes any action requiring attention only when the vehicle is indicated as stationary.

**2. Assumption**

The dashcam has an output channel, such as a screen, speaker, or status light, whose form and intensity can be configured or constrained.

**Specification**

The software exposes alerts through configured channels and user-set limits for sound, brightness, and visual prominence, and provides no alert presentation that requires the driver to look away from the road for an extended interaction.

**3. Assumption**

The driver can safely receive urgent information through a permitted, brief alert, and the system can distinguish urgent cases from routine status information.

**Specification**

The software exposes only concise, prioritized urgent alerts during a trip, while deferring routine information and detailed instructions until the vehicle is stationary.

**4. Assumption**

The dashcam can communicate with a paired phone or vehicle display that supports driving-safe notification behavior, or can detect that no such channel is available.

**Specification**

The software transmits an alert to a paired, driving-safe channel when available; otherwise it uses the dashcam’s constrained alert mode and does not depend on phone interaction while the vehicle is moving.

#### Potential Loss

Frequent or false alerts reduce trust and lead drivers to ignore genuine reports or disable the feature.

##### Requirement

Alerts are accurate, appropriately prioritized, and supported by a reliable process for validating and updating missing-child reports.

**Engineering implications:**

**1. Assumption**

An authoritative missing-child reporting service or designated agency can provide reports, status changes, and withdrawals with identifiable provenance and timestamps.

**Specification**

The software receives and records report source, identifier, issue time, current status, and withdrawal or correction updates, and exposes the report's validation status and freshness to the driver whenever it presents an alert.

**2. Assumption**

Current, sufficiently specific descriptions and reference images can be supplied for active reports, and report subjects can be distinguished from people and scenes visible in dashcam footage.

**Specification**

For each candidate match, the software presents the driver an alert containing the linked report identifier, relevant identifying details, confidence or uncertainty indication, and observation time and location when available; it does not present an unqualified confirmed identification.

**3. Assumption**

Drivers can receive concise alerts through an available vehicle interface without needing to look away from driving, and alert urgency can be conveyed through that interface.

**Specification**

The software exposes alerts with priority and urgency appropriate to the match and report status, using the available driver-facing notification interface, and avoids requiring driver interaction to continue normal driving.

**4. Assumption**

The reporting authority can provide timely corrections and status updates, and the dashcam or connected phone can periodically exchange those updates when connectivity is available.

**Specification**

The software stores the last received report version and update time, requests or receives updates when a connection is available, and exposes when report data is stale or unavailable rather than representing it as current.

**5. Assumption**

Owners have access to settings and storage controls, and device power, connectivity, and data-use limitations can be communicated to the software.

**Specification**

The software exposes configurable alert and connectivity/data-use settings, reports resource or connection limitations that affect alert availability, and records feature operation or failures in a user-accessible status view without interrupting ordinary dashcam recording.

---

## Stakeholder: Missing children and their families

**Type:** indirect

**Why they matter:** They may benefit from faster location of a child, while inaccurate matches or exposure of sensitive case information could cause harm.

### Goal / Value

Have a missing child located and returned safely and promptly, without exposing the child or family to further danger.

#### Potential Loss

A delayed or missed sighting prolongs the child's exposure to danger or prevents timely recovery.

##### Requirement

Reliable, timely communication channels are available to relevant responders when a credible sighting occurs.

**Engineering implications:**

**1. Assumption**

Relevant responders can be identified and have current, reachable contact endpoints or dispatch systems for receiving sighting alerts.

**Specification**

The software exposes a responder directory or configured dispatch endpoint, accepts updates to responder routing details, and transmits credible-sighting alerts with the report’s time, location, and confidence information to the selected responders.

**2. Assumption**

At least one available communication path—such as a paired phone, vehicle connection, or Wi‑Fi hotspot—can provide network access when the dashcam itself is offline.

**Specification**

The software provides the sighting alert and required metadata to the available connected device or network interface for delivery to responders, and exposes whether delivery was confirmed or remains pending.

**3. Assumption**

Connectivity may be intermittent, but local storage remains available long enough to retain undelivered alerts and the device can retry or reconnect.

**Specification**

The software stores undelivered alert records, including timestamps and delivery status, and exposes or transmits them for retry when a communication path becomes available, while preventing duplicate reports from being presented as new sightings.

**4. Assumption**

Responders can receive and act on concise alerts promptly, and the communication channel supports an acknowledgement or other delivery-status response.

**Specification**

The software transmits alerts in a responder-usable format and receives and records delivery or acknowledgement status, exposing that status to the reporting user or connected device.

**5. Assumption**

Sharing identifiable child or family information is necessary only for authorized response, and the communication endpoints can be restricted to legitimate responders.

**Specification**

The software transmits only the sighting information needed for response to authorized responder endpoints and exposes the destination and information shared to the reporting user or authorized operator.

##### Requirement

Responders have clear procedures and sufficient capacity to assess leads and act quickly.

**Engineering implications:**

**1. Assumption**

Responding organizations designate accountable personnel, define roles and escalation paths, and can provide current contact and operating-procedure information to the system.

**Specification**

The software exposes each lead with the applicable responder role, assessment and escalation procedure, required actions, and current contact route, and makes procedure updates available to authorized responders.

**2. Assumption**

Responders can receive alerts through supported communication channels and provide or maintain their availability and operational status.

**Specification**

The software transmits prioritized lead notifications to designated responders over available configured channels and exposes acknowledgment, availability, and status information to authorized coordinators.

**3. Assumption**

Organizations define lead-priority criteria, response-time targets, and the capacity or coverage constraints relevant to assessing leads.

**Specification**

The software presents lead urgency, relevant response-time targets, and responder coverage or workload information, and records lead receipt, acknowledgment, and disposition times for authorized coordination.

**4. Assumption**

The information needed to evaluate and act on a lead can be shared with authorized responders in a usable, sufficiently timely form, subject to privacy and safety restrictions.

**Specification**

The software provides authorized responders with the lead evidence and context needed for assessment, including sighting time and location, confidence or uncertainty, and applicable access restrictions, and exposes updates or corrections as they become available.

#### Potential Loss

A false identification causes responders or the public to approach, detain, or otherwise endanger an unrelated child.

##### Requirement

Sighting information is independently verified to an appropriate level before an intervention or public identification.

**Engineering implications:**

**1. Assumption**

Authoritative missing-child reports are available to the system and include current identifying details, case status, and a trusted contact or agency for confirmation.

**Specification**

The software receives and stores the authoritative report, its source, timestamp, identifying details, status, and verification contact; it exposes the source and freshness alongside any candidate sighting submitted for review.

**2. Assumption**

A second independent, reliable source of evidence can be obtained for a candidate sighting, such as a separately captured observation or confirmation from an authorized responder, and its provenance can be distinguished from the original report.

**Specification**

Before marking a sighting as verified or exposing it for intervention or public identification, the software requires and records a corroborating item from a distinct source, including source and capture or confirmation time; it presents both sources and their provenance to an authorized reviewer.

**3. Assumption**

Authorized reviewers or responders can assess submitted evidence and communicate a verification decision through a trusted, authenticated channel.

**Specification**

The software transmits the candidate sighting and available corroborating evidence only to authenticated authorized reviewers, receives and records their verification decision and identity, and withholds intervention or public-identification outputs until an affirmative decision is received.

**4. Assumption**

Case information can change, and the responsible authority can notify the system when a case is closed, updated, or its verification is revoked.

**Specification**

The software receives and records case-status updates and verification revocations, and stops exposing a sighting as actionable or suitable for public identification when the associated case is closed, changed, or its verification is revoked.

##### Requirement

People handling leads are trained to avoid confrontational action based solely on an automated match.

**Engineering implications:**

**1. Assumption**

People who review or act on a reported match can be identified as authorized lead handlers, and their training status can be recorded or confirmed by the service or their organization.

**Specification**

Before exposing match details or sending a lead to an authorized handler, the software shall provide a training-status check or recorded training notice for that handler, and shall withhold actionable lead details when the required training status is not confirmed.

**2. Assumption**

Lead handlers receive software-generated match alerts through an interface that can display safety guidance alongside the alert.

**Specification**

Every match alert shown to a lead handler shall display a clear warning that an automated match is unverified and must not, by itself, prompt confrontation, detention, or approach of a child.

**3. Assumption**

The software can communicate follow-up instructions and status to handlers or designated dispatchers after a match is reviewed.

**Specification**

The software shall provide an escalation path in the lead record for requesting independent verification or contacting designated authorities, and shall expose the lead's verification and escalation status to authorized handlers before any action is taken.

**4. Assumption**

Organizations handling leads can provide approved procedures for safe, non-confrontational response and identify the appropriate source of those procedures.

**Specification**

The software shall expose the organization-approved safe-response procedure with each actionable lead, including directions to seek independent confirmation and avoid direct engagement based solely on the match.

#### Potential Loss

A public or unauthorized disclosure of the child's location enables an abductor or other harmful person to find or target the child.

##### Requirement

Access to sensitive case and location information is limited to trusted, authorized parties with a legitimate need.

**Engineering implications:**

**1. Assumption**

A trusted authority (such as a verified missing-child agency) can provide authenticated identities, roles, and current authorization decisions for people who need case information.

**Specification**

The software receives and validates authorization credentials and role/need decisions from the trusted authority, and exposes sensitive case and location information only to requesters whose current authorization permits access.

**2. Assumption**

Authorized recipients can be uniquely identified, and their approved purposes and permitted data scope can be stated in access requests.

**Specification**

The software accepts requests that identify the recipient and purpose, and returns only the case fields and location precision approved for that recipient and purpose; it does not expose data outside that scope.

**3. Assumption**

Devices and services that exchange case information have protected communication channels available, and intended recipients can be identified before transmission.

**Specification**

The software transmits sensitive case and location information only to identified, authorized endpoints over protected channels, and does not send it to public feeds or unapproved recipients.

**4. Assumption**

The operating environment can restrict access to stored case data to the software and explicitly authorized users, including when a device is lost, shared, or retired.

**Specification**

The software stores case and location information in a form accessible only through authorized interfaces, and upon access revocation or device retirement ceases exposing the information and removes or renders inaccessible retained case data.

**5. Assumption**

Authorized parties can be reached through an approved channel for urgent notifications, and notification contents can be limited to what recipients need.

**Specification**

The software sends alerts containing sensitive case or location details only to currently authorized recipients through approved channels, and exposes no identifying or location details in public-facing alerts or notification previews.

##### Requirement

Case information is handled and communicated in ways that prevent exposure to unauthorized people.

**Engineering implications:**

**1. Assumption**

The service has a reliable way to identify authorized case participants and distinguish them from other people or devices requesting case information.

**Specification**

The software receives an authenticated identity and access request for each case-information query, and exposes case details only to identities authorized for that case; requests lacking verifiable authorization receive no case details.

**2. Assumption**

Authorized recipients can be reached through communication channels whose endpoints and confidentiality protections are known to the service.

**Specification**

When transmitting case information, the software sends it only to registered authorized endpoints over channels that protect the information from disclosure in transit; it does not send case details through unprotected or unverified channels.

**3. Assumption**

People with physical or account access to a dashcam, paired phone, vehicle display, or associated storage may not all be authorized to see a case.

**Specification**

The software does not expose case details on public or shared device interfaces, notifications, or unprotected local storage, and makes locally retained case information available only after authorization.

**4. Assumption**

Authorized agencies and case managers can specify which case fields each recipient needs and can report when access should end.

**Specification**

The software receives recipient-specific permissions and access-expiration or revocation updates, and exposes or transmits only the permitted case fields while access is current.

**5. Assumption**

The service can identify whether an incoming case update or instruction comes from an authorized source.

**Specification**

The software accepts case details and changes only from verified authorized sources, and does not expose or transmit unverified case information as an actionable report.

### Goal / Value

Protect the family's privacy, dignity, and emotional wellbeing while participating in a search.

#### Potential Loss

Unnecessary collection or retention of footage reveals the family's movements, relationships, or other sensitive circumstances.

##### Requirement

Data collection and retention are limited to what is necessary for a legitimate search purpose.

**Engineering implications:**

**1. Assumption**

A legitimate search has an authorized, identifiable purpose and scope (such as a particular missing-child alert, area, and time window) that can be communicated to the system.

**Specification**

The software receives the authorized search identifier, scope, and validity period, and accepts footage or derived search data only when it falls within that active scope; it exposes the applicable scope to participating devices.

**2. Assumption**

The search authority or designated operator can determine when a search is active, concluded, or extended, and can provide those status changes to the system.

**Specification**

The software receives search-status and expiry updates, stops collecting or transmitting search-related data when authorization expires or the search is concluded, and exposes a deletion deadline for associated retained data.

**3. Assumption**

The participating dashcam can distinguish locally captured footage from the subset relevant to an active search, or can provide footage for relevance assessment without making unrelated footage available outside the device.

**Specification**

The software exposes to the search service only footage segments or search results that match the active search scope, and does not transmit unrelated footage; any retained material is limited to the relevant subset.

**4. Assumption**

Families and other affected people can be given understandable notice of what search data is collected, who receives it, and how long it is retained, and a responsible party can provide a privacy choice where participation is optional.

**Specification**

The software presents the collection, recipient, retention, and participation information before optional sharing, receives the user's participation choice, and transmits search data only in accordance with that choice and the active search authorization.

##### Requirement

Families have clear, accessible information about what data is collected, who can access it, and how long it is retained.

**Engineering implications:**

**1. Assumption**

Families can access a supported user-facing channel, such as a companion app, website, or printed notice, before or during participation in a search.

**Specification**

The software exposes a plain-language notice through the available family-facing channel before families submit or authorize search-related data, identifying each category of data collected and its purpose.

**2. Assumption**

The system operator can identify the roles or organizations authorized to receive or view search data, and any changes to that access.

**Specification**

The software presents families with the categories of people or organizations that can access their data, including relevant access limitations, and updates this information when the authorized recipients change.

**3. Assumption**

Retention periods or deletion conditions for each data category are set by the service or applicable policy and can be stated to families.

**Specification**

The software displays the retention period or deletion condition for each collected data category in the family-facing notice, and exposes revised terms when they change.

**4. Assumption**

Families may need to review the information later or may have accessibility or language needs that make a one-time notice inadequate.

**Specification**

The software makes the data-collection, access, and retention information available for later review in an accessible format and supported languages, through the family-facing channel.

#### Potential Loss

Repeated false alerts or poorly communicated leads cause severe anxiety, distress, or loss of trust in the search.

##### Requirement

Families receive leads through designated, trained contacts who communicate uncertainty and status responsibly.

**Engineering implications:**

**1. Assumption**

The search organization designates specific contacts who are trained to communicate with families and maintains a current, authorized contact roster.

**Specification**

The software receives and stores the authorized contact roster and routes family-facing lead notifications only to contacts listed as currently designated.

**2. Assumption**

Search leads can be assigned a source, confidence or uncertainty description, and a status that the search organization can update.

**Specification**

For each lead shared with a designated contact, the software transmits its available source, uncertainty/confidence information, and current status, and sends status updates when those fields change.

**3. Assumption**

Families have a way to identify their preferred authorized contact channel and to update or withdraw that preference.

**Specification**

The software receives and stores each family's contact and communication preferences, and exposes lead communications only through the family's selected, authorized channel.

**4. Assumption**

The search organization establishes rules for limiting sensitive family and lead information to what a contact needs to communicate responsibly.

**Specification**

The software exposes to each designated contact only the family and lead information authorized for that contact and records what lead information was transmitted and when.

##### Requirement

Search processes provide a means to correct inaccurate information and avoid presenting unverified leads as confirmed.

**Engineering implications:**

**1. Assumption**

Families or their authorized representatives can access a supported channel to submit corrections to case details or to report that a lead is inaccurate.

**Specification**

The software exposes an accessible correction/reporting interface that accepts the case or lead reference, the information being corrected, and the submitter's contact or authorization details, and confirms receipt without requiring public disclosure.

**2. Assumption**

A designated search authority can assess submitted corrections and leads and communicate a review status through an available channel.

**Specification**

The software records and exposes each correction or lead's review status and assessment outcome to authorized search participants, and does not label an unreviewed lead as confirmed.

**3. Assumption**

Search participants can distinguish the status and source of information when viewing or receiving alerts.

**Specification**

The software presents the source, timestamp, and verification status with each lead or alert, using explicit unverified or under-review labels until an authorized assessment confirms it.

**4. Assumption**

Authorized search personnel can amend or withdraw inaccurate case information and notify affected recipients.

**Specification**

The software accepts authorized amendments or retractions, updates the information exposed in search views, and transmits a correction or withdrawal notice to recipients who received the superseded information.

#### Potential Loss

Sensitive details about the case become publicly associated with the family, causing stigma, harassment, or lasting reputational harm.

##### Requirement

Public communications about a case respect the family's wishes where feasible and disclose only information necessary to support the search.

**Engineering implications:**

**1. Assumption**

The family or an authorized representative can communicate preferences about what case details may be shared, and those preferences can be recorded in a form available to the system.

**Specification**

The software shall receive and retain the family’s or authorized representative’s sharing preferences, including any restrictions on specific details, and make those preferences available to authorized communications workflows.

**2. Assumption**

An authorized case coordinator can provide verified case information and identify which details are necessary for public search assistance.

**Specification**

The software shall receive the coordinator-approved public-facing case information and necessity designations, and shall expose or transmit only the approved information in public communications.

**3. Assumption**

Public communications are generated or distributed through interfaces that the software can identify as public-facing and can mediate.

**Specification**

Before publishing or transmitting case-related content through a public-facing interface, the software shall apply the recorded family preferences and coordinator-approved limits, and shall prevent unapproved sensitive details from being exposed.

**4. Assumption**

Family preferences and the set of necessary search details may change as the case evolves, and an authorized representative can notify the system of updates.

**Specification**

The software shall receive updates to sharing preferences and approved search details, use the current versions for subsequent public communications, and provide authorized users with a way to review the currently recorded settings.

##### Requirement

There are effective safeguards and recourse for addressing unauthorized disclosure or misuse of case information.

**Engineering implications:**

**1. Assumption**

Families, authorized case organizations, and relevant oversight or law-enforcement bodies can be identified and provide approved contact channels for receiving reports and responses.

**Specification**

The software shall expose a reporting channel through which families or their authorized representatives can submit suspected unauthorized disclosure or misuse, and shall transmit the report and any family-approved contact details to the designated recipient.

**2. Assumption**

An accountable organization is designated to receive and investigate misuse reports and can provide case-specific status and outcome information.

**Specification**

For each submitted report, the software shall provide the designated organization with a report reference and shall expose investigation status, decisions, and available corrective actions to the reporting family or authorized representative.

**3. Assumption**

The service environment can identify which users and organizations are authorized to access case information and can receive revocation or restriction requests.

**Specification**

The software shall expose the identity and access history associated with case-information access to authorized reviewers, and provide an interface for submitting requests to restrict or revoke access when misuse is suspected.

**4. Assumption**

A designated response organization has authority and practical means to request removal or correction of disclosed information from participating services or recipients.

**Specification**

When an authorized response organization records a confirmed unauthorized disclosure, the software shall transmit removal or correction requests to the relevant participating services or recipients and expose the request status and outcome to the authorized organization and affected family.

---

## Stakeholder: Law enforcement agencies

**Type:** direct

**Why they matter:** They may submit missing-child alerts and act on leads generated by the system, affecting investigation workload and response practices.

### Goal / Value

Protect children and support timely, effective missing-child investigations.

#### Potential Loss

A child is not located promptly because a useful sighting is missed or delayed.

##### Requirement

Alerts and actionable leads reach responsible investigators promptly, with clear ownership and escalation paths.

**Engineering implications:**

**1. Assumption**

Investigating agencies provide a current, authoritative directory of responsible investigators and a way to identify the agency and jurisdiction for each reported sighting.

**Specification**

The software receives and maintains investigator and jurisdiction contact and responsibility information, and exposes each lead with the responsible agency and assigned investigator identified.

**2. Assumption**

Responsible investigators or agency alerting systems can receive notifications through at least one configured communication channel, and report delivery or failure status.

**Specification**

The software transmits alerts and actionable lead details, including sighting time, location, confidence or evidential basis, and a reference to available evidence, to configured recipients, and exposes delivery status or failure.

**3. Assumption**

Agencies define response-time expectations, backup recipients, and escalation authority for unacknowledged or unassigned leads.

**Specification**

The software records lead assignment and acknowledgement status and, when a defined response deadline passes without acknowledgement or ownership, notifies the designated escalation recipient and exposes the escalation status.

**4. Assumption**

Investigators can access a secure interface to review lead details and update ownership and investigation status.

**Specification**

The software exposes a secure interface through which authorized investigators can review leads, claim or reassign ownership, acknowledge alerts, and update lead status; it retains and makes available the resulting ownership and status history.

#### Potential Loss

Investigators divert resources from urgent cases to false or irrelevant leads.

##### Requirement

Leads are sufficiently reliable, contextualized, and prioritized for their urgency and evidentiary strength.

**Engineering implications:**

**1. Assumption**

Law-enforcement agencies can provide authoritative, current missing-child case details and update or close a case through an approved channel.

**Specification**

The software receives and timestamps authorized case details, including identifying descriptors, case status, urgency, and geographic/time scope; it exposes or transmits leads only while the associated case is active and presents the case version and update time with each lead.

**2. Assumption**

Dashcam footage or observations include usable time and location information, and these data can be associated with the captured material.

**Specification**

For each candidate observation, the software provides investigators with the associated capture time and location, or explicitly marks either value unavailable or uncertain, alongside the lead.

**3. Assumption**

Investigators can supply criteria for urgency and evidentiary strength and can review lead evidence in a secure, accessible interface.

**Specification**

The software exposes each lead with its supporting evidence or source references, uncertainty and match limitations, and separate urgency and evidentiary-strength indicators, and allows authorized investigators to sort or filter using those indicators.

**4. Assumption**

Agencies can communicate lead dispositions and corrections back to the system, and authorized users can access relevant disposition history.

**Specification**

The software receives investigator feedback such as confirmed, disproved, duplicate, or pending status, and exposes the current disposition and relevant history with subsequent presentations of the lead so agencies can avoid repeatedly acting on resolved or duplicate leads.

#### Potential Loss

Officers approach or detain an innocent person after a mistaken identification.

##### Requirement

A lead is treated as an investigative prompt rather than proof, and officers verify identity through independent evidence before consequential action.

**Engineering implications:**

**1. Assumption**

Officers can access reliable identity-checking sources or procedures independent of the dashcam-generated lead, such as official records, documents, or direct confirmation.

**Specification**

The software labels each match or alert as an unverified investigative lead and presents its supporting observations separately from any identity confirmation, without representing the alert as proof.

**2. Assumption**

Officers have an opportunity to review the lead and obtain independent evidence before approaching, detaining, or otherwise taking consequential action toward a person.

**Specification**

Before displaying or transmitting a lead for operational use, the software exposes a clear instruction that identity must be independently verified before consequential action, and does not characterize the lead alone as sufficient grounds for such action.

**3. Assumption**

Operational users can receive and understand relevant uncertainty and limitations associated with a candidate identification.

**Specification**

For each lead, the software provides the candidate evidence and identification uncertainty or limitations to officers, and includes these details in any exported or transmitted report so they can inform independent verification.

**4. Assumption**

Agencies can document verification outcomes and communicate them to personnel who may act on the lead.

**Specification**

The software provides fields to record the independent evidence checked and the verification outcome, and exposes that status with the lead wherever it is subsequently viewed or shared.

#### Potential Loss

A case is misdirected because an alert is outdated, inaccurate, or lacks essential context such as time or location.

##### Requirement

Missing-child alerts are accurate, current, and include sufficient provenance and context for investigators to assess relevance.

**Engineering implications:**

**1. Assumption**

Law-enforcement agencies or an authorized alerting authority provide updates when a child’s status, identifying details, or search boundaries change, and mark superseded reports.

**Specification**

The software receives alert revisions and status changes from the authorized source, associates each alert with its source and issue/update time, and exposes the current version while identifying or withdrawing superseded versions.

**2. Assumption**

Dashcam observations can be associated with a sufficiently trustworthy capture time and location, such as from device timestamps and available positioning data.

**Specification**

For each transmitted sighting or alert-relevant observation, the software includes the capture time and location when available, identifies unavailable or uncertain values, and exposes their reported source or accuracy.

**3. Assumption**

Investigators have an authorized channel and a means to distinguish official alert sources from unverified reports.

**Specification**

The software exposes the alert issuer/source and its verification status, and transmits alert or sighting information only with that provenance attached.

**4. Assumption**

Investigators can receive structured alert and sighting details through a supported interface and need enough information to judge whether a match is relevant.

**Specification**

The software presents or transmits the relevant child-identification and sighting context available to it, including observation time, location, and confidence or uncertainty, while distinguishing observed facts from supplied alert details.

#### Potential Loss

A potentially helpful lead cannot be acted upon because investigators cannot establish its credibility or chain of custody.

##### Requirement

Evidence used in investigations has traceable provenance, integrity, and handling records suitable for review under applicable evidentiary standards.

**Engineering implications:**

**1. Assumption**

Dashcams and connected phones or vehicles have a reliable way to identify each device and provide a trustworthy time source or indicate when time is uncertain.

**Specification**

For each captured or exported evidence item, the software records and exposes the originating device identifier, capture time and time-confidence status, and any associated case or alert reference; it preserves those fields when transferring the item to an authorized recipient.

**2. Assumption**

Evidence files and their metadata remain accessible to the software from capture through export, and the system has sufficient storage to retain relevant records.

**Specification**

The software stores the original evidence item and its associated provenance metadata, including capture context and subsequent handling events, and makes the original and records available for authorized review without silently replacing them.

**3. Assumption**

Investigators or other authorized handlers can authenticate themselves and provide handling actions or custody transfers to the system.

**Specification**

The software accepts authenticated custody and handling events, such as receipt, access, transfer, export, and disposition, associates each event with the handler, time, and evidence item, and exposes the resulting history to authorized reviewers.

**4. Assumption**

The operating environment permits evidence to be transferred to an authorized investigative system using an available connection, and recipients can receive the evidence and its accompanying records.

**Specification**

When evidence is exported, the software transmits the evidence together with its provenance, integrity-validation information, and handling history, and reports transfer status or failure to the authorized sender and recipient.

**5. Assumption**

Applicable investigative procedures identify authorized reviewers and the records or formats they need to assess authenticity and handling.

**Specification**

The software exposes evidence and associated provenance, integrity, and custody records in a reviewable form to authorized investigators, including clear indication of missing, uncertain, or invalid records.

### Goal / Value

Conduct investigations lawfully, protect public trust, and use agency resources responsibly.

#### Potential Loss

Investigators use footage or identifying information beyond the authorized missing-child purpose, harming privacy and undermining public trust.

##### Requirement

Collection, access, retention, and disclosure of footage and identifying information are limited by clear legal authority, purpose restrictions, and accountable oversight.

**Engineering implications:**

**1. Assumption**

Applicable laws, court orders, and agency policies define which missing-child purposes are authorized, what data may be collected or accessed, and the applicable retention and disclosure limits; those rules are available to the system in a current, machine-readable form.

**Specification**

The software receives the applicable authority and policy constraints for each case and data category, and exposes or transmits footage and identifying information only for the authorized missing-child purpose and within the stated collection, access, retention, and disclosure limits; it rejects requests that lack a valid basis.

**2. Assumption**

Authorized personnel can be uniquely identified, and the agency maintains reliable records of role assignments and case-specific authorization.

**Specification**

The software receives an authenticated user's identity, role, and case authorization before granting access, and exposes only the data permitted for that user's authorized role and case.

**3. Assumption**

The agency designates accountable reviewers who can receive audit records and investigate access, handling, and disclosure of the information.

**Specification**

The software produces and retains tamper-evident records of collection, access, export, retention changes, and disclosure, including the responsible user, case, time, and stated purpose, and exposes those records to designated oversight personnel.

**4. Assumption**

The agency can provide approved retention schedules and can identify when a lawful hold or case-related preservation order applies.

**Specification**

The software receives retention schedules and preservation-hold status, and deletes or renders inaccessible stored footage and identifying information when the authorized retention period ends, except while an applicable hold remains in effect.

**5. Assumption**

Law enforcement agencies and external recipients can identify and communicate a valid legal basis, authorized purpose, and permitted scope for each requested disclosure.

**Specification**

For each disclosure request, the software receives the asserted legal authority, purpose, recipient, and scope; it transmits only approved information within that scope and records the request and disclosure for oversight.

#### Potential Loss

Sensitive case information is exposed to unauthorized parties, endangering a child, family, or investigation.

##### Requirement

Case information is protected through appropriate confidentiality controls, secure handling, and timely response to suspected disclosures.

**Engineering implications:**

**1. Assumption**

Law-enforcement agencies can identify authorized personnel, roles, and the cases each person is permitted to access, and can provide updates when access changes.

**Specification**

The software receives agency-provided identities, role and case-access grants, and revocations; it exposes case information only to authenticated users whose current grants authorize that case, and reports denied access attempts to the agency.

**2. Assumption**

Agencies have approved rules defining which case data may be collected, retained, shared, and disclosed, including applicable legal restrictions.

**Specification**

The software receives agency-configured handling and retention rules, applies them to case information it stores or transmits, and exposes or shares only data permitted by those rules.

**3. Assumption**

Agencies provide a trusted destination and authorized recipients for case-related reports, evidence, and alerts.

**Specification**

The software transmits case information only to agency-designated recipients and destinations, identifies the case and recipient in each transfer, and makes transfer status available to authorized agency users.

**4. Assumption**

Agencies designate a monitored channel and responsible personnel to receive suspected-disclosure notifications and provide a response process.

**Specification**

When the software detects or receives a report of a suspected disclosure, it promptly sends a minimal, access-restricted alert to the designated agency channel and exposes relevant event details to authorized responders.

**5. Assumption**

Agency personnel and authorized recipients can provide reliable time and event information needed to review access and disclosure activity.

**Specification**

The software records and makes available to authorized agency reviewers an audit trail of case-information access, export, sharing, and suspected-disclosure events, including the case, actor or recipient, action, and time when available.

#### Potential Loss

Agency workload and response capacity are degraded by an unmanageable volume of low-quality leads.

##### Requirement

Lead volume and review demands are compatible with available staffing, training, and established case-prioritization practices.

**Engineering implications:**

**1. Assumption**

Agencies can provide or periodically update operational limits and policies, such as staffing capacity, review hours, training scope, and case-prioritization criteria.

**Specification**

The software receives agency-configured capacity limits and prioritization criteria, and exposes controls and status information for updating them so that lead handling can be constrained and organized against current agency practice.

**2. Assumption**

A lead can be represented with observable evidence and context sufficient for trained reviewers to assess its relevance and urgency, and the agency can define minimum information needed for review.

**Specification**

For each submitted lead, the software exposes the associated evidence, location/time context, confidence or uncertainty indicators, and provenance in a reviewable format, and accepts agency-defined thresholds for withholding or flagging insufficient submissions.

**3. Assumption**

Agencies have an established mechanism and personnel for receiving, triaging, and acting on leads, including a way to distinguish urgent cases from routine ones.

**Specification**

The software transmits leads through an agency-designated intake channel with case-priority and urgency fields, and exposes the queue or delivery status to authorized agency users so that incoming volume can be managed within existing triage practices.

**4. Assumption**

Agencies can estimate the review effort they can sustain and communicate when that capacity changes, while contributors can tolerate delayed, throttled, or paused submissions.

**Specification**

The software exposes aggregate lead-volume and review-demand summaries to authorized agency users and accepts pause, rate-limit, or backlog-based intake settings, applying those settings to future lead submissions and informing connected contributors of the resulting status.

---

## Stakeholder: Child-protection and missing-person organizations

**Type:** direct

**Why they matter:** They may coordinate reports and verify case details, influencing which alerts are distributed and how leads are handled.

### Goal / Value

Ensure missing-child reports and resulting leads are accurate, appropriately verified, and useful for locating the child.

#### Potential Loss

An unverified or outdated report triggers alerts, misdirecting search efforts and wasting responders’ time.

##### Requirement

Organizations have reliable procedures and accountable personnel for confirming a report’s authenticity, current status, and relevant identifying details before it is treated as actionable.

**Engineering implications:**

**1. Assumption**

Participating child-protection organizations can designate accountable personnel and provide their verified identities and contact details to the service.

**Specification**

The software receives and maintains, for each participating organization, the designated report-verification personnel’s identity, role, and authorized contact details, and exposes these details alongside report review records.

**2. Assumption**

An authoritative organization source can confirm whether a report is genuine and whether the child is still reported missing.

**Specification**

Before distributing a report as actionable, the software receives and records an explicit confirmation from an authorized organization representative that the report is authentic and currently active; it exposes the confirmation source and time with the report.

**3. Assumption**

Organizations can provide reliable, sufficiently current identifying details and updates for each report.

**Specification**

The software receives the identifying details approved by the organization, records their source and last-confirmed time, and transmits updated or withdrawn details to recipients; it exposes the report’s current status and confirmation time.

**4. Assumption**

Organizations can communicate changes in report status, including resolution or withdrawal, to the service in a timely manner.

**Specification**

The software accepts status-change notices from authorized organization contacts, records when they were received, and propagates the revised status to connected recipients so that superseded reports are no longer presented as actionable.

#### Potential Loss

Incorrect identity matching generates a false lead that exposes an uninvolved child to questioning or intervention.

##### Requirement

People handling leads have access to sufficiently specific, current case information and training to corroborate identity before taking action.

**Engineering implications:**

**1. Assumption**

Authorized child-protection organizations can provide authoritative case records, including current identifying details, known aliases, and relevant distinguishing characteristics, and can notify the system when records change or cases close.

**Specification**

The software shall receive and expose to authorized lead handlers the source, last-updated time, current case status, and approved identifying and distinguishing details for each case associated with a lead; it shall identify records whose currency or status cannot be confirmed.

**2. Assumption**

Organizations can designate and authenticate personnel who are authorized to access sensitive case information and handle leads.

**Specification**

The software shall expose case and lead information only to authenticated personnel with organization-assigned authorization, and shall provide handlers a way to confirm which organization and role is associated with a lead.

**3. Assumption**

Organizations can supply and maintain approved guidance and training materials that explain corroboration requirements, limits of visual matching, and escalation steps before intervention.

**Specification**

The software shall present handlers with current, organization-approved corroboration guidance and training materials alongside lead details, including the requirement to obtain independent confirmation before taking action.

**4. Assumption**

Lead handlers can submit verification findings and outcome updates, and organizations can review those updates to correct or close a lead.

**Specification**

The software shall provide a means for handlers to record corroborating evidence, uncertainty, actions, and lead disposition, and shall transmit these updates to the responsible organization with timestamps for review and case maintenance.

#### Potential Loss

A genuine sighting is overlooked or delayed because organizations cannot assess or route the lead promptly.

##### Requirement

Organizations have adequate staffing, clear responsibilities, and timely channels for assessing and escalating credible leads.

**Engineering implications:**

**1. Assumption**

Participating child-protection and missing-person organizations designate reachable staff or duty roles to receive and assess incoming leads, with current contact and responsibility information available to the system.

**Specification**

The software shall expose lead notifications to the designated organization contacts and provide the organization with controls to register and update duty contacts, responsibilities, and availability.

**2. Assumption**

Organizations define escalation criteria and the information they need to judge a lead's credibility and urgency.

**Specification**

The software shall transmit each lead with its available supporting evidence, provenance, time and location, and case reference, and expose organization-configured escalation criteria or urgency categories alongside the lead.

**3. Assumption**

Organizations provide a timely channel for receiving notifications and returning assessments or escalation decisions, and that channel is accessible to the software.

**Specification**

The software shall deliver lead alerts and follow-up updates through the organization's configured channel and receive and expose acknowledgments, assessment status, and escalation outcomes to authorized participants.

**4. Assumption**

Organizations make staffing and response coverage information available and notify the system when lead queues exceed their ability to respond promptly.

**Specification**

The software shall expose lead queue volume, age, and unacknowledged status to designated organizational contacts and accept updates indicating coverage gaps or a need to route leads to an alternate authorized organization.

#### Potential Loss

Conflicting records or unclear case ownership cause a lead to be duplicated, lost, or sent to the wrong authority.

##### Requirement

Participating organizations and authorities have agreed procedures for maintaining authoritative case status, assigning ownership, and coordinating lead handoffs.

**Engineering implications:**

**1. Assumption**

Participating organizations can identify the authority or organization authorized to maintain the authoritative status for each missing-child case, and can provide its current status.

**Specification**

The software receives and records, for each case, the designated authoritative organization and its status updates, and exposes the source and timestamp of the current status to authorized participants.

**2. Assumption**

Participating organizations have identifiable personnel or organizational roles that can be assigned responsibility for each case and for individual leads.

**Specification**

The software receives and stores case and lead ownership assignments, including the responsible organization and contact or role, and makes the current assignment visible to authorized participants.

**3. Assumption**

Organizations agree on the information and acknowledgment needed when a lead is handed from one participant to another.

**Specification**

The software transmits lead handoffs with the agreed case reference, lead details, sending and receiving parties, and required acknowledgment information, and exposes the handoff and its acknowledgment status to authorized participants.

**4. Assumption**

Participants can provide timely corrections or dispute notices when case records, ownership, or lead details conflict.

**Specification**

The software accepts and records correction and dispute notices with their source and time, and exposes unresolved conflicts to the designated case owner and affected participants rather than presenting conflicting information as settled.

### Goal / Value

Protect children’s safety, dignity, and privacy while coordinating public assistance and investigations.

#### Potential Loss

Sensitive case details or a child’s location are disclosed to unauthorized people, increasing exposure to exploitation or harm.

##### Requirement

Access to sensitive case information is limited to authorized people with a legitimate role, with confidentiality obligations and oversight.

**Engineering implications:**

**1. Assumption**

The organizations and relevant authorities can provide a current, authoritative roster of people, their organizational roles, and the cases each role is permitted to access.

**Specification**

The software receives and stores role- and case-scoped authorization records, and exposes sensitive case information only to authenticated users whose active authorization covers that case and information.

**2. Assumption**

Users can be reliably authenticated, and the identity provider or organization can communicate identity status and changes such as revocation to the software.

**Specification**

The software receives authentication and account-status information, binds each sensitive-information request to an authenticated identity, and denies access when identity or authorization status is missing, invalid, or revoked.

**3. Assumption**

Organizations can define confidentiality obligations applicable to authorized roles and communicate acknowledgments or policy updates to users.

**Specification**

Before exposing sensitive case information, the software presents the applicable confidentiality obligations and records the user's acknowledgment; it withholds access when required acknowledgment is absent or expired.

**4. Assumption**

An oversight function is designated and authorized to review access activity, and applicable retention and privacy rules for oversight records are defined.

**Specification**

The software records and makes available to authorized oversight personnel an access log identifying the user, case, information accessed, time, and access outcome, while limiting the log's contents and retention to the defined oversight rules.

#### Potential Loss

An alert remains active after a child is found or a case is withdrawn, leading to continued exposure or unwanted encounters.

##### Requirement

Organizations can communicate status changes promptly, and participating parties have clear responsibilities for stopping outdated outreach.

**Engineering implications:**

**1. Assumption**

Authorized child-protection or missing-person organizations can provide authenticated, case-specific status updates, such as found, withdrawn, or reopened, through a supported communication channel.

**Specification**

The software accepts and records authenticated status updates with the case identifier, status, effective time, and issuing organization, and exposes the recorded status and update time to participating parties.

**2. Assumption**

Participating parties, including alert distributors and dashcam or phone service operators, are identifiable and have reachable channels for receiving case updates and withdrawal notices.

**Specification**

For each case, the software exposes the parties responsible for distributing and stopping outreach, and transmits status changes and explicit stop-outreach notices to those parties through their registered channels, providing delivery or failure status to the organization.

**3. Assumption**

Participating parties can receive and act on timely stop notices, and can report whether related outreach has been halted.

**Specification**

The software provides participating parties a means to acknowledge a stop notice and report outreach-stoppage status, and exposes acknowledgements, outstanding recipients, and unresolved delivery failures to the responsible organization.

**4. Assumption**

Organizations can specify an expected update or review interval and an escalation contact for active cases.

**Specification**

The software records and exposes the organization-provided review interval and escalation contact, and notifies the organization when an active case reaches its review time without a confirming status update.

#### Potential Loss

A child or family experiences stigma, distress, or loss of trust after an inaccurate or unnecessarily broad alert circulates.

##### Requirement

Public-safety outreach is proportionate to the verified case and considers the child’s circumstances, family safety, and potential harms of disclosure.

**Engineering implications:**

**1. Assumption**

Authorized child-protection or missing-person organizations can provide current, verifiable case information, including whether an alert is approved, its scope, and any restrictions on disclosure.

**Specification**

The software receives and presents case status, verification source and time, approved outreach scope, and disclosure restrictions to authorized operators; it does not expose an alert as active outreach when required verification or scope information is absent or expired.

**2. Assumption**

The responsible organization can assess and communicate the child’s circumstances and family-safety risks relevant to public disclosure, and can update that assessment when circumstances change.

**Specification**

The software accepts and stores authorized case-specific disclosure and safety guidance, and makes those restrictions available wherever case details or outreach materials are prepared or shared.

**3. Assumption**

Authorized case personnel can specify intended audiences, geographic reach, channels, and permitted identifying details for each outreach action.

**Specification**

The software presents outreach recipients and disclosure details for authorization, and transmits or exposes only the approved audience, geographic scope, channels, and identifying information for that case.

**4. Assumption**

Authorized organizations can review an alert’s accuracy and necessity and can issue corrections, narrowing instructions, or withdrawal requests.

**Specification**

The software provides authorized personnel with a way to submit corrections, narrow or withdraw outreach, and propagates approved changes to connected recipients and outreach surfaces while exposing the current alert status.

---

## Stakeholder: People captured in dashcam footage

**Type:** indirect

**Why they matter:** Bystanders, passengers, and other road users may have their images or location recorded and analyzed without directly using the feature.

### Goal / Value

Privacy, dignity, and control over personal information, images, and location traces captured incidentally.

#### Potential Loss

A bystander's or passenger's face or other identifying details are exposed through unauthorized access or disclosure of footage.

##### Requirement

Footage and identifying information are protected from unauthorized access, including during transfer, storage, and review.

**Engineering implications:**

**1. Assumption**

The dashcam and any companion phone, vehicle system, or hotspot have a trustworthy way to identify authorized users and services, and that identity information is available to the software when access is requested.

**Specification**

For every request to view, export, or manage footage or identifying information, the software receives the requester identity and authorization context and exposes the data only to an authorized requester; it denies unauthorized requests without returning the protected content.

**2. Assumption**

Transfers between the dashcam and companion devices or services use communication links that support confidentiality and peer authentication, or can be configured to do so.

**Specification**

When transmitting footage or identifying information, the software sends it only over a link that authenticates the intended recipient and protects the content from disclosure in transit; if those protections are unavailable, it does not transmit the content.

**3. Assumption**

The dashcam's storage and any storage used by connected devices or review services provide access controls, and the software can identify the storage locations it uses.

**Specification**

The software stores footage and identifying information only in locations with access controls limited to authorized users or services, and does not expose stored content through unauthenticated interfaces.

**4. Assumption**

People conducting review can be presented with distinct views of footage, and identifying details such as faces, plates, or location traces can be withheld or obscured without preventing the authorized missing-child review.

**Specification**

During review, the software exposes only the footage and identifying details necessary for the authorized missing-child task, and withholds or obscures other identifying details from reviewers who are not authorized to see them.

**5. Assumption**

The software can receive a defined retention or deletion instruction from an authorized user or service, and the relevant storage locations are accessible for applying it.

**Specification**

On an authorized deletion or retention-expiry instruction, the software removes the corresponding footage and identifying information from the storage locations it controls and does not expose it in subsequent review or export.

#### Potential Loss

A person's movements or routines are reconstructed from retained dashcam footage or location-linked records.

##### Requirement

Collection and retention of identifiable footage and location data are limited to what is necessary, with clear retention limits and accountable deletion.

**Engineering implications:**

**1. Assumption**

The system can distinguish footage or records needed for a specific missing-child alert from routine dashcam recordings, and receives alert status or case-closure updates from an authorized source.

**Specification**

The software shall expose to the retention environment only the minimum footage segments and location fields associated with an active alert, and shall remove their identifiable association when the alert is closed or the authorized retention period ends.

**2. Assumption**

A governing policy or authorized configuration provides a defined retention period for each category of footage and location data.

**Specification**

The software shall accept and expose the applicable retention limit for each stored data category, and shall make each item unavailable for retrieval after that limit expires.

**3. Assumption**

The storage environment supports deletion requests and can report whether data under the software's control has been deleted.

**Specification**

The software shall issue deletion requests for expired or no-longer-necessary identifiable footage and location records, and expose deletion status or failures to an authorized oversight interface.

**4. Assumption**

Users and affected people can be given access to clear information about what data is retained, why, and for how long, through an appropriate notice or information channel.

**Specification**

The software shall provide an accessible notice describing the categories and purposes of retained identifiable footage and location data, applicable retention limits, and how deletion is handled.

#### Potential Loss

A person is recorded or analyzed in contexts where they reasonably expect privacy, causing embarrassment or intrusion.

##### Requirement

The system is used only in lawful, appropriately limited contexts, with safeguards for areas and situations where privacy expectations are high.

**Engineering implications:**

**1. Assumption**

Applicable laws and privacy restrictions vary by jurisdiction and may be represented as current, authoritative rules or policy inputs available to the system for its operating location.

**Specification**

The software receives the applicable jurisdiction and current allowed-use rules, and limits capture analysis, retention, and sharing to the purposes and conditions those rules permit; it exposes a status or reason when operation is restricted.

**2. Assumption**

Some locations or situations—such as private property, changing areas, medical settings, or other locally designated sensitive zones—can be identified through reliable user-, vehicle-, or environment-provided zone information.

**Specification**

When the software receives an indication that the dashcam is within a designated sensitive zone, it suppresses missing-child analysis and avoids retaining or transmitting footage or derived person/location data from that zone, exposing only a restriction status if needed.

**3. Assumption**

Vehicle operators or authorized administrators can provide valid, understandable configuration for permitted operating contexts and can update it when circumstances or policy change.

**Specification**

The software accepts and exposes the active operating-context configuration, and applies it to whether footage is analyzed or shared; it does not treat an absent, invalid, or expired configuration as authorization for unrestricted use.

**4. Assumption**

People captured incidentally may be identifiable in raw footage and derived data, and the system can distinguish data needed for a narrowly authorized missing-child search from unrelated footage or person data.

**Specification**

The software exposes, stores, and transmits only footage or derived data needed for an authorized search, limits access and retention to the configured lawful purpose, and provides deletion or expiry behavior for unrelated or no-longer-needed data.

#### Potential Loss

A person's image or location is repurposed for unrelated surveillance, profiling, or commercial use without meaningful authorization.

##### Requirement

Purpose boundaries and oversight prevent use of captured data beyond the missing-child search purpose unless a valid legal basis and appropriate safeguards exist.

**Engineering implications:**

**1. Assumption**

A clearly bounded missing-child search purpose can be expressed in an authorized search request, including what data may be used, for what search, and its validity period.

**Specification**

The software shall receive and retain the authorized search purpose, permitted data categories, scope, and expiry with the search request, and shall expose those limits to any component or service requesting captured data.

**2. Assumption**

Any party seeking to access or reuse captured images, location traces, or derived results can be identified and can provide a stated purpose and, where applicable, evidence of legal authority and safeguards.

**Specification**

Before disclosing captured data or search-derived information, the software shall receive the requester identity, declared purpose, and applicable legal-basis and safeguard information, and shall expose whether the request is within the active search authorization.

**3. Assumption**

The software can control its data outputs to external parties and can distinguish search-related disclosures from requests for unrelated use.

**Specification**

The software shall transmit or expose captured data and search results only for the authorized missing-child search; it shall reject or withhold unrelated-use requests unless the request includes a valid legal basis and appropriate safeguards, and shall communicate the decision to the requester.

**4. Assumption**

An accountable oversight party can receive records of data access and disclosures and can review them under applicable privacy and legal rules.

**Specification**

The software shall produce and retain an access and disclosure record identifying the requester, purpose, data categories, time, authorization or legal basis, safeguards, and decision, and shall make that record available to the designated oversight party.

**5. Assumption**

The authorized search has a defined end point, after which continued retention or availability is not needed for that search unless a valid legal basis and safeguards require it.

**Specification**

At search expiry or closure, the software shall stop making search data available for that purpose and shall expose deletion or retention status; any continued retention or access shall be accompanied by the applicable legal basis, safeguards, and authorized scope.

### Goal / Value

Fair treatment, personal safety, and freedom from harmful consequences of inaccurate identification or association with a missing-child search.

#### Potential Loss

An innocent person is mistakenly identified as the missing child, leading to confrontation, questioning, or detention.

##### Requirement

Any identification used to prompt intervention is independently verified by trained, accountable personnel before action is taken.

**Engineering implications:**

**1. Assumption**

A trained, authorized human reviewer can be reached before any field response, and their identity and authorization can be confirmed by the system.

**Specification**

Before exposing an identification as an actionable alert, the software provides the candidate evidence and relevant context to an authorized reviewer, and records the reviewer’s identity and verification decision; it exposes no intervention prompt unless that decision is affirmative.

**2. Assumption**

Reviewers have access to sufficient, relevant footage or other case information to assess whether the candidate is the missing child, and the material can be presented without unnecessary exposure of unrelated people.

**Specification**

The software presents the reviewer with the source footage or relevant frames, capture time and location, and the case reference, while limiting the presented material to what is needed for verification; it labels the candidate as unverified until a reviewer records a decision.

**3. Assumption**

The organization receiving an intervention prompt can distinguish a verified identification from an unverified candidate and can delay action until verification is documented.

**Specification**

The software transmits intervention prompts only with a recorded positive verification, and includes the reviewer’s authorization and decision time; it does not transmit an actionable prompt for pending, rejected, or unavailable reviews.

**4. Assumption**

A reliable record can be retained and accessed by accountable personnel for audit, correction, or investigation of an identification and subsequent action.

**Specification**

The software stores and exposes an auditable record linking the candidate, evidence shown, reviewer identity, verification outcome and time, and any intervention prompt issued, to support review of whether action followed independent verification.

#### Potential Loss

A person is treated as suspicious or targeted because their appearance, behavior, or location is associated with a search alert.

##### Requirement

Search procedures protect people from adverse treatment based solely on automated matches or incidental proximity.

**Engineering implications:**

**1. Assumption**

An automated match or proximity indication is uncertain and can be incorrect, and people exposed to the search may not know that the system generated it.

**Specification**

The software labels and presents a match or proximity result as an unverified lead, communicates its uncertainty and relevant limitations to authorized recipients, and does not expose it as a conclusion that a person is the missing child or is suspicious.

**2. Assumption**

A designated human reviewer with authority to evaluate search leads is available before any consequential intervention is made.

**Specification**

The software routes candidate leads to an authorized human reviewer and withholds any alert or output that recommends, initiates, or represents adverse action against a person until the reviewer has independently assessed the lead.

**3. Assumption**

Reviewers and responders can distinguish an actionable, corroborated identification from incidental resemblance or location overlap when given suitable context.

**Specification**

The software provides reviewers with the permitted supporting context and provenance for a lead, including the basis and time of the observed match or proximity, and requires an independently corroborated determination before communicating a lead as actionable.

**4. Assumption**

Search information can be retained or shared beyond its intended purpose unless access and lifecycle limits are communicated and enforced at the system boundary.

**Specification**

The software restricts search-related footage, candidate data, and alerts to authorized recipients and the stated search purpose, and exposes retention and deletion controls so that data is not retained or redistributed after the authorized need ends.

#### Potential Loss

A person’s sensitive location or presence is disclosed to others, exposing them to harassment, retaliation, or physical danger.

##### Requirement

Access to location-linked information is restricted to authorized parties with a legitimate need, and disclosures are subject to oversight.

**Engineering implications:**

**1. Assumption**

A trusted authority or service can provide verifiable identities, roles, and current authorization status for people requesting location-linked information.

**Specification**

The software receives and validates requester identity, role, and authorization status, and exposes location-linked information only to requesters whose authorization and stated legitimate need are confirmed.

**2. Assumption**

The environment defines which purposes and data fields are necessary for each authorized role, and applicable disclosure limits.

**Specification**

For each request, the software receives the declared purpose and requested data scope, and returns only the location-linked fields permitted for that role and purpose; it denies requests outside those limits.

**3. Assumption**

An oversight authority is designated, can access disclosure records, and can protect those records from unauthorized alteration or access.

**Specification**

The software records each disclosure and denial with requester, purpose, data scope, time, and recipient, and exposes these records to designated oversight personnel.

**4. Assumption**

Secure communication channels and recipient endpoints are available for authorized parties and oversight personnel.

**Specification**

The software transmits approved location-linked information only to the verified authorized recipient over an authenticated protected channel, and does not expose it through public or unverified interfaces.

---

## Stakeholder: Vehicle passengers

**Type:** indirect

**Why they matter:** Passengers may be recorded during trips and could be affected by data collection, retention, or sharing even when they did not choose the system.

### Goal / Value

Protect passengers’ privacy, dignity, and control over their personal information while traveling.

#### Potential Loss

A passenger’s face, voice, or other identifying details are captured without their awareness, exposing them to unwanted surveillance.

##### Requirement

Passengers have reasonable notice that recording and missing-child detection may occur in the vehicle.

**Engineering implications:**

**1. Assumption**

Passengers can see or hear an in-vehicle notice before or when they enter the vehicle, and the notice remains accessible during the trip.

**Specification**

The software exposes a clear, concise notice in an in-vehicle display or audio interface before recording or missing-child detection begins, stating that recording and detection may occur and identifying the relevant data types at a high level.

**2. Assumption**

The vehicle operator or service provider can provide accurate, current information about whether recording and missing-child detection are enabled and when they operate.

**Specification**

The software receives the current recording and detection status and exposes that status to passengers through the in-vehicle notice, including any changes during the trip.

**3. Assumption**

Passengers may board after initial notices have been displayed, or may need to review the notice while traveling.

**Specification**

The software keeps the notice available through an accessible in-vehicle interface for the duration of the trip, so passengers can review the recording and detection information after boarding.

**4. Assumption**

Passengers can use a provided interface to request more information about data handling, and the system has approved information available to present.

**Specification**

The software exposes a means for passengers to access concise information about what identifying data may be captured, whether it is stored or transmitted, and where to find further privacy details.

##### Requirement

Recording practices respect passengers’ reasonable expectations of privacy and applicable consent requirements.

**Engineering implications:**

**1. Assumption**

Passengers can be informed before recording begins through a visible, audible, or connected interface, and can provide or withhold consent where consent is required.

**Specification**

Before capturing or retaining passenger-identifiable audio or video, the software shall expose a clear recording notice and obtain any required consent through an available interface; when consent is absent or declined, it shall not capture or retain that passenger-identifiable data, except where an applicable legal exception is explicitly represented.

**2. Assumption**

The vehicle environment provides a reliable way to indicate recording state, such as a visible indicator or an in-cabin display accessible to passengers.

**Specification**

While passenger-identifiable recording is active, the software shall expose an unambiguous recording-status indication to occupants, and shall expose a status change when recording pauses or resumes.

**3. Assumption**

Passengers have a usable means to request that recording stop or that their identifying data not be retained, and the system can distinguish such requests from ordinary input.

**Specification**

The software shall receive passenger privacy-control requests through the provided interface and, where permitted by law and system function, stop passenger-identifiable capture or prevent the requested data from being retained or transmitted; it shall expose the outcome of the request.

**4. Assumption**

The system can separate footage needed for an external missing-child search from passenger-identifiable cabin content, and any necessary recipients or retention limits are defined by policy or law.

**Specification**

When sharing or retaining data for a missing-child search, the software shall transmit or store only the passenger-identifiable information authorized for that purpose, and shall expose to passengers the data categories, recipients, and retention conditions applicable to that handling.

#### Potential Loss

Sensitive images or audio of passengers are retained longer than needed, creating risk of later exposure or misuse.

##### Requirement

Personal data is retained only for a defined, justified period, with deletion or secure disposal when that period ends.

**Engineering implications:**

**1. Assumption**

The organization operating the missing-child detection service can define and justify retention periods for each category of personal data and processing purpose, including any applicable legal or operational limits.

**Specification**

The software receives and stores an approved retention period and purpose for each category of personal data it retains, and exposes the applicable period and purpose in its data-handling notice or user-facing information.

**2. Assumption**

The dashcam and any connected phone, vehicle, hotspot, or service expose the personal-data records they hold, along with enough metadata to determine each record's category, purpose, and retention deadline.

**Specification**

For every personal-data item the software stores or transmits, it records its category, purpose, and retention deadline, and makes this inventory available to authorized privacy or service-management interfaces.

**3. Assumption**

The device and any connected systems that receive personal data remain powered or reconnect often enough to process deletion requests and scheduled expiry; storage media also support deletion or secure disposal.

**Specification**

When an item's retention period ends, the software deletes or securely disposes of that item from each storage location it controls, and sends deletion instructions to connected recipients holding a copy.

**4. Assumption**

Connected recipients can acknowledge deletion or report whether copies remain, and the operator can provide an authorized channel for handling recipients that cannot be reached.

**Specification**

The software exposes deletion status and any unconfirmed copies to an authorized management interface, and does not represent disposal as complete until controlled recipients confirm deletion or the remaining copy is otherwise accounted for.

#### Potential Loss

A passenger’s footage or identifying information is accessed or shared by unauthorized people or organizations.

##### Requirement

Recorded personal information is protected against unauthorized access and disclosure throughout storage and transfer.

**Engineering implications:**

**1. Assumption**

The dashcam’s storage and connected devices (such as a phone or vehicle system) can be identified as trusted or untrusted endpoints, and the software can determine the intended recipient for a transfer.

**Specification**

The software exposes recorded personal information only to authenticated, authorized users and sends it only to an identified, authorized recipient; it rejects access or transfer requests that lack valid authorization.

**2. Assumption**

The dashcam and its paired receiving devices support a means of protecting information while it is stored and while it traverses USB, Bluetooth, or Wi-Fi links.

**Specification**

The software stores recorded personal information in protected form and transmits it in protected form over supported links, so the information is not exposed in readable form to unauthorized parties during storage or transfer.

**3. Assumption**

Users can provide or change privacy choices, and the dashcam can receive and retain those choices before recording or transferring personal information.

**Specification**

The software receives and applies passenger or vehicle-user privacy choices to the collection, retention, and sharing of recorded personal information, and exposes transfer controls or status so users can determine whether information is being shared.

**4. Assumption**

The dashcam can identify when stored personal information is no longer needed under applicable retention rules, and storage deletion is available to the software.

**Specification**

The software limits stored personal information to the configured retention period and exposes no longer-retained information for retrieval or transfer after it is deleted.

#### Potential Loss

A passenger is falsely associated with a missing-child sighting, causing suspicion, distress, or reputational harm.

##### Requirement

Reports based on footage are sufficiently reliable and distinguish confirmed facts from uncertain identification.

**Engineering implications:**

**1. Assumption**

Dashcam footage may be blurred, obstructed, poorly lit, or otherwise insufficient to establish a child's identity or the circumstances of a sighting.

**Specification**

For each reported sighting, expose the observed time and location, the footage-derived observations, and an explicit uncertainty or insufficient-evidence status whenever the available footage does not support a confident identification; do not present an uncertain identity as confirmed.

**2. Assumption**

A report recipient can distinguish direct observations from identity claims and other interpretations when these are labeled clearly.

**Specification**

Transmit reports with separate, clearly labeled fields for directly observed facts (such as clothing, approximate age, and direction of travel) and any possible identity match, marking the latter as unconfirmed unless independently confirmed.

**3. Assumption**

The system may receive missing-child reference information that is incomplete, outdated, or inconsistent with a child's current appearance.

**Specification**

Expose the reference information and its applicable date or version alongside any comparison result, and identify missing, stale, or conflicting reference data as a limitation rather than asserting a confirmed match.

**4. Assumption**

People reviewing reports can provide confirmation or correction through an available review channel before an identification is treated as confirmed.

**Specification**

Keep identification status visible to authorized reviewers and recipients, and transmit a status change to confirmed only when the designated confirmation is received; retain the prior unconfirmed status when no confirmation is available.

##### Requirement

People named or implicated in a report have access to fair procedures for correcting errors and contesting allegations.

**Engineering implications:**

**1. Assumption**

A person implicated in a report can be identified or contacted through a trusted channel without exposing their identity to unrelated users.

**Specification**

The software exposes a private notice to an implicated person, through an available contact channel, identifying the report and explaining how to request correction or contest the allegation.

**2. Assumption**

A designated, appropriately authorized reviewer or appeal body is available to receive and assess challenges.

**Specification**

The software accepts and securely transmits a challenge, supporting information, and the referenced report to the authorized reviewer, and provides the person with a receipt and status updates.

**3. Assumption**

The report and associated evidence can be referenced and retained for a reasonable period under applicable privacy and retention rules.

**Specification**

The software provides the person and authorized reviewer access to the relevant report details and evidence needed to assess the allegation, while restricting access to authorized parties and indicating any redactions or unavailable material.

**4. Assumption**

There is an established process for recording outcomes and correcting downstream copies or uses of inaccurate reports.

**Specification**

The software exposes the review outcome and any correction to the implicated person, updates the report status, and transmits the correction or retraction to recipients or systems that received the original report.

### Goal / Value

Remain physically safe and avoid undue disruption or unfair treatment resulting from the system’s operation.

#### Potential Loss

A driver or passenger is distracted or alarmed by an alert while the vehicle is moving, increasing the risk of a collision.

##### Requirement

Vehicle occupants are not required to interact with system alerts while the vehicle is in motion.

**Engineering implications:**

**1. Assumption**

The vehicle can provide a sufficiently timely and reliable indication of whether it is moving, such as vehicle-speed or motion status.

**Specification**

The software receives the vehicle's motion status and, while that status indicates motion, does not present an alert that requires an occupant response; it defers the required interaction until the vehicle is stationary.

**2. Assumption**

The system has an output channel for alerts that can be configured to avoid demanding attention from occupants, and occupants are not required to acknowledge or dismiss a passive notification.

**Specification**

While the vehicle is in motion, the software exposes detection information only through non-interactive notifications that require no acknowledgement, dismissal, or other occupant input.

**3. Assumption**

The vehicle provides a reliable way to determine when it is stationary, and occupants can access the system or its alerts after stopping.

**Specification**

The software retains any alert requiring occupant review and makes it available for interaction only after receiving an indication that the vehicle is stationary.

**4. Assumption**

The vehicle's control interface can distinguish driver controls from passenger-accessible controls, or otherwise indicate whether an interaction would require the driver to respond.

**Specification**

While the vehicle is moving, the software does not expose alert actions through controls that require driver input; any required response is made available through a passenger-accessible interface or deferred until the vehicle is stationary.

##### Requirement

Safety-critical driving tasks take priority over detection and reporting activities.

**Engineering implications:**

**1. Assumption**

The vehicle or dashcam can provide a sufficiently reliable indication of whether the vehicle is moving and, where available, whether safety-critical driving conditions are active (such as an active warning or maneuver).

**Specification**

The software receives vehicle-motion and available driving-safety status signals, and suppresses or defers nonurgent detection and reporting outputs while the vehicle is moving or a safety-critical condition is active.

**2. Assumption**

The dashcam's alert channels (such as display, audio, and connected-device notifications) can be controlled or scheduled by the software.

**Specification**

While driving, the software exposes no audible, visual, or connected-device notification that requires immediate passenger or driver attention for routine detection or reporting; it queues such notifications for a safe time, and uses only an agreed non-distracting indication if one is available.

**3. Assumption**

A connected phone or service can receive queued reports later, and the system has a way to identify a safe reporting opportunity, such as when the vehicle is parked or the trip has ended.

**Specification**

The software stores pending detection reports locally and transmits or presents them only after receiving a parked/trip-ended indication, unless the report is explicitly classified under an externally defined emergency policy.

**4. Assumption**

The vehicle provides a reliable means to distinguish urgent safety warnings from ordinary detection results, and the system's reporting policy defines which events qualify as urgent.

**Specification**

The software exposes an urgent alert during motion only for events identified by the supplied policy as requiring immediate action; it routes other detection results to deferred reporting and does not ask occupants to interact while the vehicle is moving.

#### Potential Loss

A passenger’s whereabouts or travel patterns are inferred from footage and used to track or target them.

##### Requirement

Access to location-linked footage and travel information is limited to legitimate, necessary purposes.

**Engineering implications:**

**1. Assumption**

A recognized missing-child alert or other defined response trigger can be made available to the system, and authorized responders and permitted purposes can be identified and verified.

**Specification**

The software accepts footage or travel-information requests only when they include a verifiable response trigger, requester identity, and purpose, and exposes matching location-linked information only to requesters authorized for that purpose.

**2. Assumption**

The device and any connected phone, vehicle, or service can provide reliable controls for user consent and privacy preferences, and those controls are observable to the software.

**Specification**

The software receives the applicable consent and privacy settings and does not collect, retain, or share location-linked footage or travel information beyond what those settings and an authorized missing-child response require.

**3. Assumption**

The system can distinguish location-linked records from other footage and can identify when records are no longer needed for an active authorized response.

**Specification**

The software labels and stores location-linked footage and travel information as purpose-limited records, makes them accessible only for the active authorized response, and deletes or de-identifies them when that purpose ends or the permitted retention period expires.

**4. Assumption**

Recipients and communication channels can be identified, and their authorization and ability to protect transmitted information can be checked.

**Specification**

Before transmitting location-linked footage or travel information, the software exposes it only to a verified authorized recipient over an approved channel, and provides no broader disclosure in user-facing interfaces or exports.

##### Requirement

Passengers are protected from discriminatory, retaliatory, or otherwise improper use of information derived from the system.

**Engineering implications:**

**1. Assumption**

Organizations and individuals receiving system-derived information can be identified, and their roles and purposes for access can be stated and made available to the software.

**Specification**

The software shall expose system-derived information only to authenticated recipients whose declared role and purpose are authorized for the missing-child search, and shall deny requests for unrelated tracking, profiling, or targeting.

**2. Assumption**

The service operator and receiving authorities can accept restrictions on onward use and sharing of information derived from the system.

**Specification**

When transmitting information, the software shall accompany it with permitted-use and onward-disclosure restrictions, and shall not provide exports or interfaces that enable recipients to repurpose it for passenger tracking or targeting.

**3. Assumption**

The software can distinguish information necessary to report a possible child sighting from incidental passenger-identifying or travel-pattern information.

**Specification**

The software shall transmit or expose only the minimum information needed to assess and follow up a possible sighting, and shall not include passenger identities, unrelated occupants, or passenger travel histories.

**4. Assumption**

A responsible operator or oversight authority is available to receive and investigate reports of access or use that may violate the stated purposes.

**Specification**

The software shall make records of access, disclosures, and denied access available to the designated oversight authority, including recipient, time, and stated purpose, without exposing those records to unauthorized users.

**5. Assumption**

The service can define a retention period appropriate to the missing-child search and can receive notice when the search or a submitted sighting is no longer active.

**Specification**

The software shall expose or retain system-derived information only for the applicable search period, then delete it or make it unavailable for further use, including use to infer passenger whereabouts or travel patterns.

---

## Stakeholder: Dashcam and vehicle manufacturers

**Type:** direct

**Why they matter:** They integrate and maintain on-device processing, connectivity, power use, and user controls, and bear product-support and liability risks.

### Goal / Value

Deliver a reliable, safe, and supportable product that integrates missing-child detection without compromising core dashcam and vehicle functions.

#### Potential Loss

Detection processing drains the vehicle battery or disrupts dashcam recording and other essential vehicle electronics.

##### Requirement

Vehicle electrical systems have sufficient protected power capacity and stable operation across expected operating conditions.

**Engineering implications:**

**1. Assumption**

The vehicle provides the dashcam with a supported, protected power connection whose available capacity and operating state can be measured or reported to the dashcam.

**Specification**

The software receives the available-power capacity and power-state status from the vehicle interface and exposes whether missing-child detection is permitted under the reported limits.

**2. Assumption**

The dashcam or vehicle exposes reliable indicators of supply voltage, brownout conditions, and ignition or engine state across expected operating conditions.

**Specification**

The software receives voltage and vehicle-state alerts and reports detection-service availability or suspension status to the vehicle and dashcam interfaces when those conditions fall outside supported limits.

**3. Assumption**

The dashcam platform provides observable recording-health and essential-electronics status signals, and accepts service-priority or load-shedding requests.

**Specification**

The software exposes its detection workload state and responds to recording or electronics health and priority signals by reporting when detection is reduced or unavailable, without claiming service availability when the platform reports a conflict.

**4. Assumption**

The vehicle manufacturer defines validated electrical operating limits and safe operating modes for the dashcam connection, including permitted behavior when parked and during startup or shutdown.

**Specification**

The software receives the applicable electrical limits and operating-mode status and exposes its power demand and detection-service state in a form that allows the vehicle interface to verify operation remains within those limits.

##### Requirement

Dashcam recording and essential vehicle functions remain available despite variable detection workloads.

**Engineering implications:**

**1. Assumption**

The vehicle exposes a reliable indication of available power or a low-voltage/battery-protection state to the dashcam software.

**Specification**

The software receives the vehicle's available-power or battery-protection status and exposes detection activity as suspended or reduced when that status indicates that continued processing could threaten vehicle power availability; it leaves recording and essential vehicle functions available.

**2. Assumption**

The dashcam platform exposes recording status and resource availability, such as processor, memory, and storage pressure, to the detection software.

**Specification**

The software receives recording status and resource-availability information and exposes detection workload as limited or paused when required to preserve ongoing recording and essential dashcam services.

**3. Assumption**

The vehicle and dashcam provide defined interfaces for identifying essential vehicle functions and communicating faults or degraded operating states.

**Specification**

The software exposes its detection operating state and faults through the supported vehicle/dashcam interface, and does not send detection-related commands or data that disable or interfere with identified essential vehicle functions.

**4. Assumption**

The vehicle power and dashcam recording interfaces can accept explicit requests to suspend or resume optional detection processing.

**Specification**

The software produces suspend/resume requests for detection processing in response to reported power or recording constraints, and exposes whether detection is active, reduced, or suspended while recording and essential functions remain available.

#### Potential Loss

Variable processing capacity across dashcam models causes missed detections, excessive latency, overheating, or device failure.

##### Requirement

Supported hardware models have documented compute, thermal, and memory capabilities adequate for their assigned detection workload.

**Engineering implications:**

**1. Assumption**

Manufacturers can provide authoritative, model- and configuration-specific specifications or measurements for available compute resources, including relevant accelerators and operating limits.

**Specification**

For each supported hardware model and configuration, the software exposes and stores a model-specific compute capability profile, with its source or validation status, for assignment of a detection workload.

**2. Assumption**

The device’s thermal sensors and operating environment provide temperature and thermal-limit information that can be read reliably while the detection workload is active.

**Specification**

For each supported model, the software records and exposes the applicable thermal operating limits and the thermal capability evidence used to qualify its assigned workload.

**3. Assumption**

The device firmware or manufacturer supplies accurate information about memory available to the detection feature under supported operating conditions.

**Specification**

For each supported model and configuration, the software exposes and stores the memory capacity/reserve profile relevant to detection, and identifies the workload assignment qualified against that profile.

**4. Assumption**

Model identity and hardware configuration can be determined unambiguously at runtime, and supported-model qualification data can be maintained and distributed to the device.

**Specification**

The software receives the device model/configuration identity, associates it with a versioned capability record, and exposes that record and its assigned workload designation to authorized support or diagnostic interfaces.

##### Requirement

Devices operate within manufacturer-defined thermal and electrical limits under expected ambient conditions.

**Engineering implications:**

**1. Assumption**

Each supported dashcam model has manufacturer-defined thermal and electrical operating limits, including any required safety margin, available to the software through configuration or a model profile.

**Specification**

The software receives the applicable model limits and exposes operational status or a fault indication when operation is outside those limits, rather than reporting the device as operating normally.

**2. Assumption**

The dashcam or vehicle provides sufficiently current measurements or status signals for temperature, supply voltage, and relevant power conditions, with defined units and validity indicators.

**Specification**

The software consumes the available temperature and electrical-status signals and adjusts or suspends missing-child detection activity when those signals indicate the applicable limits are reached or exceeded.

**3. Assumption**

Expected ambient conditions for each deployment are bounded and documented, and the device's available environmental sensors or platform status can indicate conditions relevant to those bounds.

**Specification**

The software receives ambient-condition information when available and communicates a degraded or unavailable detection status if those conditions fall outside the supported operating envelope.

**4. Assumption**

The vehicle power interface can report power interruptions or transitions, and the dashcam can expose a controlled status to other vehicle or dashcam functions.

**Specification**

The software reports its power-related operating state to the host interface and stops or limits detection processing during power conditions that could breach electrical limits or disrupt core vehicle functions.

#### Potential Loss

Inaccurate detections or missed matches lead to customer complaints, costly support incidents, or reputational damage.

##### Requirement

Detection performance, operating limitations, and uncertainty are characterized for the environments in which the product is offered.

**Engineering implications:**

**1. Assumption**

The offered product configurations and intended operating environments can be identified, including camera/sensor characteristics, mounting, vehicle types, and relevant weather, lighting, and road conditions.

**Specification**

For each offered product configuration, the software exposes a supported-environment profile identifying applicable vehicle and camera configurations and the environmental conditions under which missing-child detection performance is characterized.

**2. Assumption**

Representative, appropriately labeled footage and ground-truth match outcomes can be obtained for the supported environments, including varied child appearances and realistic non-match cases.

**Specification**

The software provides performance results for each characterized environment, including detection and missed-match rates, the evaluation population and conditions, and the time or version to which the results apply.

**3. Assumption**

Environmental conditions that materially affect detection, such as low visibility or obstructed views, can be represented by observable input data or condition categories.

**Specification**

When presenting a detection result, the software exposes the applicable operating limitations and any detected condition that places the current input outside the characterized conditions or makes the result less reliable.

**4. Assumption**

A match score or other output can be calibrated against known outcomes, and recipients can interpret a defined uncertainty representation.

**Specification**

For each reported candidate match, the software exposes a confidence or uncertainty indication and the corresponding interpretation or limits, rather than presenting an unqualified match assertion.

**5. Assumption**

Manufacturers and support personnel have an authorized means to receive product characterization information, and applicable privacy and data-retention constraints are defined.

**Specification**

The software makes the current characterization and limitations available to authorized manufacturer or support interfaces, including the model/version and relevant operating context, without exposing footage or personal data beyond the configured privacy and retention rules.

##### Requirement

Users and support personnel have clear, accessible information about system limitations and appropriate expectations.

**Engineering implications:**

**1. Assumption**

Users and support personnel can access an in-product interface, documentation, or support materials in a language and format they can understand.

**Specification**

The software exposes concise, accessible information describing the system’s intended use, known limitations, and appropriate expectations through the user interface and support-facing materials available to authorized support personnel.

**2. Assumption**

Relevant operating conditions and input-quality factors—such as camera visibility, lighting, image quality, and connectivity—can be identified or described to users and support personnel.

**Specification**

The software exposes the conditions that may affect detection and matching, and when observable, reports relevant conditions affecting a particular operation, so users and support personnel can interpret results appropriately.

**3. Assumption**

The system can distinguish a potential match or detection result from a confirmed identification, and can communicate that distinction to the user.

**Specification**

The software presents detection results with explicit uncertainty and states that a potential match is not a confirmed identification; it does not expose results as definitive identity claims.

**4. Assumption**

Support personnel have an authorized means to access information about reported results and system limitations without receiving unnecessary personal or footage data.

**Specification**

The software makes support-relevant status and limitation information available through an authorized support interface, while exposing only the information needed to explain system behavior and avoiding unnecessary disclosure of footage or personal data.

#### Potential Loss

Unclear responsibility among manufacturers, service operators, and authorities exposes manufacturers to legal or contractual liability.

##### Requirement

Roles, responsibilities, and liability boundaries among participating organizations are established and communicated.

**Engineering implications:**

**1. Assumption**

Participating organizations and their authorized representatives can be identified, and each organization can provide an authoritative description of its role, responsibilities, and liability boundaries.

**Specification**

The software shall receive and retain organization identities, authorized representative details, and their approved role, responsibility, and liability-boundary statements for the missing-child detection service.

**2. Assumption**

Organizations can agree on a controlled, versioned set of responsibility terms and communicate when those terms are approved or changed.

**Specification**

The software shall expose the current approved responsibility terms and their version and effective date to authorized participating organizations, and transmit updates to their designated contacts.

**3. Assumption**

Manufacturers, service operators, and relevant authorities have designated channels and contacts through which operational responsibilities and escalation boundaries can be communicated.

**Specification**

The software shall provide authorized users with the designated contact and escalation information for each participating organization, and transmit that information to other authorized organizations when applicable.

**4. Assumption**

Organizations require an auditable record of which responsibility terms were communicated, to whom, and when, to support contractual and liability inquiries.

**Specification**

The software shall record and make available to authorized parties the responsibility-term version communicated, recipient organization or contact, and communication timestamp.

##### Requirement

Applicable legal, safety, and data-protection obligations for each operating jurisdiction are understood and met.

**Engineering implications:**

**1. Assumption**

The jurisdiction in which the dashcam is operating can be identified reliably, either from a trusted vehicle/location signal or explicit user or fleet configuration, and changes can be detected before relevant data handling occurs.

**Specification**

The software receives the applicable jurisdiction identifier and exposes the active jurisdiction and any unresolved/uncertain status to the operator or vehicle integration; it does not initiate jurisdiction-dependent detection, storage, or transmission while the jurisdiction is unresolved.

**2. Assumption**

Manufacturers can obtain authoritative, current legal and regulatory requirements for each supported jurisdiction, including rules governing recording, child-related data, retention, disclosure, and cross-border transfer.

**Specification**

The software accepts and identifies the approved jurisdiction-specific policy configuration, exposes its version and effective jurisdiction, and signals when a required policy is absent, expired, or unsupported so the feature can be disabled or restricted.

**3. Assumption**

The manufacturer, service operator, and relevant authorities provide documented role assignments, contact points, and permitted purposes for collecting, reviewing, retaining, and disclosing detection data.

**Specification**

The software exposes the configured responsible-party and escalation information, and labels each alert or data export with the applicable purpose and authorized recipient context; it rejects or flags requests whose recipient or purpose is not configured as permitted.

**4. Assumption**

The vehicle and dashcam operating environment provides a means for authorized personnel to receive safety, privacy, and compliance notices, and can report when the feature is unavailable or operating in a restricted mode.

**Specification**

The software presents jurisdiction-specific operating restrictions, consent or notice requirements, and feature-status warnings through the available vehicle or dashcam interface, and reports relevant status to the authorized support interface without exposing unrelated footage.

### Goal / Value

Preserve customer trust and comply with privacy, security, and cost expectations while enabling useful connectivity and user control.

#### Potential Loss

Unauthorized access, disclosure, or retention of footage or information about a missing child causes privacy harm and regulatory penalties.

##### Requirement

Personal and sensitive data are protected throughout collection, transfer, access, and retention.

**Engineering implications:**

**1. Assumption**

The camera, companion phone, vehicle, and any hotspot or backend expose identifiable interfaces and can indicate connection state and the destination or recipient of a transfer.

**Specification**

The software shall expose or transmit personal or sensitive data only to the configured, authorized recipient over an available connection, and shall not send it to other nearby devices or destinations.

**2. Assumption**

The device has a usable source of time and storage that can represent data-retention limits and whether a case or user-authorized purpose remains active.

**Specification**

The software shall store collected footage and case-related data with an associated retention limit, expose the applicable retention status to the user or authorized operator, and delete or stop retaining the data when that limit or purpose expires.

**3. Assumption**

Users and authorized operators can be identified to the software through an available account, device-pairing, or vehicle-access interface.

**Specification**

The software shall expose footage, child-identifying information, and privacy settings only to authenticated users or operators whose interface access is authorized for that data.

**4. Assumption**

The software can distinguish data categories and receive user or system settings that specify which collection and sharing activities are enabled.

**Specification**

The software shall collect and transmit only the personal or sensitive data and footage needed for enabled missing-child detection functions, and shall expose the collection and sharing choices through the user interface.

**5. Assumption**

Connected endpoints can report whether a transfer channel is available and whether a transfer completed or failed.

**Specification**

The software shall transmit sensitive data only over a channel reported as available for the intended recipient; when no such channel is available, it shall not expose the data through an alternate route and shall report transfer status without disclosing the sensitive content.

##### Requirement

Data collection and retention are limited to purposes and periods that are publicly disclosed and legally permitted.

**Engineering implications:**

**1. Assumption**

Applicable privacy laws and regulatory requirements for each deployment region, including permitted purposes and retention limits, are identifiable and kept current by the manufacturer or service operator.

**Specification**

The software receives the applicable jurisdiction, permitted processing purposes, and retention limits, and exposes or uses these constraints to limit collection, use, and retention of footage and child-related information to those limits.

**2. Assumption**

Users can access accurate, current public disclosures describing what data is collected, for which purposes, and for how long, before enabling the relevant feature.

**Specification**

Before feature activation, the software presents the applicable collection purposes and retention periods to the user and exposes the same disclosures through the product's user-facing information interface.

**3. Assumption**

The dashcam or connected service has a reliable means to determine when stored footage or related information reaches its applicable retention deadline.

**Specification**

The software stores data with its applicable retention deadline and, when that deadline is reached, removes the data from accessible storage and does not continue exposing or transmitting it.

**4. Assumption**

Users can change feature settings or withdraw consent through an available dashcam or companion-device interface.

**Specification**

The software receives the user's purpose-selection or withdrawal instruction and exposes a resulting state in which collection and retention for the declined or withdrawn purpose stop, subject to legally required retention.

**5. Assumption**

Any connected recipient or storage provider can receive and honor purpose and retention constraints supplied by the dashcam software.

**Specification**

When transmitting footage or related information to a phone, vehicle, hotspot, or service, the software communicates the authorized purpose and applicable retention limit, and exposes only data needed for that purpose.

#### Potential Loss

Unexpected mobile-data use, connectivity charges, or power consumption prompts customer backlash and product returns.

##### Requirement

Connectivity, data-volume, and power costs are predictable and acceptable to customers under ordinary use.

**Engineering implications:**

**1. Assumption**

The vehicle supplies a sufficiently reliable signal for ignition/accessory state and, where available, battery or charging status, so software can distinguish ordinary driving from parked operation.

**Specification**

The software receives and uses the available vehicle power-state information to expose to the user when connectivity or detection may consume vehicle power, and to limit or suspend nonessential operation according to user-configured power preferences.

**2. Assumption**

The phone or hotspot operating system exposes connectivity state and, where supported, mobile-data usage or metered-network status to the dashcam software.

**Specification**

The software receives network and metering status and exposes whether uploads or other network transfers are enabled, the expected data-use category or estimate, and controls to disable or restrict transfers on metered connections.

**3. Assumption**

Users can access a setup interface on the dashcam or its paired phone before or during ordinary use.

**Specification**

The software presents user-selectable connectivity and data-use settings, including upload enablement and limits, and stores the selected preferences so they remain visible and apply across ordinary operating sessions.

**4. Assumption**

The system can measure or estimate the volume of data it transmits and can identify applicable connectivity charges only when the carrier or connected device provides that information.

**Specification**

The software exposes measured or estimated data usage over a stated period and, when charge information is available, an estimated cost; it labels unavailable or uncertain charge estimates rather than implying exact billing.

##### Requirement

Customers can understand and control whether their devices use available phone, vehicle, or hotspot connections.

**Engineering implications:**

**1. Assumption**

Customers can access a dashcam or companion-app interface that presents device settings and is usable before or during connection setup.

**Specification**

The software exposes a connection-control setting for each supported phone, vehicle, or hotspot connection, showing whether it is enabled and allowing the customer to enable or disable its use.

**2. Assumption**

The device or connection provider can report when a phone, vehicle, or hotspot connection becomes available, along with enough identifying information for the customer to distinguish it.

**Specification**

The software presents the available connection type and identifiable network or device information before using that connection, and exposes the choice to accept or decline it.

**3. Assumption**

The software can observe data transfer and power use attributable to its connectivity features, or obtain estimates from the operating environment.

**Specification**

The software exposes connection-related data-use and power-use estimates or usage totals, including the connection they relate to, so customers can assess likely costs and energy impact.

**4. Assumption**

Customers can provide preferences through the interface, and the device can retain settings across restarts and connection changes.

**Specification**

The software stores and exposes the customer's selected connection permissions and limits, and applies those preferences when deciding whether to use an available connection.

**5. Assumption**

The device can detect when use of a connection is about to incur charges or exceed a customer-configured threshold, either from provider information or configured estimates.

**Specification**

Before initiating or continuing connectivity likely to incur charges or exceed a configured data-use limit, the software exposes a warning and requests authorization, unless the customer has explicitly configured a corresponding automatic-use rule.

#### Potential Loss

Users cannot readily disable, pause, or understand the feature, undermining trust and creating complaints or noncompliance.

##### Requirement

Users have clear notice of when the feature is active, what information it uses, and how to change participation settings.

**Engineering implications:**

**1. Assumption**

The vehicle or dashcam has a user-visible interface, such as a display, companion-phone app, or accessible settings page, through which notices and controls can be presented.

**Specification**

The software exposes an activation indicator and a notice describing the feature’s purpose and current operating state through the available user interface whenever the feature is active.

**2. Assumption**

The software can identify the categories of information the feature uses and whether any information is retained or sent outside the dashcam.

**Specification**

The software presents users with an accessible description of the information categories used, and discloses whether and to whom information is stored or transmitted, before participation is enabled and while settings can be reviewed.

**3. Assumption**

Users can interact with a supported interface to change feature settings, and the vehicle provides the software with those input events.

**Specification**

The software exposes controls for enabling, disabling, or pausing participation and receives the user's selection through the supported interface; it communicates the resulting setting and effective status to the user.

**4. Assumption**

Feature status and user settings can be made available across the dashcam and any companion interface used to manage the feature.

**Specification**

The software exposes the current participation setting and active/paused state consistently on the dashcam and connected management interface, and updates the displayed state when a setting change takes effect.

##### Requirement

User controls are accessible and understandable across supported device and vehicle configurations.

**Engineering implications:**

**1. Assumption**

Each supported dashcam, phone app, and vehicle interface exposes a user-operable input and a display or other feedback channel while the feature is available.

**Specification**

For every supported configuration, the software shall expose controls to enable, disable, and pause the feature through the available user interface, and provide an observable confirmation of the selected state.

**2. Assumption**

Users can access a help or information channel associated with the dashcam or its companion interface, including when network access is unavailable.

**Specification**

The software shall expose a concise explanation of the feature, its data use, and the effects of its control settings through an information channel available in each supported configuration, without requiring an internet connection.

**3. Assumption**

The system can identify which supported dashcam, vehicle, and companion-device configuration is currently connected and which controls that configuration offers.

**Specification**

The software shall present only controls supported by the active configuration and shall communicate when a control is unavailable, along with the available way to change the feature state.

**4. Assumption**

Users may change settings on one device while the dashcam is disconnected or while other paired interfaces are available.

**Specification**

The software shall expose the effective feature state and any pending or unsynchronized control change on each connected interface, and shall communicate the result when a change takes effect.

---

## Stakeholder: Telecommunications and hotspot providers

**Type:** indirect

**Why they matter:** Their networks may carry alerts or footage when a dashcam connects through a phone or hotspot, creating capacity, cost, and privacy implications.

### Goal / Value

Protect network capacity and reliability for telecommunications and hotspot providers and their other customers.

#### Potential Loss

Large volumes of dashcam footage or repeated uploads congest network resources, degrading service for other users.

##### Requirement

Network capacity and service quality remain adequate for ordinary customer traffic during periods of system use.

**Engineering implications:**

**1. Assumption**

The phone, car, hotspot, or network service exposes connectivity status and, where available, a usable indication of current link capacity or congestion.

**Specification**

The software receives available connectivity and capacity/congestion information from the connected device or service, and limits or defers footage and alert-data transmission when the reported link is constrained.

**2. Assumption**

A missing-child report can be served using compact metadata or selected image segments rather than requiring continuous full-resolution footage uploads.

**Specification**

The software transmits only the report-related metadata and media payload requested for a detection or review, and exposes the size and purpose of each outbound transfer to the connected phone or network interface.

**3. Assumption**

The phone or hotspot can buffer data locally and later provide connectivity without requiring continuous network access from the dashcam.

**Specification**

When connectivity is unavailable or constrained, the software stores eligible report data locally and transmits it when a usable connection is available, without repeatedly retransmitting already acknowledged data.

**4. Assumption**

The network provider or hotspot can apply usage limits or communicate an allowed transfer budget to connected applications or devices.

**Specification**

The software receives any exposed transfer quota or user-configured data limit, and keeps system uploads within that limit while reporting when a limit prevents transmission.

#### Potential Loss

Bursts of alerts or uploads during a widely publicized missing-child search overload local networks or hotspot connections.

##### Requirement

Traffic demand from the system remains within the capacity available in affected network areas, including during demand surges.

**Engineering implications:**

**1. Assumption**

Affected mobile networks and hotspots expose current or estimated available capacity, congestion status, or explicit traffic limits to the system through a provider interface or connected device.

**Specification**

The software receives capacity or congestion status for the relevant network area and limits, defers, or pauses its transmissions so the traffic it sends stays within the reported available capacity.

**2. Assumption**

The system can identify bursts of local alert and upload demand, and can distinguish urgent alerts from bulk or deferrable data.

**Specification**

The software exposes traffic priority and urgency to the network interface and schedules or reduces non-urgent uploads during surges, while keeping urgent alert traffic within provider-imposed limits.

**3. Assumption**

Providers or hotspot operators can publish per-device, per-connection, or per-area rate limits and these limits are available to the dashcam or companion software.

**Specification**

The software receives and observes applicable rate limits and constrains its aggregate transmitted alert and media data to those limits, including when multiple items are queued.

**4. Assumption**

Network availability and capacity can change during a search, and the software can detect connectivity loss or restoration through its communication interfaces.

**Specification**

The software exposes queued-data volume and transmission status to the connected network service, suspends transmission when connectivity is unavailable or capacity is insufficient, and resumes only within subsequently available limits.

#### Potential Loss

Unexpected sustained data use causes providers to incur unplanned network operating and support costs.

##### Requirement

System-related traffic volumes and peak loads are sufficiently predictable for providers to plan capacity and operations.

**Engineering implications:**

**1. Assumption**

Providers can supply or publish service-specific usage limits, rate policies, or capacity guidance for supported network connections.

**Specification**

The software receives provider usage limits or policy updates for each supported connection and exposes its expected and observed system-related traffic against those limits through a provider-accessible interface.

**2. Assumption**

Dashcams or companion phones can identify the active connectivity path and report when that path changes.

**Specification**

The software reports traffic volume and connection-session start and end times, associated with the identified connectivity path, to the provider or an authorized planning interface.

**3. Assumption**

Providers can use periodic aggregate usage forecasts and historical summaries, and the software can transmit them when connectivity is available.

**Specification**

The software exposes forecasts and aggregate historical summaries of system-related traffic by reporting period, including expected peak periods, with a stated reporting interval and units.

**4. Assumption**

The system can operate with connectivity intermittent or unavailable, and local storage remains available for a bounded period.

**Specification**

The software stores timestamped traffic totals and connectivity availability intervals during outages, then transmits the accumulated records when a connection becomes available, identifying their original reporting periods.

**5. Assumption**

Providers need advance notice of material changes in system traffic behavior to adjust capacity and operations.

**Specification**

The software transmits a notice to the provider-facing interface when a configured, provider-visible traffic forecast or observed-usage threshold is exceeded, including the affected service, time window, and estimated volume.

### Goal / Value

Preserve customer privacy, trust, and fair use of network services.

#### Potential Loss

Sensitive footage or information about a child's location is exposed while traversing or being handled by network infrastructure.

##### Requirement

Applicable privacy and security protections are maintained across network links and any provider-operated infrastructure that handles system data.

**Engineering implications:**

**1. Assumption**

Dashcam-to-phone, vehicle, or hotspot links expose a way to establish an authenticated, encrypted connection, and the receiving endpoint supports compatible protections.

**Specification**

Before sending footage, child-location information, or related identifiers over a link, the software uses the link's authenticated protected channel; it does not send that sensitive data over an unprotected connection.

**2. Assumption**

Provider-operated services that receive or relay system data can identify their service endpoints and offer documented privacy and security conditions, including restrictions on access and onward disclosure.

**Specification**

When communicating with a provider-operated endpoint, the software sends only the data required for the requested service and exposes it only to the identified endpoint under the provider's stated privacy and security conditions.

**3. Assumption**

The device or companion software can determine whether a network connection is protected and whether the intended endpoint's identity can be validated.

**Specification**

If connection protection or endpoint identity cannot be validated, the software withholds sensitive footage and child-location data from that link and makes the failed or unavailable transfer status visible to the user.

**4. Assumption**

The dashcam or companion device has storage available for data awaiting a protected transfer, and users can access controls governing retention and deletion.

**Specification**

While awaiting a protected transfer, the software stores sensitive data only on the user-controlled device, exposes its retention status and deletion controls, and does not place it in provider-operated storage until the protected transfer conditions are met.

**5. Assumption**

Network providers may impose usage limits or charge for data, and the software can obtain connection-type or user-approved transfer settings.

**Specification**

Before transmitting large or non-urgent sensitive data over a metered or provider-managed connection, the software follows the user's transfer and data-use settings and exposes the expected transfer size or relevant usage status.

#### Potential Loss

Customers blame providers for unexpected data charges or hotspot depletion caused by system traffic, damaging trust and prompting complaints.

##### Requirement

Customers have clear expectations about potential system-related data use, and resulting charges or resource consumption are transparent and acceptable.

**Engineering implications:**

**1. Assumption**

Users can access a device or companion-app interface before enabling missing-child search, and that interface can display estimates or ranges for expected data use.

**Specification**

Before network-dependent activity is enabled, the software exposes an estimate or range of expected data use for the selected operating mode and search period, identifying that actual use may vary.

**2. Assumption**

The dashcam or companion app can observe whether a connection is using cellular data, a metered hotspot, or an unmetered connection, or can obtain this status from the connected device.

**Specification**

The software receives the available connection or metering status and exposes which connection the system will use; it requests user confirmation before transmitting search-related data over a connection identified as metered.

**3. Assumption**

The device or companion app can measure or estimate bytes sent and received for system activity, and users have a way to view this information.

**Specification**

The software exposes an ongoing and cumulative record of data consumed by the missing-child detection service, with the relevant reporting period and an indication when values are estimates.

**4. Assumption**

Users can change service settings, and the software can defer or limit network-dependent activity in response to those settings.

**Specification**

The software exposes controls to set or change a data-use limit or preference, and communicates when the service is paused, reduced, or awaiting a permitted connection because that setting has been reached.

**5. Assumption**

Telecommunications or hotspot providers make applicable data charges, fair-use conditions, or resource limits available to customers through their own service terms or interfaces.

**Specification**

The software presents a notice that provider charges and hotspot limits are governed by the user's plan and may not be knowable by the system, and directs the user to the provider's available plan information rather than asserting that use is charge-free.

#### Potential Loss

Network use for the system conflicts with provider service terms, regulatory obligations, or lawful handling requirements, exposing providers to liability.

##### Requirement

System-related network use is compatible with applicable telecommunications rules, service terms, and legal obligations in the jurisdictions where it operates.

**Engineering implications:**

**1. Assumption**

Applicable telecommunications rules, hotspot service terms, and legal obligations can be identified for each operating jurisdiction and for the relevant connection type.

**Specification**

The system exposes its operating jurisdiction, connection type, and intended network-use categories to an authorized compliance configuration interface, and receives the applicable restrictions and permitted-use conditions for those contexts.

**2. Assumption**

Providers or device owners can communicate relevant usage limits and conditions, such as caps, permitted destinations, or restrictions on automated/background traffic, through available network or configuration interfaces.

**Specification**

Before and during network transfers, the system exposes or transmits its expected traffic purpose, destination, and estimated or actual usage where supported, and receives applicable usage limits or restrictions; it limits transfers to those received conditions.

**3. Assumption**

The system can determine when network access is unavailable, restricted, or not authorized without relying on the provider to infer the system's compliance state.

**Specification**

The system receives connection authorization and restriction status from the phone, hotspot, or network interface and, when access is absent or restricted, does not send system data over that connection.

**4. Assumption**

Lawful handling obligations relevant to transmitted data, including any required notices, consent states, retention limits, or deletion requests, can be supplied to the system through authorized interfaces.

**Specification**

The system receives applicable data-handling instructions and consent or authorization status, and exposes/transmits only the system data permitted by those instructions; it provides interfaces to report relevant transfer and deletion status when required.

**5. Assumption**

Providers can reasonably identify the system's network traffic and obtain records needed to address complaints, audits, or lawful requests, subject to applicable privacy safeguards.

**Specification**

The system labels or otherwise identifies its network traffic as system-related where the connection supports it, and makes a minimal record of transfer time, destination, purpose category, and volume available to the authorized user or provider when lawfully requested.

---

## Stakeholder: Privacy and data-protection regulators

**Type:** indirect

**Why they matter:** They oversee compliance with rules governing children’s data, biometric or image processing, location data, and cross-party data sharing.

### Goal / Value

Ensure the system complies with applicable privacy, data-protection, and child-safeguarding laws and regulatory obligations.

#### Potential Loss

Children’s or bystanders’ images are collected or processed without a valid legal basis or required safeguards, exposing the organization to enforcement action and undermining regulatory protection.

##### Requirement

Applicable legal bases, permitted purposes, and safeguards for processing children’s and bystanders’ data are clearly established for each operating jurisdiction.

**Engineering implications:**

**1. Assumption**

Applicable privacy, data-protection, and child-safeguarding rules can be identified for each jurisdiction in which the system is offered or used, including requirements that vary by purpose, data type, and affected person.

**Specification**

For each enabled jurisdiction, the software receives and exposes a current jurisdiction-specific policy record identifying the applicable legal bases, permitted processing purposes, and required safeguards for children’s and bystanders’ data; it makes processing unavailable where that record is absent or marked unresolved.

**2. Assumption**

The organization’s authorized legal or compliance function can determine and provide the lawful basis and permitted purposes for each deployment and processing activity.

**Specification**

The software accepts and stores an approved processing configuration that associates each enabled activity with its jurisdiction, legal basis, purpose, covered data, and applicable safeguards, and exposes that configuration for review.

**3. Assumption**

Regulatory safeguards can be expressed as observable conditions or limits, such as retention periods, access restrictions, notice requirements, or constraints on transmission.

**Specification**

The software receives the safeguards applicable to each configured activity and exposes relevant user notices and processing limits, and records or provides evidence of retention, access, and transmission events needed to demonstrate compliance.

**4. Assumption**

The system can obtain a reliable indication of the jurisdiction governing a particular deployment or processing event, and that indication is available to the software.

**Specification**

The software receives the applicable jurisdiction context for each deployment or processing event and exposes which jurisdictional policy governs it; when the context is unknown or conflicting, it suspends affected processing and reports the unresolved jurisdiction.

#### Potential Loss

Sensitive image or biometric data is retained longer or used more broadly than permitted, leading to unlawful processing and regulatory sanctions.

##### Requirement

Retention periods and permitted uses for image and biometric data are limited, documented, and consistent with applicable law.

**Engineering implications:**

**1. Assumption**

Applicable privacy, data-protection, and child-safeguarding rules can be identified for each deployment jurisdiction, including distinctions between image data and biometric data.

**Specification**

The software receives or is configured with the applicable jurisdiction and its authorized retention limits and permitted purposes, and exposes the resulting policy scope for review; where no applicable policy is available, it does not enable collection or use of the affected data.

**2. Assumption**

A legally authorized party can define and update retention periods and permitted uses, and provide authenticated policy changes to the system.

**Specification**

The software accepts authenticated policy updates specifying data categories, retention deadlines, and permitted purposes, and produces an acknowledgment or an error identifying policy entries it cannot apply.

**3. Assumption**

The system can identify when image or biometric records are created, their data category, and any purpose for which they are collected or used.

**Specification**

For each stored image or biometric record, the software stores associated category, collection/use purpose, and retention deadline, and exposes these records or associated metadata for authorized compliance inspection.

**4. Assumption**

The system has a reliable time source and access to stored records so that expiry can be determined and expired data can be removed from active storage and any system-controlled copies.

**Specification**

The software uses the configured deadlines to remove expired image and biometric data, including system-controlled copies, and produces an auditable record of deletion; it exposes no expired data for further use after the deadline.

**5. Assumption**

Authorized recipients and system functions can be distinguished by identity and declared purpose, and relevant access and transfer events are observable.

**Specification**

Before exposing or transmitting image or biometric data, the software checks the requester's authorization and stated purpose against the configured permitted uses, denies out-of-scope requests, and records the decision and any permitted disclosure for audit.

#### Potential Loss

Location-linked footage or search results are disclosed to parties without proper authority, violating restrictions on sensitive data sharing.

##### Requirement

Authorities and organizations receiving location-linked or identifying data have verified legal authority, defined roles, and binding data-sharing terms.

**Engineering implications:**

**1. Assumption**

A competent authority or authorized organization can provide verifiable credentials or documentation identifying its legal mandate, authorized data categories, geographic or case scope, and validity period.

**Specification**

Before disclosing location-linked footage or identifying search results, the software receives and records the recipient's authority evidence and requested scope, and exposes data only when the verified authority covers that scope; otherwise it refuses disclosure.

**2. Assumption**

The participating authorities and organizations designate accountable contacts and can provide role assignments for personnel who request, approve, or receive sensitive data.

**Specification**

The software receives and stores recipient organization and user role information, associates each access or disclosure with the responsible roles, and exposes data only to roles authorized for the relevant task.

**3. Assumption**

Applicable law and participating organizations support binding, documented data-sharing agreements that specify permitted purposes, data types, retention, onward disclosure, security duties, and deletion or return obligations.

**Specification**

The software receives or references the applicable agreement and its terms, stores the agreement version and recipient acceptance, and transmits or exposes location-linked or identifying data only under the agreed purpose and conditions.

**4. Assumption**

Legal authority, role assignments, and data-sharing agreements can expire, be amended, or be revoked, and the relevant organizations provide timely status updates.

**Specification**

The software receives updates to authority, roles, and agreement status, records their effective dates, and stops or limits subsequent disclosures when the applicable authorization or terms are expired, suspended, revoked, or superseded.

#### Potential Loss

Children or their guardians are denied applicable rights or protections because responsibilities and processes for handling requests and complaints are unclear.

##### Requirement

Clear, accessible processes and accountable parties exist for exercising applicable data rights and raising privacy complaints, including on behalf of children.

**Engineering implications:**

**1. Assumption**

Applicable laws and regulatory guidance identify relevant data rights, complaint routes, response obligations, and any special rules for children or representatives, and this information is available to the system operator.

**Specification**

The software exposes a clear, accessible privacy notice that identifies the applicable rights and complaint routes, explains how a child or guardian/authorized representative can submit a request, and provides relevant deadlines and escalation options.

**2. Assumption**

A designated operator or other accountable organization can be identified and provides current contact details and responsibility boundaries for handling rights requests and complaints.

**Specification**

The software presents the responsible organization and a usable contact channel for rights requests and privacy complaints, including who handles each type of request and how to reach them.

**3. Assumption**

People can submit requests or complaints through at least one supported communication channel, and the operator can receive and acknowledge submissions through that channel.

**Specification**

The software provides an accessible submission interface or directs users to a supported channel, and transmits submitted requests or complaints and a receipt confirmation to the designated handler.

**4. Assumption**

The system can receive enough information from the requester or operator to distinguish a child, guardian, or other representative and to communicate safely without requiring unnecessary personal data.

**Specification**

The software exposes guidance on what information is needed to verify identity or authority, supports indicating that a request is made on behalf of a child, and communicates the request's status or required next steps to the requester through the provided channel.

**5. Assumption**

The operator is responsible for maintaining records and carrying out legally required follow-up, and can provide the software with relevant outcome or escalation information.

**Specification**

The software transmits requests and complaints to the accountable handler and exposes the handler's acknowledgment, response, or escalation contact to the requester, without representing that the software itself determines legal eligibility or resolves the complaint.

### Goal / Value

Protect individuals from disproportionate surveillance, privacy harms, and insecure handling of sensitive data while enabling accountable use of the system.

#### Potential Loss

Continuous or widespread capture of uninvolved people creates disproportionate surveillance and loss of privacy.

##### Requirement

Collection is necessary and proportionate to the defined missing-child purpose, with meaningful limits on whose data and which areas or periods may be included.

**Engineering implications:**

**1. Assumption**

The missing-child program or authorized case service can provide authenticated, current case information that identifies an active search, the child sought, and the geographic areas and time window relevant to that search.

**Specification**

The software receives and verifies case scope and validity information from the authorized service, and limits any footage or derived observations collected or transmitted for a search to that case's specified areas and active time window; it exposes the case scope and expiry to authorized operators.

**2. Assumption**

Applicable policy and operational rules define which people and data are necessary for a missing-child search, and provide an authorized way to represent exclusions or limits on collecting uninvolved people’s data.

**Specification**

The software receives the applicable collection rules, and exposes only search-relevant observations to the authorized service; it does not transmit or retain identifiable footage or observations outside those rules, and reports the collection scope and any exceptions to authorized oversight.

**3. Assumption**

The dashcam can determine or receive its current location and time with sufficient reliability to apply search boundaries and duration limits.

**Specification**

The software receives location and time information and uses it as the basis for deciding whether search-related footage or observations fall within the authorized area and period; it withholds transmission and limits retention when the information is unavailable or cannot establish that the scope is valid.

**4. Assumption**

Authorized users and oversight bodies can access a clear record of the search authorization and the data collected, retained, or transmitted under it.

**Specification**

The software exposes to authorized users an auditable record of the search identifier, scope, time limits, and categories and amounts of data collected, retained, or transmitted, without making that record available to unauthorized parties.

#### Potential Loss

A breach or unauthorized access exposes children’s identities, images, or location histories, causing safety, dignity, or privacy harms.

##### Requirement

Sensitive data is protected throughout its lifecycle by security controls appropriate to the risks, and security responsibilities are assigned and monitored.

**Engineering implications:**

**1. Assumption**

A trusted authority can provide authenticated, current missing-child case data, including authorized purpose, scope, and expiry, over an available phone, vehicle, or hotspot connection.

**Specification**

The software shall accept case data only with its associated authorization, purpose, scope, and expiry; expose only the case information needed for matching; and cease retaining or transmitting case data when authorization expires or is revoked.

**2. Assumption**

Dashcam owners can configure whether and when the device may process or share footage, and can receive understandable notices about the data involved.

**Specification**

The software shall expose privacy and sharing settings, provide notice of the categories and destinations of sensitive data before sharing, and honor the selected settings when storing or transmitting footage, images, matches, and location information.

**3. Assumption**

Authorized operators and service personnel have identifiable accounts or credentials, and an accountable organization can designate their roles and review access.

**Specification**

The software shall require authenticated access to sensitive data and administrative functions, expose data only to role-authorized users, and provide the responsible organization with access and privilege-change records for review.

**4. Assumption**

The device, connected phone or vehicle, and receiving services provide interfaces capable of protected communication and protected storage, and report relevant security status or failures.

**Specification**

The software shall use the available protected-storage and protected-communication interfaces for sensitive data, avoid sending it over unprotected channels, and expose security failures or unavailable protections to the user or responsible service so that data handling can be restricted.

**5. Assumption**

The responsible organization can define applicable retention limits and security responsibilities, and has a channel to receive incident and compliance information.

**Specification**

The software shall apply configured retention and deletion limits to sensitive data, and provide the designated organization with records of retention, deletion, security incidents, and assigned responsibility sufficient to monitor compliance.

#### Potential Loss

Inaccurate identification or location matches trigger intrusive intervention against an uninvolved child or family.

##### Requirement

Any action based on a system match is subject to accountable human verification, and the system’s known accuracy limits and error risks are assessed.

**Engineering implications:**

**1. Assumption**

A match can be associated with a report, the relevant image or clip, a time and location, and the model/version and confidence information available when the match was generated.

**Specification**

For each match, the software exposes to an authorized reviewer the match evidence, report reference, time and location, confidence information, and model/version metadata before any operational action is initiated.

**2. Assumption**

An authorized human reviewer is available to inspect match evidence and record a verification decision before responders or other parties act on a match.

**Specification**

The software provides an authorized review interface to accept, reject, or defer each match, records reviewer identity, decision, and time, and transmits or exposes a match for action only after a recorded verification decision.

**3. Assumption**

Ground-truth cases, representative operating-condition data, and observed false-positive and false-negative outcomes can be obtained for evaluating the system's performance and its limits.

**Specification**

The software produces and retains an assessment record that presents measured accuracy, false-positive and false-negative rates, evaluation conditions, and known limitations for each deployed model/version, and makes it available to designated oversight personnel.

**4. Assumption**

Relevant stakeholders can receive notices when accuracy assessments or material error risks change, and can use those notices to review continued use.

**Specification**

When an assessment is updated or a material error risk is identified, the software exposes the change, its affected model/version and operational scope, and the assessment record to designated oversight personnel before that version is used for new match-based actions.

---

## Stakeholder: Emergency dispatchers and search-and-rescue teams

**Type:** indirect

**Why they matter:** They may receive system-generated leads and must assess their reliability, potentially changing search priorities and operational workload.

### Goal / Value

Make sound, timely search and response decisions using leads that are sufficiently reliable and actionable.

#### Potential Loss

A false or poorly localized lead redirects teams away from the child’s actual location, delaying recovery.

##### Requirement

Leads available to responders have adequate location precision, recency, and evidential confidence for the decisions they may inform.

**Engineering implications:**

**1. Assumption**

Dashcams or paired devices can obtain a location estimate with a timestamp, and that estimate has a measurable uncertainty or quality indicator.

**Specification**

For each candidate sighting exposed to responders, provide the location estimate, its capture time, and the available location-accuracy/uncertainty information; identify when location data is unavailable or too imprecise to support localization.

**2. Assumption**

Dashcams, paired devices, and communication links provide enough timing information to determine when footage was captured and whether it is stale when delivered.

**Specification**

Associate each lead with the footage capture time and the lead creation or transmission time, and expose its age or freshness status to responder-facing systems.

**3. Assumption**

The footage contains observable evidence that can be reviewed and compared with the missing-child report, and responders can interpret supporting context.

**Specification**

Transmit or expose the evidence supporting each lead, such as relevant image/video excerpts and the reported-child attributes used for comparison, while distinguishing observed evidence from inferred match claims.

**4. Assumption**

Responders have a means to receive lead metadata and evidence, and can act on explicit uncertainty and provenance information.

**Specification**

Expose a confidence or uncertainty indication together with the basis and provenance of the lead, including source device and relevant processing or report version, and mark leads that are unverified or below configured decision-use thresholds rather than presenting them as confirmed sightings.

##### Requirement

Operational procedures preserve the ability to continue or resume other search priorities while a lead is checked.

**Engineering implications:**

**1. Assumption**

Dispatchers can keep multiple search priorities active and assign different teams or resources to them while a reported lead is being checked.

**Specification**

The software exposes each lead as a separately trackable item alongside the active search priorities, and lets authorized users record its verification status without replacing or closing those priorities.

**2. Assumption**

Teams checking a lead can report their availability, progress, and whether they need additional support through a channel accessible to the software.

**Specification**

The software receives and displays lead-check status and team availability, and exposes the information to dispatchers so they can continue assigning resources to other priorities while the check is underway.

**3. Assumption**

A lead may remain unverified, be rejected, or become stale, and dispatchers need to distinguish these states to avoid treating it as a confirmed location.

**Specification**

The software records and presents the lead's verification state, timestamp, and any expiry or supersession status, and communicates status changes to dispatchers without marking an unverified lead as confirmed.

**4. Assumption**

Search teams can act on bounded, actionable lead information without abandoning their current assignments, and dispatchers can specify which resources are committed to a check.

**Specification**

The software exposes the lead's location estimate, uncertainty, source/time, and requested check resources separately from existing assignments, and provides dispatchers a way to record or transmit the limited resource allocation for the check.

#### Potential Loss

An outdated sighting is treated as current, causing resources to be sent to a location where the child is no longer present.

##### Requirement

Responders can distinguish when a sighting occurred from when it was received, and understand the uncertainty in its age.

**Engineering implications:**

**1. Assumption**

A dashcam or its connected phone/car can provide a timestamp for when footage was captured, and its clock offset or uncertainty can be estimated or bounded.

**Specification**

For each sighting, expose and transmit the estimated occurrence time, the clock/time-source basis, and an explicit time-uncertainty interval or status; do not present an unqualified timestamp when its uncertainty is unknown.

**2. Assumption**

The reporting device or communication service can record when it receives a sighting, using a clock that is distinguishable from the capture-time source.

**Specification**

Store, display, and transmit the sighting's receipt time separately from its estimated occurrence time, labeling both so responders can tell them apart.

**3. Assumption**

Capture metadata may be absent, delayed, or unreliable, and responders need to know when the sighting age cannot be determined confidently.

**Specification**

When occurrence time or its uncertainty cannot be established from received metadata, expose an explicit unknown or low-confidence age status and its available bounds rather than implying a precise age.

**4. Assumption**

Reports may be forwarded through multiple devices or services, and transmission delays can vary.

**Specification**

Preserve and expose the original occurrence-time and receipt-time fields across forwarding, while recording each later receipt/forwarding time distinctly, so relaying does not make an old sighting appear recent.

#### Potential Loss

Duplicate or correlated reports are mistaken for independent corroboration, creating unjustified confidence in a lead.

##### Requirement

Responders can determine whether reports are independent or derive from the same underlying observation.

**Engineering implications:**

**1. Assumption**

Reports can include a stable, privacy-appropriate reference to the observation they came from, such as a source report identifier or a securely derived event fingerprint, and reporting devices preserve it when forwarding a report.

**Specification**

The software receives and retains the observation reference with each report, and exposes that reference or a responder-readable relationship between reports so responders can identify reports linked to the same source observation.

**2. Assumption**

Reporting devices or intermediaries can provide provenance information identifying the originating device or reporter and any forwarding or relay chain, and this information is available to the system.

**Specification**

The software records and presents report provenance, including origin and known relay relationships, alongside each lead so responders can distinguish direct observations from reports relayed from another report.

**3. Assumption**

Independent reporting devices have sufficiently distinct, privacy-permitted source identifiers, while devices that share an observation can be linked through a common reference or declared forwarding relationship.

**Specification**

The software exposes source identifiers and any known shared-observation links for related reports, enabling responders to assess whether apparently separate submissions represent independent observations.

**4. Assumption**

Reports contain usable time and location context, and reporting devices or reporters can provide it with enough accuracy to compare observations.

**Specification**

The software stores and displays the reported observation time and location, including uncertainty where supplied, for each report so responders can judge whether reports may reflect the same encounter rather than independent corroboration.

#### Potential Loss

A vague or incomplete lead consumes dispatch attention and field resources without enabling effective verification.

##### Requirement

Leads provided for operational use contain enough context to assess and verify them, including relevant uncertainty and source limitations.

**Engineering implications:**

**1. Assumption**

Dispatchers and search teams can receive structured lead information through their operational systems or devices, even when originating dashcams lack internet access.

**Specification**

For each lead sent for operational use, the software exposes or transmits the observation time and location, the relevant sighting context, and the lead's source identifier in a format available to receiving responders.

**2. Assumption**

Dashcam observations and location/time signals may be incomplete or imprecise, and those limitations can be represented as data.

**Specification**

The software includes available location and time precision, missing or unavailable fields, and any applicable uncertainty indicators with the lead, rather than presenting estimates as exact values.

**3. Assumption**

A lead's evidential strength depends on what was observed and the conditions under which the observation was made, such as visibility or image quality.

**Specification**

The software provides responders with the relevant observation evidence or a reviewable excerpt, together with disclosed capture limitations that affect interpretation, subject to applicable privacy and retention constraints.

**4. Assumption**

Responders can use information about how a lead was generated and whether it has been corroborated to prioritize verification.

**Specification**

The software labels the lead's basis (for example, automated match, user report, or both), distinguishes unverified from corroborated information, and exposes any available corroboration and its source.

**5. Assumption**

Operational recipients need enough provenance to request clarification or independently assess a lead, and the software has access to that provenance.

**Specification**

The software includes available provenance—such as reporting device or submitting contact, submission time, and a means to request follow-up—in the lead record transmitted to authorized recipients.

#### Potential Loss

High-volume or low-quality leads overload dispatchers, delaying attention to urgent calls and other search activity.

##### Requirement

Lead volume and verification workload remain within the capacity of dispatch and search operations, including during surges.

**Engineering implications:**

**1. Assumption**

Dispatch and search operations can provide or designate current capacity limits, including surge-specific limits, for lead intake and verification.

**Specification**

The software receives and stores the current lead-volume and verification-workload limits from authorized dispatch or search operations, and exposes those limits to the systems and users that submit or review leads; when limits are changed, it makes the updated limits available before further lead handling.

**2. Assumption**

Dispatchers and search teams can distinguish and act on leads when each lead includes concise, decision-relevant evidence and provenance.

**Specification**

For every lead sent to dispatch or search personnel, the software transmits the location and time estimate, available supporting evidence, source/provenance, and an uncertainty or confidence indication, and exposes these fields for review before operational action.

**3. Assumption**

Dispatch and search operations have a means to receive status or priority information and can defer, limit, or pause nonurgent lead delivery during overload.

**Specification**

The software exposes current lead backlog and verification workload to authorized operations personnel and accepts their priority, deferral, rate-limit, or pause decisions, applying those decisions to subsequent lead delivery and notifying them when delivery is constrained.

**4. Assumption**

Dispatch and search teams can provide feedback on whether leads are actionable, duplicate, or incorrect, and that feedback can inform ongoing operations.

**Specification**

The software provides an interface for authorized personnel to label leads as actionable, duplicate, insufficient, or incorrect, stores the feedback with the associated lead, and exposes aggregate lead-quality and verification-workload summaries to operations personnel.

### Goal / Value

Protect the safety, lawful operation, and public trust necessary for coordinated search-and-rescue work.

#### Potential Loss

Teams enter a hazardous area or approach a person based on an erroneous identification or location, risking injury to responders or the public.

##### Requirement

Search actions based on leads are subject to appropriate risk assessment and independent verification before hazardous or confrontational intervention.

**Engineering implications:**

**1. Assumption**

Dispatchers and search-and-rescue teams can provide the system with the operational context for a lead, including the reported location and time, confidence, and any known hazards or access restrictions.

**Specification**

The software receives and presents lead context, uncertainty, and available hazard or access information to authorized dispatchers and responders before they decide whether to act.

**2. Assumption**

Independent verification can be obtained from a source or person distinct from the original lead, such as a second authorized reviewer or corroborating observation.

**Specification**

The software records and exposes the verification source, verification time, and corroborating information separately from the original lead, and indicates when independent verification has not been supplied.

**3. Assumption**

Responders can provide or access a risk assessment for the proposed action before entering a hazardous area or initiating a confrontational intervention.

**Specification**

The software requests and records a risk assessment associated with a proposed action, and presents its status and identified risks to the responsible dispatcher or team before the action is authorized or marked as proceeding.

**4. Assumption**

Dispatchers and response teams can receive timely updates when a lead is corrected, withdrawn, or superseded.

**Specification**

The software transmits lead corrections, withdrawals, and material changes in confidence or location to the authorized recipients who received the lead, and exposes whether those updates were delivered or acknowledged.

#### Potential Loss

Unnecessary collection or disclosure of sensitive footage or location information undermines public trust and cooperation with search efforts.

##### Requirement

Access to and sharing of sensitive lead information are limited to legitimate response needs and governed by clear accountability and retention practices.

**Engineering implications:**

**1. Assumption**

Authorized response agencies can be identified and provide current role or case assignments, and those assignments are observable to the software.

**Specification**

The software shall receive responder identity, agency, role, and case-assignment information from an authoritative source, and expose sensitive lead information only to authenticated responders whose current assignments authorize access to that case.

**2. Assumption**

Agencies define which lead fields and actions are necessary for each response role, and those rules can be supplied to the system.

**Specification**

The software shall receive role- and task-specific access rules and, when responding to lead queries or sharing requests, expose only the fields and actions permitted by those rules.

**3. Assumption**

A designated response authority can authorize disclosures to additional parties and specify the purpose and scope of each disclosure.

**Specification**

Before transmitting sensitive lead information to a recipient outside the current authorized case team, the software shall receive and record the approving authority, recipient, purpose, scope, and expiry, and shall transmit only the approved information to that recipient.

**4. Assumption**

Accountability and retention policies are defined by the responsible agencies, including required audit records, retention periods, and authorized deletion conditions.

**Specification**

The software shall store access and disclosure records identifying the actor, case, information accessed or shared, time, and authorization basis; expose those records to authorized auditors; and retain or delete lead data and audit records according to the supplied retention and deletion rules.

#### Potential Loss

Unclear responsibility for validating and acting on system-generated leads causes conflicting actions or gaps between dispatch and field teams.

##### Requirement

Roles and handoff responsibilities for receiving, assessing, validating, and acting on leads are clear across participating organizations.

**Engineering implications:**

**1. Assumption**

Participating organizations can identify their authorized roles and provide current contact or routing details for dispatch and field-team functions.

**Specification**

The software receives and stores organization, role, and current contact/routing details for lead receipt, assessment, validation, and field action, and exposes the applicable responsibility and contact information with each lead.

**2. Assumption**

Organizations agree on lifecycle states and the events that constitute accepting, assessing, validating, escalating, or closing a lead.

**Specification**

The software presents leads using the agreed lifecycle states and records and exposes the responsible organization or role and timestamp for each reported state transition.

**3. Assumption**

Authorized users can exchange lead records and acknowledgments through supported system interfaces, even when individual dashcams lack internet connectivity.

**Specification**

The software transmits each lead and its assigned receiving role to the designated participating organization, and exposes receipt or delivery status and any handoff acknowledgment to authorized users.

**4. Assumption**

Participating organizations can provide updates when responsibility changes, a lead is rejected, or further action is required.

**Specification**

The software receives and records reassignment, rejection, escalation, and action updates with the submitting organization and time, and exposes the current accountable role and outstanding handoff status to relevant organizations.
