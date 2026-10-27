
# Campus Event Financial Planning System

import math

# Event budget details
venue_cost = 15000
equipment_cost = 8000
catering_cost_per_person = 200
transport_cost_per_person = 100
certificate_cost_per_person = 30

expected_participants = 100
registration_fee = 250
sponsorship_received = 10000

# Calculate fixed and variable costs
fixed_cost = venue_cost + equipment_cost

variable_cost_per_person = (
    catering_cost_per_person
    + transport_cost_per_person
    + certificate_cost_per_person
)

total_event_cost = (
    fixed_cost
    + variable_cost_per_person * expected_participants
)

# Calculate participant contributions
participant_contributions = (
    registration_fee * expected_participants
)

# Calculate total funds and shortfall
total_funds = participant_contributions + sponsorship_received

shortfall = max(0, total_event_cost - total_funds)
surplus = max(0, total_funds - total_event_cost)

# Calculate minimum registrations needed to break even
if registration_fee > variable_cost_per_person:
    required_registrations = math.ceil(
        (fixed_cost - sponsorship_received)
        / (registration_fee - variable_cost_per_person)
    )
    required_registrations = max(0, required_registrations)
else:
    required_registrations = None

# Display budget report
print("=" * 45)
print(" CAMPUS EVENT FINANCIAL REPORT")
print("=" * 45)

print("\nFIXED COSTS")
print("Venue Cost: Rs.", venue_cost)
print("Equipment Cost: Rs.", equipment_cost)
print("Total Fixed Cost: Rs.", fixed_cost)

print("\nVARIABLE COSTS PER PARTICIPANT")
print("Catering: Rs.", catering_cost_per_person)
print("Transport: Rs.", transport_cost_per_person)
print("Certificate: Rs.", certificate_cost_per_person)
print("Total Per Participant: Rs.", variable_cost_per_person)

print("\nOVERALL EVENT BUDGET")
print("Expected Participants:", expected_participants)
print("Total Event Cost: Rs.", total_event_cost)
print("Registration Fee: Rs.", registration_fee)
print("Participant Contributions: Rs.", participant_contributions)
print("Sponsorship Received: Rs.", sponsorship_received)
print("Total Available Funds: Rs.", total_funds)

print("\nFINANCIAL SUMMARY")
print("Sponsorship Shortfall: Rs.", shortfall)
print("Budget Surplus: Rs.", surplus)

print("\nBREAK-EVEN ANALYSIS")
if required_registrations is not None:
    print("Minimum Registrations Required:",
          required_registrations)

    if required_registrations <= expected_participants:
        print("Break-even is possible within the expected "
              "participant count.")
    else:
        print("More participants or additional funding "
              "are needed.")
else:
    print("Break-even through registrations alone "
          "is not possible with this fee.")

print("=" * 45)
