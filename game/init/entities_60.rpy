init 60 python:
  # Character creation and game-init happens here

####### CHARACTERS 
  #max
  eMAX = Entity('max', 'home')
  eMAX.set_stat('skyler_resist', 10)  #resistence stats scale 100 to -100
  eMAX.set_title('skyler','Skyler')

  #skyler
  eSKYLER = Entity('skyler','skyler')
  eSKYLER.set_stat('bug_max', 20) #how often skyler bugs max
  eSKYLER.set_title('max', 'bosslady')

  #julia
  eJULIA = Entity('julia','julia')

  ####### LOCATIONS Downstairs
  #the bar
  eBAR = Entity('bar','bar')
  eBAR.set_attr('description','The Bar')
  eBAR.set_stat('julia_debt',50000)
  eBAR.set_stat('patrons',3)
  eBAR.set_stat('beer_quality',1)

  #the downstairs hallway
  eHALL_d = Entity('hall_d','hall_d')
  eHALL_d.set_attr('description','Downstairs Hallway')

  #the store room
  eSTORE = Entity('storage','storage')
  eSTORE.set_attr('description','The Bar')

  #the office 
  eOFFICE = Entity('office', 'office')
  eOFFICE.set_attr('description','Maxs Office')

  #Max's desk in the office 
  eOFFICE = Entity('max_desk', 'max_desk')
  eOFFICE.set_attr('description','Max\'s Desk')

  #the office peephole
  ePEEP_d = Entity('peep_d','peep_d')
  ePEEP_d.set_attr('description','Glory-Stall Peephole')

  #the public bathroom
  eBANYO_d = Entity('banyo_d','banyo_d')
  eBANYO_d.set_attr('description','Public Bathroom')


####### LOCATIONS Upstairs
  #the upstairs hallway
  eHALL_u = Entity('hall_u','hall_u')
  eHALL_u.set_attr('description','Upstairs Hallway')

  #Maxs room
  eMAXSROOM = Entity('maxs','maxs')
  eMAXSROOM.set_attr('description', 'Maxs Old Bedroom')

  #Maxs peephole into skylers room
  ePEEP_u = Entity('peep_u','peep_u')
  ePEEP_u.set_attr('description','Maxs Peephole')

  #Skyler's room
  eSKYLERS = Entity('skyler_bedroom','skyler_bedroom')
  eSKYLERS.set_attr('description', 'Skylers Bedroom')

  #The upstairs shared bathroom
  eBANYO_u = Entity('banyo_u','banyo_u')
  eBANYO_u.set_attr('description', 'Upstairs Shared Bathroom')
