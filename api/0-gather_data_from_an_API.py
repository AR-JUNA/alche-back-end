#!/usr/bin/python3
"""
0-gather_data_from_an_API.py
Fetches employee TODO list progress from REST API
"""

import sys
import requests


def main():
    """Main function to get employee TODO progress"""
    
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        return 1
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        return 1
    
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    
    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data.get('name')
        
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()
        
        total_tasks = len(todos_data)
        done_tasks = 0
        done_titles = []
        
        for task in todos_data:
            if task.get('completed'):
                done_tasks += 1
                done_titles.append(task.get('title'))
        
        print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks, total_tasks))
        
        for title in done_titles:
            print("\t {}".format(title))
            
    except requests.exceptions.HTTPError:
        print("Error: Could not find employee with ID {}".format(employee_id))
        return 1
    except Exception as e:
        print("Error: {}".format(e))
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
