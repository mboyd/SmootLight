import pdb
from operationscore.Behavior import *
import util.ComponentRegistry as compReg
class ResponseMover(Behavior):
    """ResponseMover is a scaffold for behaviors that spawn 'walkers' which act autonomously on input.
    To control the movment, use the behavior as part of a BehaviorChain and add a recursive hook which
    modulates the location."""

    def processResponse(self, sensorInputs, recursiveInputs):
        return (recursiveInputs, recursiveInputs+sensorInputs)
    
