import school_scores
list_of_record = school_scores.get_all()

print(list_of_record[0])

for score in list_of_record:
    print(score["State"]["Name"])
