
magicTotal = 24.0
numRange = range(1,  25)
numToChoose = 4

f = open("c24out.txt", "w")

import itertools

class oSequence:
	def __init__(self, inTotal, inHistory, inFuture):
		self.Total = inTotal
		self.History = inHistory
		self.Future = inFuture

def ComputeOperations(Seq):
	retList = []
	retList.append(oSequence(Seq.Total + Seq.Future[0], "(" + Seq.History + "+" + str(Seq.Future[0]) + ")", Seq.Future[1:len(Seq.Future)]))
	retList.append(oSequence(Seq.Total - Seq.Future[0], "(" + Seq.History + "-" + str(Seq.Future[0]) + ")", Seq.Future[1:len(Seq.Future)]))
	retList.append(oSequence(Seq.Total * Seq.Future[0], "(" + Seq.History + "*" + str(Seq.Future[0]) + ")", Seq.Future[1:len(Seq.Future)]))
	if Seq.Future[0] != 0:
		retList.append(oSequence(Seq.Total / Seq.Future[0], "(" + Seq.History + "/" + str(Seq.Future[0]) + ")", Seq.Future[1:len(Seq.Future)]))
	return retList

newSolution = True
def BuildNumbers(List_of_Seq, inNums):
        global newSolution
        for seq in List_of_Seq:
                if not seq.Future:
                        if seq.Total == magicTotal:
                                if newSolution:
                                        f.write(str(inNums) + ":\n")
                                        newSolution = False
                                                #print (seq.History)
                                f.write(seq.History + " = 24\n")
                else:
                        NewSeqList = ComputeOperations(seq)
                        BuildNumbers(NewSeqList, inNums)


def Solve(inNums):
        global newSolution
        newSolution = True
        seq_List = list(itertools.permutations(inNums))
        seq_List = set(seq_List) #remove duplicates
        for iterSeq in seq_List:
                BuildNumbers([oSequence(iterSeq[0], str(iterSeq[0]), iterSeq[1:len(iterSeq)])], inNums)



TotalSet = list(itertools.combinations_with_replacement(numRange, numToChoose))



for myiter in TotalSet:
	Solve(myiter)

f.close()
print("done")
