import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries")
        return
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, 1):
        filled_template = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if not value:
                value = "N/A"
            filled_template = filled_template.replace(f"{{{key}}}", str(value))
        
        filename = f"output_{i}.txt"
        with open(filename, 'w') as file:
            file.write(filled_template)
