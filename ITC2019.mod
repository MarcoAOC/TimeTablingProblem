########################################################
#                                    ITC2019 MODEL BY GEORGE FONSECA,                                        #
########################################################

#Basic parameters
param nCourses, integer >= 0;

param nStudents, integer >= 0;

param nRooms, integer >= 0;

param nTimeOptions, integer >= 0;

########################################################
#                                                           SETS                                                                    #
########################################################

#Courses
set C := {1..nCourses};

#Students
set S  := {1..nStudents};

#Students attend courses
set SC, within S cross C;

#Rooms
set R := {1..nRooms};

#Unavailiable rooms for courses
set UR, within R cross C;

#Time options
set T  := {1..nTimeOptions};

#Conflicting times
set CT, within T cross T;

#Possible times for courses
set PTC, within C cross T;

#Possible rooms for courses
set PRC, within C cross R;

#Room unavailable times
set RUT, within R cross T;

########################################################
#                                                     PARAMETERS                                                              #
########################################################

#Travel times
param travelTimes{R, R}, integer >= 0, default 0;

#Room capacity
param roomCapacity{R}, integer >= 0, default 0;

########################################################
#                                                       VARIABLES                                                              #
########################################################

# 1 iif course c has been scheduled to time t; 0 otherwise
var x{c in C, t in T} binary;

# 1 iif course c has been assigned to room; 0 otherwise
var y{c in C, r in R} binary;

# 1 iif course c has been scheduled to time t and room r; 0 otherwise
#var z{c in C, t in T, r in R} binary;

# slack variable of conflicting courses for student s
var sConflits{s in S, c1 in C, c2 in C} binary;

########################################################
#                                                   CONSTRAINTS                                                             #
########################################################

s.t. assignTime{c in C}: sum{(c, t) in PTC} x[c, t] = 1;

s.t. assignRoom{c in C}: sum{(c, r) in PRC} y[c, r] = 1;

#s.t. assignTimeRoom{c in C}: sum{(c, t) in PTC} sum{(c, r) in PRC} z[c, t, r] = 1;

#s.t. studentConflicts{s in S, (s, c) in SC, (s, c2) in SC, (c, t) in PTC, (c2, t2) in PTC : c <> c2 and (t, t2) in CT}: x[c, t] + x[c2, t2] <= 1;
s.t. studentConflicts{s in S, (s, c) in SC, (s, c2) in SC, (c, t) in PTC, (c2, t2) in PTC : c < c2 and (t, t2) in CT}: x[c, t] + x[c2, t2] <= 1 + sConflits[s, c, c2];

s.t. roomConflicts{r in R, (c, r) in PRC, (c2, r) in PRC, (c, t) in PTC, (c2, t2) in PTC : c < c2 and (t, t2) in CT}: y[c, r] + y[c2, r] + x[c, t] + x[c2, t2] <= 3;

s.t. unavailiableTimesRooms{r in R, (c, r) in PRC, (r, t) in RUT, t2 in T : (t, t2) in CT}: x[c, t2] + y[c, r] <= 1;
s.t. directlyUnavailiableTimesRooms{r in R, (c, r) in PRC, (r, t) in RUT}: x[c, t] + y[c, r] <= 1;

########################################################
#                                           OBJECTIVE FUNCTION                                                        #
########################################################

minimize slack: sum{s in S, (s, c) in SC, (s, c2) in SC : c < c2} sConflits[s, c, c2];

solve;

printf{c in C, t in T : x[c, t] <> 0}
    "x: %d %d = %d\n", c, t, x[c, t];

printf{c in C, r in R : y[c, r] <> 0}
    "y: %d %d = %d\n", c, r, y[c, r];

printf{s in S, (s, c) in SC, (s, c2) in SC : sConflits[s, c, c2] <> 0}
    "sConflict: %d %d %d = %d\n", s, c, c2, sConflits[s, c, c2];

########################################################
#                                                 SMALL TEST DATA                                                          #
########################################################

data;

param nCourses := 4;
param nStudents := 6;
param nRooms := 2;
param nTimeOptions := 4;

param travelTimes :=
1 2 5
2 1 5
;

param roomCapacity :=
1 40
2 40;

set SC :=
1 1
1 2
2 3
2 4
3 1
3 2
4 3
4 4
5 1
5 2
6 3
6 4
;

set CT :=
1 2
1 3
2 3
2 1
3 1
3 2
;

set PTC :=
1 1
1 2
2 3
#2 4
3 1
3 2
4 3
4 4
;

set PRC :=
1 1
1 2
2 1
2 2
3 1
3 2
4 1
4 2
;

set RUT :=
#1 1
#1 2
#2 3
2 4
;

end;

########################################################
