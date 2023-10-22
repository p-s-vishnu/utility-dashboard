import datetime


def extract_time(data):
    transformed_data = []

    for entry in data:
        timestamp = datetime.datetime.fromisoformat(entry['interval_start'])
        time_component = timestamp.strftime('%H:%M')

        transformed_entry = {
            "interval_start": time_component,
            "interval_end": time_component,
            "consumption": entry['consumption']
        }
        transformed_data.append(transformed_entry)

    return transformed_data
