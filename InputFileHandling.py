class InputFileHandling:


    def __init__(self, filep):
        self.__filepath = filep

    def writeonFile(self, a):
        fh = open(self.__filepath, 'a')
        stringFile = "data;\n"
        stringFile += "param nCourses :=" + " " +";\n"
        stringFile += "param nStudents :=" + str(len(a.students)) + ";\n"
        stringFile += "param nRooms :=" + str(len(a.rooms)) + ";\n"
        stringFile += "param nTimeOptions :=" + " " + ";\n"

        stringFile += "param travelTimes :=\n"
        stringAuxCapacity = "param roomCapacity :=\n"
        for i in a.rooms:
            stringAuxCapacity += str(i.id) + " " +str(i.capacity) + "\n"
            if(len(i.travel) > 0):
                aux = i.travel.items()
                for j in aux:
                    stringFile += str(i.id) + " "
                    stringFile += str(j[0]) + " " + str(j[1]) + "\n"
        stringFile += ";\n"
        stringAuxCapacity += ";\n"
        stringFile += stringAuxCapacity

        stringFile += "set SC :\n"
        for i in a.students:
            for j in i.ids:
                stringFile += str(i.idstudent) + " " + str(j) + "\n"
        stringFile += ";\n"


        stringFile += "\n end;"
        fh.write(stringFile)
        fh.close