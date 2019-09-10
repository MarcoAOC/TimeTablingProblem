from TTProblem import TTProblem
from XMLParser import XMLParser

inputx = XMLParser("sampleproblem.xml").getInput()
tst = TTProblem(inputx)
print(tst)