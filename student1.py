import json

# function to add to JSON
def write_json(data, filename='student.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)
      
      
with open('student.json') as json_file:
    data = json.load(json_file)
      
    temp = data['student_details']
  
    # python object to be appended
    y = {"name":'Nikhil',
         "email": "nikhil@geeksforgeeks.org",
         "age": "22"
        }
  
  
    # appending data to emp_details 
    temp.append(y)
      
write_json(data) 