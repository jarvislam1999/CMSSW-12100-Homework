'''
Sample problem: Paper tracking
'''

class Review:
    ''' Class for representing reviews '''
    def __init__(self, paper, reviewer_name, score, comments):
        self.paper = paper
        self.reviewer_name = reviewer_name
        self.score = score
        self.comments = comments

    def get_reviewer_name(self):
        return self.reviewer_name

    def get_score(self):
        return self.score

    def get_comments(self):
        return self.comments


class Reviewer(object):
    def __init(self, name, university, areas):
        self.name = name
        self.university = university
        self.areas = areas
    def add_area(self, area):
        self.areas.append(area)
    def remove_area(self, area):
        self.remove(area)


class Paper:
    ''' Class for representing papers '''
    def __init__(self, title, authors, areas):
        self.title = title
        self.authors = authors[:]
        self.areas = set(areas)
        self.reviews = []

    def add_review(self, reviewer_name, score, comments):
        '''
        Creates a Review object and adds it to the list of reviews
        '''

        # Adjust score if necessary
        if score < 0:
            score = 0
        elif score > 5:
            score = 5

        r = Review(self, reviewer_name, score, comments)
        self.reviews.append(r)

    def overlap(self, reviewer):
        for area in reviewer.areas:
            if (area not in self.areas):
                return False
        return True


class Journal:
    ''' Class for representing journals '''
    def __init__(self, name):
        self.name = name
        self.papers = set()

    def add_paper(self, paper):
        '''
        Adds a paper to the journal.  Return false if the Paper object
        was already added.  Return true if the Paper was added
        successfully.
        '''
        if paper in self.papers:
            return False

        self.papers.add(paper)
        return True

    def add_review(self, paper, reviewerName, score, comments):
        '''
        Adds a review to a paper in the journal.
        Return false if the Paper object is not part of the journal.
        Return true if the review was added successfully.
        '''

        if paper not in self.papers:
            return False

        paper.add_review(reviewerName, score, comments)
        return True

    def get_papers_above(self, score):
        '''
        Returns a List of Paper objects with an average review score
        greater than or equal to the provided "score" parameter
        '''

        papers_above = []
        for paper in list(self.papers):
            if (len(paper.reviews) == 0):
                continue
            if (sum([review.get_score() for review in paper.reviews])/len(paper.reviews) >= score):
                papers_above.append(paper)
        return papers_above


def test_1():
    ''' Test code '''

    j = Journal("Journal of Computer Science Applications")

    p1 = Paper("A Trie-based Method for Word Autocompletion",
               ["Susan Calvin", "Grace Kingston-Hughes"],
               ["Data Structures", "Text Processing"])

    p2 = Paper("A Novel Approach to Linear Regression",
               ["Jane Smith"],
               ["Statistics"])

    p3 = Paper("Thanks Obama: An Application for Analyzing ACA Data",
               ["Joanna Lovelace", "Sandy Hopper"],
               ["Visualization", "Healthcare"])

    p4 = Paper("A New Algorithm for Finding Crossing Orders",
               ["Diana Liskov", "Ada Lynch"],
               ["Data Structures", "Finance"])

    rv = j.add_paper(p1)
    assert rv, "Failed add of paper p1"

    rv = j.add_paper(p2)
    assert rv, "Failed add of paper p2"

    rv = j.add_paper(p3)
    assert rv, "Failed add of paper p3"

    rv = j.add_paper(p4)
    assert rv, "Failed add of paper p4"

    rv = j.add_paper(p1)
    assert not rv, "Failed duplicated add of paper p1"

    rv = j.add_review(p1, "REVIEWER 1", 4, "Excellent!")
    assert rv, "Failed add of review 1 for p1"

    rv = j.add_review(p1, "REVIEWER 2", 5, "Tres magnifique!")
    assert rv, "Failed add of review 2 for p1"

    rv = j.add_review(p1, "REVIEWER 3", 4, "Quite an achievement!")
    assert rv, "Failed add of review 3 for p1"

    rv = j.add_review(p2, "REVIEWER 4", 3, "Needs improvement")
    assert rv, "Failed add of review 4 for p1"

    rv = j.add_review(p2, "REVIEWER 1", 4, "Quite good")
    assert rv, "Failed add of review 1 for p2"

    rv = j.add_review(p2, "REVIEWER 2", 3, "I've seen worse")
    assert rv, "Failed add of review 2 for p2"

    rv = j.add_review(p3, "REVIEWER 3", 2, "Reject!")
    assert rv, "Failed add of review 3 for p3"

    rv = j.add_review(p3, "REVIEWER 4", 1, "Intolerable!")
    assert rv, "Failed add of review 4 for p3"

    rv = j.add_review(p3, "REVIEWER 1", 1, "Did not cite my paper!")
    assert rv, "Failed add of review 1 for p3"

    rv = j.get_papers_above(3.0)
    msg = "Failed getting papers above 3.0. Expected: 2  Got: {}.".format(len(rv))
    assert len(rv) == 2, msg
    msg = "Failed getting papers above 3.0. Missing: A Novel Approach to Linear Regression"
    assert p2 in rv, msg
    msg = "Failed getting papers above 3.0. Missing: A Trie-based Method for Word Autocompletion"
    assert p1 in rv, msg

    rv = j.get_papers_above(4.0)
    msg = "Failed getting papers above 4.0. Expected: 1  Got: {}.".format(len(rv))
    assert len(rv) == 1, msg
    msg = "Failed getting papers above 4.0. Missing: A Trie-based Method for Word Autocompletion"
    assert p1 in rv, msg


if __name__ == "__main__":
    test_1()
