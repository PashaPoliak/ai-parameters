def save_to_file_json_response(data, filename="additional_parameters_results.json"):
    """
    Save the response data to a JSON file
    """
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Results saved to {filename}")
