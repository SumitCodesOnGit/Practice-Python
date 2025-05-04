import pickle
# sample data
company_details = {
    "name":"Sutradhari.ai",
    "founded": 2025,
    "Founder": "Sumit Singh",
    "Sector": "IT-Women Welefare Service sector"
}
""" # pickling: save data to a file
with open("company.pkl","wb") as file:
    pickle.dump(company_details,file)
    print("Data pickled successfully")

# unpickling: load data back from file
with open("company.pkl","rb") as file:
    loaded_data=pickle.load(file)
    print("Data unpickled sucessfully")
    print(loaded_data) """

# pickling and unpickling multiple objects
import pickle
data1=[12,34,78]
data2=("abc","sumit")
data3={"1":"Go to Manhatten"}

with open("multiple.pkl","wb") as file:
    pickle.dump(data1,file)
    pickle.dump(data2,file)
    pickle.dump(data3,file)
    print("multiple data pickled sucessfully")

with open("multiple.pkl","rb") as file:
    loaded_data1=pickle.load(file)
    loaded_data2=pickle.load(file)
    loaded_data3=pickle.load(file)
    print("multiple data unpickled successfully")
    print(loaded_data1)
    print(loaded_data2)
    print(loaded_data3) # always ensure u unpickle the data in the same order u pickled.


