#######################
# CORE CONFIGURATIONS #
#######################
BOT_PREFIX = "?"
SEP = ", "

LOG_THRESHOLD = 0
LOG_LEVELS = ["D", "I", "W", "E"]

##########################
# CHANNEL CONFIGURATIONS #
##########################
# Enabled channels
ENABLED_CHANNELS = {
    536221565487022101,  # MemeOE >> hacker lounge
    563785796050485259,  # MemeOE >> testing channel

    292058732416991232,  # Almost a hero >> questions
    463938235425357824,  # Almost a hero >> gog questions
    710389563540897903,  # Almost a hero >> seasons questions
    293126100077379594,  # Almost a hero >> bot commands
    293123013170429952  # Almost a hero >> staff >> bot
}
# NLP-enabled channels, must be a subset of ENABLED_CHANNELS
NLP_CHANNELS = {
    536221565487022101,  # MemeOE >> hacker lounge
    563785796050485259,  # MemeOE >> testing channel

    292058732416991232,  # Almost a hero >> questions
    463938235425357824,  # Almost a hero >> gog questions
    710389563540897903  # Almost a hero >> seasons questions
}

# Move message from the following channels:
MOVE_FROM_CHANNELS = {
    827241144488427560  # Almost a hero >> vent and report
}
# Move messages to this one channel:
MOVE_TO_CHANNEL = 563785796050485259  # Almost a hero >> vent and report bot

# vent and report = 827241144488427560
# vent and report bot = 831381240958550046
######################
# NLP CONFIGURATIONS #
######################
NLP_CONFIDENCE_THRESHOLD = 0.7
