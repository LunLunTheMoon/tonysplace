init 10 python:

  '''
    The interaction class maps a forwarding label to an entity class object
    When the entity is triggerd by the user, its interaction will be triggered via the global interact label
    interactions always forward to a label
  ''' 
  INTERACTIONS = {} # global interactions dict

  class Interaction(object):
    def __init__(self, label, entity_name, v={}):
      self.label = label # the rpy label this event launches
      self.v = v #ad-hoc variables
      ENTITIES[entity_name].Q.append(self) # register the interaction with the entity's queue
      INTERACTIONS[label] = self #register with the global index of interactions

      
    # override this method to set specific requirements 
    def is_runnable(self):
      if 'enabled' in self.v:
        return self.v['enabled']
      else:
        return False

    def enable(self):
      self.v['enabled'] = True

    def disable(self):
      self.v['enabled'] = False
