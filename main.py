from models.doctor import Doctor

#creation of instance
doctor1 = Doctor("Vincent")
#converts instance to row
# doctor1.save()
print(doctor1)


doctors =["Ruth", "Elfas", "Godwin"]

# for doctor in doctors:
#     new_doc = Doctor(doctor)
#     new_doc.save()

# Doctor.create_many([("Jane",), ("John",)])

many_docs = Doctor.find_many_by_ids(6,7,8)
print(many_docs)

one_doc = Doctor.find_one(7)
print(one_doc)

one_doc.update("Mandela")