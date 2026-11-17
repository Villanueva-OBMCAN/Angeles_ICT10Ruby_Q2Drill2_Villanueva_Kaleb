
from pyscript import document

# Set of g7-10 students in club
grade_7 = {"Kalvin Villanueva", "Kandice Villanueva", "Ivan Recabar"}
grade_8 = {"Dustin Decierto", "Miguel Sison", "Noel Villanueva"}
grade_9 = {"Aidric Ang", "Hans Lee", "Kristoff Lumboy"}
grade_10 = {"Kaleb Villanueva", "Sean Lee", "Deion Decierto"}

# Set for new members joining da club
new_members = set()

# Add a new member to da kaleb club
def add_member(event):
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

    new_member = first_name + " " + last_name

    new_members.add(new_member)

    # Union Operator sir balajadia!
    master_set = grade_7 | grade_8 | grade_9 | grade_10 | new_members

    # Display all members and total number, sir do we really have to add comments...
    document.getElementById("results").innerHTML = f"""
        <h3>All Club Members:</h3>
        <p><b>Grade 7:</b> {', '.join(grade_7)}</p>
        <p><b>Grade 8:</b> {', '.join(grade_8)}</p>
        <p><b>Grade 9:</b> {', '.join(grade_9)}</p>
        <p><b>Grade 10:</b> {', '.join(grade_10)}</p>
        <p><b>New Members:</b> {', '.join(new_members)}</p>
        <hr>
        <h3>All Members:</h3>
        <p>{', '.join(master_set)}</p>
        <h3>Total Members: {len(master_set)}</h3>
        
        """