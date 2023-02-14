from faker import Faker
fake = Faker()

profile = fake.profile()

print("Name:", profile["name"])
print("Address:", profile["address"])
print("Email:", profile["mail"])
print("Job:", profile["job"])
print("Company:", profile["company"])
print("SSN:", profile["ssn"])
print("Residence:", profile["residence"])
print("Current Location:", profile["current_location"])
print("Blood Group:", profile["blood_group"])
print("Website:", profile["website"])
print("Username:", profile["username"])
print("Sex:", profile["sex"])
print("Birthdate:", profile["birthdate"])
