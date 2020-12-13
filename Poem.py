from MarkovAgent import MarkovAgent
from markov import MarkovMatrix, ReverseMarkovMatrix
from PoemUtility import PoemUtility
import syllables
import pronouncing

BEGIN = "___BEGIN__"
END = "___END__"

class Poem:
    def __init__(self, markovMatrix, numSyl, category, rhyme):
        #params: markov probability matrix, number of syllables per line, category of poem (period_genre), bool that dictates if poem will have rhyming
        self.markovMatrix = markovMatrix
        self.numSyl = numSyl
        self.category = category
        self.rhyme = rhyme
    
    def generatePoem(self, iterations):
        if(self.rhyme):
            return self.gpRhyme(iterations)
            
        return self.gpNoRhyme(iterations)
    
    def gpRhyme(self, iterations):
        #param: Number of iteration to run Naive-Bayes classification
        #Generate poem given specifications in constructor
        agent = MarkovAgent(self.markovMatrix, self.genSeed())
        poem = ""
        lstWords = [agent.getState(0)]
        
        #For each line of the poem
        for s in self.numSyl:  
            bestLine = ""
            bestScore = 0
            
            #Generate line for poem and run nb classification for num of iterations
            for j in range(iterations):
                tmpLine = ""
                
                sylCount = 0
                
                #Add initial state to poem, minus the last word of that state
                for i in range(len(agent.getState()) - 1):
                    tmpLine = agent.getState()[len(agent.getState()) - 1] + " " + tmpLine
                    sylCount += syllables.estimate(agent.getState()[i])
                
                #Generate line with roughly correct number of syllables
                #len(agent.getState()) - 1] == END) implies line is finished
                while(not(sylCount == s and agent.getState()[len(agent.getState()) - 1] == END)):
                    if(sylCount > s or agent.getState()[len(agent.getState()) - 1] == END):    #If number of syllables has been surpassed or finished line has too few syllables 
                        #Restart with new line with new seed
                        agent.setState(self.genSeed())
                        
                        tmpLine = ""
                        
                        sylCount = 0
                        
                        for i in range(len(agent.getState()) - 1):
                            tmpLine = agent.getState()[i] + " " + tmpLine
                            sylCount += syllables.estimate(agent.getState()[i])
                    
                    tmpLine = agent.getState()[len(agent.getState()) - 1] + " " + tmpLine #Add the last word of the agent's current state to the line
                    sylCount += syllables.estimate(agent.getState()[len(agent.getState()) - 1]) #Update overall syllable count
                    
                    agent.transition()  #Have the agent transition to a new state
                   
                tmpScore = self.nbDist(tmpLine)
                if( tmpScore >= bestScore):  #If the current line scores better or equal to the best line
                    #best line = current line
                    bestLine = tmpLine
                    bestScore = tmpScore
                    
            poem += bestLine
            poem += "\n"
            
        return poem
    
    def gpNoRhyme(self, iterations):
        #param: Number of iteration to run Naive-Bayes classification
        #Generate poem given specifications in constructor
        agent = MarkovAgent(self.markovMatrix, self.genSeed())
        poem = ""
        
        #For each line of the poem
        for s in self.numSyl:  
            bestLine = ""
            bestScore = 0
            
            #Generate line for poem and run nb classification for number of iterations
            for j in range(iterations):
                tmpLine = ""
                
                sylCount = 0
                
                #Add initial state to poem, minus the last word of that state
                for i in range(len(agent.getState()) - 1):
                    tmpLine += agent.getState()[i] + " "
                    sylCount += syllables.estimate(agent.getState()[i])
                
                #Generate line with roughly correct number of syllables
                #len(agent.getState()) - 1] == END) implies line is finished
                while(not(sylCount == s and agent.getState()[len(agent.getState()) - 1] == END)):
                    if(sylCount > s or agent.getState()[len(agent.getState()) - 1] == END):    #If number of syllables has been surpassed or finished line has too few syllables 
                        #Restart with new line with new seed
                        agent.setState(self.genSeed())
                        
                        tmpLine = ""
                        
                        sylCount = 0
                        
                        for i in range(len(agent.getState()) - 1):
                            tmpLine += agent.getState()[i] + " "
                            sylCount += syllables.estimate(agent.getState()[i])
                    
                    tmpLine += agent.getState()[len(agent.getState()) - 1] + " "    #Add the last word of the agent's current state to the line
                    sylCount += syllables.estimate(agent.getState()[len(agent.getState()) - 1]) #Update overall syllable count
                    
                    agent.transition()  #Have the agent transition to a new state
                    
                tmpScore = self.nbDist(tmpLine)
                if( tmpScore >= bestScore):  #If the current line scores better or equal to the best line
                    #best line = current line
                    bestLine = tmpLine
                    bestScore = tmpScore
                    
                agent.setState(self.genSeed())  #Initialize seed for next iteration/line
                    
            poem += bestLine
            poem += "\n"
            
        return poem
        
    def nbDist(self, line):
        #param: line to run Naive-Bayes classification on
        #Get NaiveBayes probability distribution for category
        score = PoemUtility.classifySentence(line, self.category)
        return score
        
        #Return 0 when not testing nb classification. Training takes too long
        return 0
        
    def genSeed(self):
        if(self.rhyme):
            return self.gsRhyme()
            
        return self.gsNoRhyme()
    
    def gsRhyme(self):
        seed = tuple(self.markovMatrix.walk(None, self.markovMatrix.state_size))
        
        
    
    def gsNoRhyme(self):
        seed = tuple(self.markovMatrix.walk(None, self.markovMatrix.state_size))
        
        if(len(seed) == 0): #If seed is empty
            return self.genSeed()   #Retry
        
        return seed