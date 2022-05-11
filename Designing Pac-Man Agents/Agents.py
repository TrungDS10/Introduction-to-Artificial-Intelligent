from game import Agent
from game import Directions
import random
from util import manhattanDistance

class DumbAgent(Agent):
    def getAction(self, state):
        print("Location: ", state.getPacmanPosition()) 
        print("Actions available: ", state.getLegalPacmanActions()) 
        if Directions.EAST in state.getLegalPacmanActions():
            print("Going East.")
            return Directions.EAST 
        else:
            print("Stopping.") 
            return Directions.STOP

class RandomAgent(Agent):
    def getAction(self, state):
        print("Location: ", state.getPacmanPosition()) 
        print("Actions available: ", state.getLegalPacmanActions()) 
        availableActions = state.getLegalPacmanActions()
        action = random.choice(availableActions)
        return action

class BetterRandomAgent(Agent):
    def getAction(self, state):
        print("Location: ", state.getPacmanPosition()) 
        availableActions = state.getLegalPacmanActions()
        availableActions = availableActions[:-1]
        print("Actions available: ", availableActions) 
        action = random.choice(availableActions)
        return action

class ReflexAgent(Agent):
 
    def getAction(self, gameState):
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalPacmanActions()
        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)
        return legalMoves[chosenIndex]
        
    def evaluationFunction(self, currentgameState, action):
        successorgameState = currentgameState.generatePacmanSuccessor(action)
        newPos = successorgameState.getPacmanPosition()
        newFood = successorgameState.getFood()
        newGhostStates = successorgameState.getGhostStates()
        foodNum = currentgameState.getFood().count()
        if len(newFood.asList()) == foodNum: 
            dis = 1000
            for pt in newFood.asList():
                if manhattanDistance(pt , newPos) < dis :
                    dis = manhattanDistance(pt, newPos)
        else:
            dis = 0
        for ghost in newGhostStates: 
            dis += 4 ** (2 - manhattanDistance(ghost.getPosition(), newPos))
        return -dis