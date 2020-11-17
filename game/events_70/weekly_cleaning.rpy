init 70 python:
  class WeeklyCleaning(Event):
    #Tuesday cleaning

    def is_runnable(self):
      return GAME.time == 'Morning'

    def run(self):
      renpy.jump(self.name)

  #invocation:
  WeeklyCleaning('weekly_cleaning','dow', days=["Tuesday"],v={'enabled': True}).schedule(GAME)
