from api.exceptions.messageContainsBlackListedWordException import MessageContainsBlackListedWordException

blackListedWords = ["Hitler", "Fuck"]

def checkForBlackListedWords(description):
    for item in blackListedWords:
        if item.lower() in description.lower():
            raise MessageContainsBlackListedWordException("Your message contains a blacklisted word. Please don't do that.")
    pass