screen hud:
    zorder 100
    frame:
        padding [30,30]
        has hbox:
            spacing 20
            text "[LOCATION.now]"
            text "[GAME.HUD.TODAY], [GAME.HUD.TIME]"
            text "Week: [GAME.HUD.WEEK]"
