import xml.dom.minidom
from Clazz import Clazz
from Room import Room 
from Unavailable import Unavailable
from Student import Student
from Distribution import Distribution
from Course import Course
from Config import Config
from Time import Time
from Subpart import Subpart
import re
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
        output.append(self.__getdistributions())
        output.append(self.__getstudents())
        return output

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

    def __getdistributions(self):
        distributions = self.__doc.getElementsByTagName("distributions")
        distribution = distributions[0].getElementsByTagName("distribution")
        output = []
        retester = re.compile('\(([^)]+)\)')
        for x in distribution :
            completestring = x.getAttribute("type")
            auxiliarstring = retester.search(completestring)
            params = None
            if(auxiliarstring != None):
                params = auxiliarstring.group(0)[1:-1]
                firstbrack = auxiliarstring.regs[0][0]
                name = completestring[0:firstbrack]
            else:
                name = completestring
            classesids = []
            for classaux in x.getElementsByTagName("class"):
                classesids.append(int(classaux.getAttribute("id"),10))
            reqpen = x.getAttribute("required")
            if(reqpen == ''):
                reqpen = int(x.getAttribute("penalty"),10)
            output.append(Distribution(name,params,classesids,reqpen))
        return output
    def getcourses(self):
        courses = self.__doc.getElementsByTagName("courses")
        coursex = courses[0].getElementsByTagName("course")
        output = []
        for course in coursex:
            y = course.getElementsByTagName("config")
            courseid = int(course.getAttribute("id"),10)
            outputconfig = []
            for config in y:
                z = config.getElementsByTagName("subpart")
                configid = int(config.getAttribute("id"),10)
                outputsubpart = []
                for subpart in z:
                    w = subpart.getElementsByTagName("class")
                    subpartid = int(subpart.getAttribute("id"),10)
                    outputclass = []
                    for classx in w: 
                        classid = int(classx.getAttribute("id"),10)
                        classlimit = int(classx.getAttribute("limit"),10)
                        aux = classx.getElementsByTagName("room")
                        rooms = {}
                        for room in aux:
                            idaux = int(room.getAttribute("id"),10)
                            penaux = int(room.getAttribute("penalty"),10)
                            rooms[idaux] = penaux
                        aux = classx.getElementsByTagName("time")
                        times = []
                        for time in aux:
                            days = room.getAttribute("days")
                            weeks = room.getAttribute("weeks")
                            start = int(time.getAttribute("start"),10)
                            length = int(time.getAttribute("length"),10)
                            penaux = int(time.getAttribute("penalty"),10)
                            times.append(Time(days,start,length,weeks,penaux))
                        outputclass.append(Clazz(classid,classlimit,rooms,times)) 
                    outputsubpart.append(Subpart(subpartid,outputclass))     
                outputconfig.append(Config(config,outputsubpart))
            output.append(Course(courseid,outputconfig))  
        return output    


a = XMLParser("sampleproblem.xml")
x = a.getcourses()