class InputFileHandling:


    def __init__(self, filep):
        self.__filepath = filep

    def writeonFile(self, a):
        fh = open(self.__filepath, 'a')
        stringFile = "data;\n"
        stringFile += "param nCourses :=" + str(len(a.classes)) +";\n"
        stringFile += "param nStudents :=" + str(len(a.students)) + ";\n"
        stringFile += "param nRooms :=" + str(len(a.rooms)) + ";\n"
        stringFile += "param nTimeOptions :=" + str(len(a.times)) + ";\n"
        fh.write(stringFile)

        stringFile = "param travelTimes :=\n"
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
        fh.write(stringFile)

        stringFile = "set SC :=\n"
        fh.write(stringFile)
        for i in a.students:
            for j in i.ids:
                stringFile = str(i.idstudent) + " " + str(j) + "\n"
                fh.write(stringFile)
        stringFile = ";\n"
        fh.write(stringFile)

        stringFile = "set CT :=\n"
        fh.write(stringFile)
        for i in a.times:
            for j in a.times:
                flag = 0
                if(j.timeid != i.timeid):
                    for x in range(0, a.nrWeeks):
                        if(j.weeks[x]!='0' and i.weeks[x] != '0'):
                            for y in range(0, a.nrDays):
                                if (j.days[y] != '0' and i.days[y] != '0'):
                                    timetotalunv = j.start + j.length
                                    timeetotaltt = i.start + i.length
                                    if(j.start <= timeetotaltt and timetotalunv >= i.start):
                                        flag = 1
                                        stringFile = str(i.timeid) + " " + str(j.timeid) + "\n"
                                        fh.write(stringFile)
                                        break
                        if(flag==1):
                            break

        stringFile = "set PTC :=\n"
        fh.write(stringFile)
        for i in a.classes:
            for j in i.availabletimes:
                stringFile = str(i.classid) + " " + str(j+1) + "\n"
                fh.write(stringFile)

        stringFile = "set PRC :=\n"
        fh.write(stringFile)
        #ALTERAR
        for i in a.rooms:
            for j in a.classes:
                for aux in j.availabletimes:
                    k = a.times[aux]
                    flag = 0
                    for z in i.unavailable:
                        for x in range(0, a.nrWeeks):
                            if (k.weeks[x] != '0' and z.weeks[x] != '0'):
                                for y in range(0, a.nrDays):
                                    if (k.days[y] != '0' and z.days[y] != '0'):
                                        timetotalunv = k.start + k.length
                                        timeetotaltt = z.start + z.length
                                        if (k.start <= timeetotaltt and timetotalunv >= z.start):
                                            flag = 1
                                            break
                            if (flag == 1):
                                break
                    if(flag == 0):
                        stringFile = str(j.classid) + " " + str(i.id) + "\n"
                        fh.write(stringFile)
                        break

        stringFile = "set RUT :=\n"
        fh.write(stringFile)
        #COLOCAR RUT NO VETOR DE TIMES
        for i in a.rooms:
            for k in a.times:
                flag = 0
                for j in i.unavailable:
                    for x in range(0, a.nrWeeks):
                        if (j.weeks[x] != '0' and k.weeks[x] != '0'):
                            for y in range(0, a.nrDays):
                                if (j.days[y] != '0' and k.days[y] != '0'):
                                    timetotalunv = j.start + j.length
                                    timeetotaltt = k.start + k.length
                                    if (j.start <= timeetotaltt and timetotalunv >= k.start):
                                        flag = 1
                                        stringFile = str(i.id) + " " + str(k.timeid) + "\n"
                                        fh.write(stringFile)
                                        break
                        if (flag == 1):
                            break
                    if (flag == 1):
                        break
        stringFile = "\n end;"
        fh.write(stringFile)
        fh.close