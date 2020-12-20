#python3 wrapper/conector with telegram

class TelegramRepository:
	def __main__(self):
		pass
		# Todo implement as a service listening for entries

	def greetings(self, userAlias):
		command = {
			"id": "", #generate uuid
			"commandName": "command.greeting.generic",
			"userAlias": userAlias
		}