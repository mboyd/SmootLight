from operationscore.Behavior import *
import Util
import pdb
class BehaviorChain(Behavior):
    def behaviorInit(self):
        self.feedback = {} #dictionary to allow feedback of recursives
        self.hooks = self['RecursiveHooks']
        if self.hooks == None:
            self.hooks = {}
    def processResponse(self, sensorInputs, recursiveInputs):
        response = sensorInputs
        for behaviorId in self['ChainedBehaviors']:
            behavior = Util.getComponentById(behaviorId)
            if behaviorId in self.feedback:
                recurrence = self.feedback[behaviorId]
            else:
                recurrence = []
            (response,recurrence) = behavior.immediateProcessInput(response,\
                    recurrence)

            if behaviorId in self.hooks: #process recursive hook if there is one
                hookBehavior = Util.getComponentById(self.hooks[behaviorId])
#we feed its recurrence in as input to the behavior.  
                (recurrence, hookRecurrence) = \
                hookBehavior.immediateProcessInput(recurrence, \
                        [])
                if hookRecurrence != []:
                    print 'Hook recurrences are not currently supported.  Implement it yourself or bug russell'
            self.feedback[behaviorId] = recurrence 
        return response
