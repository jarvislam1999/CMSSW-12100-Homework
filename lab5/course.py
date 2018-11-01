import json
import dateutil.parser


class Assignment(object):
    """
    Represents an assignment in the course.

    See constructor for description of attributes.
    """

    def __init__(self, assignment_id, deadline):
        """
        Constructor

        Parameters:
        - assignment_id: (string) An identifier for the assignment
        - deadline: (datetime) The assignment's deadline
        """

        self.assignment_id = assignment_id
        self.deadline = deadline


class Student(object):
    """
    Represents a student in the course.

    See constructor for description of attributes.
    """

    def __init__(self, cnetid, first_name, last_name, dropped):
        """
        Constructor

        Parameters:
        - cnetid: (string) The student's CNetID
        - first_name, last_name: (string) The student's first and last name.
        - dropped: (boolean) Whether the student dropped this class.
        """

        self.cnetid = cnetid
        self.first_name = first_name
        self.last_name = last_name
        self.dropped = dropped


###         YOUR CODE HERE         ###
###                                ###
### Implement your Team class here ###
###                                ###


###         YOUR CODE HERE               ###
###                                      ###
### Implement your Submission class here ###
###                                      ###



def time_str(t):
    """
    Converts a time in seconds to a string representation
    in days, hours, minutes, seconds.

    Parameters:
    - t: (integer) A time in seconds

    Returns: (string) A string representation.
    """
    MINUTE = 60
    HOUR = 60 * MINUTE
    DAY = 24 * HOUR
    
    t = int(t)
    days = t // DAY
    hours = (t % DAY) // HOUR
    minutes = (t % HOUR) // MINUTE
    seconds = t % MINUTE

    if days == 0:
        return "{}h {}m {}s".format(hours, minutes, seconds)
    else:
        return "{}d {}h {}m {}s".format(days, hours, minutes, seconds)


def load_data(assignments_file, students_file, teams_file):
    """
    Loads the course data from the JSON files.

    An assignment is represented as a dictionary:

      {
        "assignment_id": "pa1", 
        "deadline": "2017-01-10T02:00:00+00:00"
      }

    A student is represented as a dictionary:

      {
        "first_name": "Cliff", 
        "last_name": "Nixon", 
        "cnetid": "cnixon", 
        "dropped": false
      }

    A team is represented as a dictionary (note that it contains
    a list of submissions, also represented as dictionaries):

      {
        "students": [
          "jdunlap", 
          "ghood"
        ], 
        "team_id": "jdunlap-ghood", 
        "submissions": [
          {
            "assignment_id": "pa2", 
            "submitted_at": "2017-01-18 00:27:35.886530+00:00", 
            "extensions_used": 0
          }, 
          {
            "assignment_id": "pa3", 
            "submitted_at": "2017-01-24 02:00:11.428773+00:00", 
            "extensions_used": 0
          }
        ]
      }

    Note: When loading the data, this function will convert the
    "deadline" field (in assignments) and the "submitted_at" field
    (in submissions in teams) to Python's datetime type.


    Parameter:
    - assignments_file: (string) Path of assignments file
    - students_file: (string) Path of assignments file
    - teams_file: (string) Path of assignments file

    Returns a tuple with three values:
    - A list of assignment dictionaries
    - A list of student dictionaries
    - A list of team dictionaries
    
    """

    with open(assignments_file) as f:
        assignments_json = json.load(f)
        for a in assignments_json:
            a["deadline"] = dateutil.parser.parse(a["deadline"])

    with open(students_file) as f:
        students_json = json.load(f)

    with open(teams_file) as f:
        teams_json = json.load(f)
        for t in teams_json:
            for s in t["submissions"]:
                s["submitted_at"] = dateutil.parser.parse(s["submitted_at"])

    return assignments_json, students_json, teams_json


def create_assignment_objects(assignments_json):
    """
    Creates Assignment objects from the loaded dataset.

    Parameters:
    - assignments_json: A list of assignment dictionaries, as
      returned by load_data

    Returns: Dictionary mapping assignment identifiers to 
             Assignment objects.
    """    
    assignments = {}
    
    for a in assignments_json:
        a_obj = Assignment(a["assignment_id"], a["deadline"])
        assignments[a["assignment_id"]] = a_obj

    return assignments


def create_student_objects(students_json):
    """
    Creates Student objects from the loaded dataset.

    Parameters:
    - students_json: A list of student dictionaries, as
      returned by load_data

    Returns: Dictionary mapping CNetIDs to Student objects.
    """    
    students = {}

    for s in students_json:
        s_obj = Student(s["cnetid"], s["first_name"], s["last_name"], s["dropped"])
        students[s["cnetid"]] = s_obj

    return students


def create_team_objects(teams_json, students, assignments):
    """
    Creates Team objects from the loaded dataset.

    Parameters:
    - teams_json: A list of team dictionaries, as
      returned by load_data
    - students: Dictionary mapping CNetIDs to Student objects.
    - assignments: Dictionary mapping assignment identifiers to
                   Assignment objects.

    Returns: Dictionary mapping team identifiers to Team objects.
    """    
    teams = {}

    ### YOUR CODE HERE ###

    return teams


if __name__ == "__main__":
    assignments_json, students_json, teams_json = load_data("data/assignments.json",
                                                            "data/students.json",
                                                            "data/teams.json")

    assignments = create_assignment_objects(assignments_json)
    students = create_student_objects(students_json)
    teams = create_team_objects(teams_json, students, assignments)

    # Count the number of teams where one of the team members ended
    # up dropping the class
    teams_with_dropped = 0
    for t in teams.values():
        if t.includes_dropped():
            teams_with_dropped += 1
    print("The number of teams with dropped students is {}".format(teams_with_dropped))

    print()

    # For non-late submissions, how many seconds before the deadline
    # do teams submit their assignments (on average)
    deltas = []
    for t in teams.values():
        for s in t.submissions:
            d = s.deadline_delta()
            if d < 0:
                deltas.append(-d)

    if len(deltas) > 0:
        avg_delta = sum(deltas) / len(deltas)
        avgs = time_str(avg_delta)

        print("On average, non-late submissions are made", avgs, "before the deadline")
        








