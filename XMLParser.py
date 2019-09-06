import xml.dom.minidom
import Class
from Room import Room 
from Unavailable import Unavailable
from Student import Student
class XMLParser:
    def __init__(self, filepath):
        self.__doc = xml.dom.minidom.parse(filepath)
    
    def getInput(self):
        output = []
        aux = self.__getproblemopt()
        output.append(aux[0])
        output.append(aux[1])
        output.append(aux[2])
        output.append(aux[3])
        output.append(aux[4])
        output.append(aux[5])
        output.append(aux[6])
        output.append(aux[7])
        output.append(self.__arrangerooms())
        #output.append(self.getcourses())
        #output.append(self.__getstudents())

    def __getproblemopt(self):
        problem = self.__doc.getElementsByTagName("problem")
        optimization = self.__doc.getElementsByTagName("optimization")
        output = []
        output.append(problem[0].getAttribute("name"))
        output.append(int(problem[0].getAttribute("nrDays"),10))
        output.append(int(problem[0].getAttribute("nrWeeks"),10))
        output.append(int(problem[0].getAttribute("slotsPerDay"),10))
        output.append(int(optimization[0].getAttribute("time"),10))
        output.append(int(optimization[0].getAttribute("room"),10))
        output.append(int(optimization[0].getAttribute("distribution"),10))
        output.append(int(optimization[0].getAttribute("student"),10))
        return output

    def __arrangerooms(self):
        rooms = self.__doc.getElementsByTagName("rooms")
        room = rooms[0].getElementsByTagName("room")
        output = []
        for x in room:
            idaux = int(x.getAttribute("id"),10)
            capaux = int(x.getAttribute("capacity"),10)
            travelaux = {}
            unavailables =[]
            travel = x.getElementsByTagName("travel")
            unava = x.getElementsByTagName("unavailable")
            if(travel != []):
                for traveltime in travel:
                    travelaux[traveltime.getAttribute("room")] = int(traveltime.getAttribute("value"),10)
            if(unava != []):
                for unavailable in unava:
                    daysaux = unavailable.getAttribute("days")
                    startaux = int(unavailable.getAttribute("start"),10)
                    lenaux = int(unavailable.getAttribute("length"),10)
                    weekaux = unavailable.getAttribute("weeks")
                    unavailables.append(Unavailable(daysaux,startaux,lenaux,weekaux))
            output.append(Room(idaux,capaux,travelaux,unavailables))
        return output

    def __getstudents(self):
        students = self.__doc.getElementsByTagName("students")
        student = students[0].getElementsByTagName("student")
        output = []
        for x in student:
            ids = []
            idstudent = (int(x.getAttribute("id"),10))
            for y in x.getElementsByTagName("course"):
                ids.append(int(y.getAttribute("id"),10))
            output.append(Student(idstudent,ids))

        return output

