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
        
        self.lstWrds = []
    
    def generatePoem(self, iterations):
        if(self.rhyme):
            return self.gpRhyme(iterations)
            
        return self.gpNoRhyme(iterations)
    
    def gpRhyme(self, iterations):
        #param: Number of iteration to run Naive-Bayes classification
        #Generate poem given specifications in constructor
        agent = MarkovAgent(self.markovMatrix, self.genSeed(0))
        poem = ""
        self.lstWrds = []
        
        #For each line of the poem
        
        lsti = 0
        for s in self.numSyl:  
            bestLine = ""
            bestScore = 0
            
            self.lstWrds += [agent.getState()[0]]
            
            #Generate line for poem and run nb classification for num of iterations
            while(bestScore < 0.7):
                tmpLine = ""
                
                sylCount = 0
                
                #Add initial state to poem, minus the last word of that state
                for i in range(agent.stateSize - 1):
                    tmpLine = agent.getState()[i] + " " + tmpLine
                    sylCount += syllables.estimate(agent.getState()[i])
                
                #Generate line with roughly correct number of syllables
                #agent.stateSize - 1] == END) implies line is finished
                while(not(sylCount > s and agent.getLastWord() == END)):
                    if(agent.getLastWord() == END):              #If finished line has too few syllables 
                        #Restart with new line with new seed
                        agent.setState(self.genSeed(lsti))
                        #print(agent.getState())
                        self.lstWrds[lsti] = agent.getState()[0]
                        
                        tmpLine = ""
                        
                        sylCount = 0
                        
                        for i in range(agent.stateSize - 1):
                            tmpLine = agent.getState()[i] + " " + tmpLine
                            sylCount += syllables.estimate(agent.getState()[i])
                    
                    tmpLine = agent.getLastWord() + " " + tmpLine #Add the last word of the agent's current state to the line
                    sylCount += syllables.estimate(agent.getLastWord()) #Update overall syllable count
                    
                    agent.transition()  #Have the agent transition to a new state
                   
                tmpScore = self.nbDist(tmpLine)
                if( tmpScore >= bestScore):  #If the current line scores better or equal to the best line
                    #best line = current line
                    bestLine = tmpLine
                    bestScore = tmpScore
                    
                agent.setState(self.genSeed(lsti))  #Initialize seed for next iteration
                    
            poem += bestLine
            poem += "\n"
            
            lsti += 1
            agent.setState(self.genSeed(lsti)) #Initialize seed for next line
            
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
            while(bestScore < 0.7):
                tmpLine = ""
                
                sylCount = 0
                
                #Add initial state to poem, minus the last word of that state
                for i in range(agent.stateSize - 1):
                    tmpLine += agent.getState()[i] + " "
                    sylCount += syllables.estimate(agent.getState()[i])
                
                #Generate line with roughly correct number of syllables
                #agent.stateSize - 1] == END) implies line is finished
                
                while(not(sylCount == s and agent.getState()[agent.stateSize - 1] == END)):
                    if(sylCount > s or agent.getLastWord() == END):    #If number of syllables has been surpassed or finished line has too few syllables 
                        #Restart with new line with new seed
                        agent.setState(self.genSeed())
                        
                        tmpLine = ""
                        
                        sylCount = 0
                        
                        for i in range(agent.stateSize - 1):
                            tmpLine += agent.getState()[i] + " "
                            sylCount += syllables.estimate(agent.getState()[i])
                    
                    tmpLine += agent.getLastWord() + " "    #Add the last word of the agent's current state to the line
                    sylCount += syllables.estimate(agent.getLastWord()) #Update overall syllable count
                    
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
        
    def genSeed(self, index = 0):
        if(self.rhyme):
            return self.gsRhyme(index, 0)
            
        return self.gsNoRhyme()
    
    def gsRhyme(self, i, j):
        if(i > 1):  #if line must rhyme with previous line
            seed = ("",) * self.markovMatrix.state_size 
            agent = MarkovAgent(self.markovMatrix, seed)
        
            seed = (BEGIN,)*(self.markovMatrix.state_size - 1)
        
            if(j >= len(pronouncing.rhymes(self.lstWrds[i % 2]))):  #If all rhyming words have been exhausted
                seed += (self.lstWrds[i % 2],)  #Use previous last word as first word in seed, [same word] rhymes with [same word]
             
            else:
                seed += (pronouncing.rhymes(self.lstWrds[i % 2])[j],)  #Use rhyming word as first word in seed
                
            agent.setState(seed)
            
            #Finish seed
            for k in range(self.markovMatrix.state_size - 1):
                agent.transition()

            seed = agent.getState()
            
            if(self.markovMatrix.move(seed) != END):    #If seed works
                return seed
                
            return self.gsRhyme(i, j+1) #Else, try next rhyming word
                
        else:
            #Same as generating seed for non rhyming line
            seed = tuple(self.markovMatrix.walk(None, self.markovMatrix.state_size))
        
            if(len(seed) != self.markovMatrix.state_size): #If seed is wrong state size
                return self.gsRhyme(i, 0)   #Retry
                
            return seed
    
    def gsNoRhyme(self):
        seed = tuple(self.markovMatrix.walk(None, self.markovMatrix.state_size))
        
        if(len(seed) != self.markovMatrix.state_size): #If seed is wrong state size
            return self.gsNoRhyme()   #Retry
        
        return seed
        
    def nbDist(self, line):
        #param: line to run Naive-Bayes classification on
        #Get NaiveBayes probability distribution for category
        return PoemUtility.classifySentence(line, self.category)
        
        #Return 0 when not testing nb classification. Training takes too long
        return 0