import random
from Bio.Cluster import kcluster

class DataGenerator:

    def __init__(self,muList,sigmaList):
        """Generates points in space, each dimension drawn from
        a Gaussian distribution (mu,sigma). Mu's and sigmas given
        as two lists. Label is a string for identification
        purposes."""
        self.muList=muList
        self.sigmaList=sigmaList

    def next(self):
        """Returns a list of values as long as len(muList), i.e. one
        value per dimension"""
        return [random.gauss(mu,sigma) for mu,sigma in zip(self.muList,self.sigmaList)]

def getExampleData2D(std):
    g1=DataGenerator([-1.0,-1.0],[std,std])
    g2=DataGenerator([1.0,1.0],[std,std])
    data=[g1.next() for _ in range(10)]+[g2.next() for _ in range(10)]+[g1.next() for _ in range(10)]
    return data

if __name__=="__main__":
    data=getExampleData2D(0.5)
    clusterValues,score,nfound=kcluster(data,nclusters=2,npass=100)
    print "Clusters:", clusterValues
    print "Score:",score
    print "Number found",nfound


        
