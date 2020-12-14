class Response:
	def __init__(self, id: str, message: str):
		self._id = null
		self._message = null

	@property
	def id(self) -> str:
		return self._id
	
	@property
	def message(self) -> str:
		return self._message
