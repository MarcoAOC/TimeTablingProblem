from TTProblem import TTProblem
from XMLParser import XMLParser
from InputFileHandling import InputFileHandling
inputx = XMLParser("sampleproblem.xml").getInput()
tst = TTProblem(inputx)
x = InputFileHandling("aaaa.txt")
x.writeonFile(tst)

print(tst)

