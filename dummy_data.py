import json
from datetime import datetime

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Planning


# Define a function to import the data into the database
def import_data(db: Session):
    with open("planning.json") as jsonfile:
        data = json.load(jsonfile)
        for row in data:
            dict_to_add = {}
            dict_to_add["id"] = row["id"]
            dict_to_add["original_id"] = row["originalId"]
            dict_to_add["talent_id"] = row["talentId"]
            dict_to_add["talent_name"] = row["talentName"]
            dict_to_add["talent_grade"] = row["talentGrade"]
            dict_to_add["booking_grade"] = row["bookingGrade"]
            dict_to_add["operating_unit"] = row["operatingUnit"]
            dict_to_add["office_city"] = row["officeCity"]
            dict_to_add["office_postal_code"] = row["officePostalCode"]
            dict_to_add["job_manager_name"] = row["jobManagerName"]
            dict_to_add["job_manager_id"] = row["jobManagerId"]
            dict_to_add["total_hours"] = float(row["totalHours"])
            dict_to_add["start_date"] = datetime.strptime(row["startDate"], "%m/%d/%Y %I:%M %p")
            dict_to_add["end_date"] = datetime.strptime(row["endDate"], "%m/%d/%Y %I:%M %p")
            dict_to_add["client_name"] = row["clientName"]
            dict_to_add["client_id"] = row["clientId"]
            dict_to_add["industry"] = row["industry"]
            dict_to_add["is_unassigned"] = row["isUnassigned"]          
            dict_to_add["required_skills"] = json.dumps(row["requiredSkills"])
            dict_to_add["optional_skills"] = json.dumps(row["optionalSkills"])
            planning = Planning(**dict_to_add)
            db.add(planning)
        db.commit()


# Run the script
if __name__ == "__main__":
    db = next(get_db())
    import_data(db)
