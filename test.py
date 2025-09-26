import fastf1
import f1_config 

# Get the schedule for a weekend
year = 2024
gp_round = 5  # Or a race name like "Miami"
event = fastf1.get_event(2025,2)
event2 = event.get_session(2)

print(event2)
