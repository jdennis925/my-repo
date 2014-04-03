
##input your 4 numbers!
nums= [1.0, 2.0, 3.0, 4.0]
magicTotal = 24.0


from math import pow
import itertools

class oSequence:
	def __init__(self, inTotal, inHistory, inFuture):
		self.Total = inTotal
		self.History = inHistory
		self.Future = inFuture

def ComputeOperations(Seq):
	##print("COMPUTE OPERATIONS")
	retList = []
	retList.append(oSequence(Seq.Total + Seq.Future[0], Seq.History + "+" + str(Seq.Future[0]), Seq.Future[1:len(Seq.Future)]))
	retList.append(oSequence(Seq.Total - Seq.Future[0], Seq.History + "-" + str(Seq.Future[0]), Seq.Future[1:len(Seq.Future)]))
	retList.append(oSequence(Seq.Total * Seq.Future[0], Seq.History + "*" + str(Seq.Future[0]), Seq.Future[1:len(Seq.Future)]))
	if Seq.Future[0] != 0:
		retList.append(oSequence(Seq.Total / Seq.Future[0], Seq.History + "/" + str(Seq.Future[0]), Seq.Future[1:len(Seq.Future)]))
	return retList


	
def BuildNumbers(List_of_Seq):
	for seq in List_of_Seq:
		if not seq.Future:
			if seq.Total == magicTotal:
				print (seq.History)
		else:
			NewSeqList = ComputeOperations(seq)
			BuildNumbers(NewSeqList)



seq_List = list(itertools.permutations(nums))

for iterSeq in seq_List:
	BuildNumbers([oSequence(iterSeq[0], str(iterSeq[0]), iterSeq[1:len(iterSeq)])])

