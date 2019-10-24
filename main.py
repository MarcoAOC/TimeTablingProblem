from TTProblem import TTProblem
from XMLParser import XMLParser
from InputFileHandling import InputFileHandling
import time
inputx = XMLParser("lums-sum17.xml").getInput()
tst = TTProblem(inputx)
x = InputFileHandling("lums-sum17.dat")
start = time.time()
x.writeonFile(tst)
end = time.time()
print(end - start)

