class Button():
	"""
	A customizable button class that supports text, images, and hover effects.
	
	Args:
		image: Background image for the button (can be None for text-only buttons)
		pos: Tuple of (x, y) coordinates for button center position
		text_input: Text to display on the button
		font: Pygame font object for rendering text
		base_color: Default text color
		hovering_color: Text color when mouse is hovering over button
	"""
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		# Use text as image if no background image provided
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		"""
		Draws the button to the screen.
		
		Args:
			screen: Pygame surface to draw the button on
		"""
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		"""
		Checks if a given position (usually mouse cursor) is within the button's bounds.
		
		Args:
			position: Tuple of (x, y) coordinates to check
			
		Returns:
			bool: True if position is within button bounds, False otherwise
		"""
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		"""
		Changes the button's text color based on mouse position for hover effects.
		
		Args:
			position: Tuple of (x, y) coordinates (usually mouse position)
		"""
		# Change to hover color if mouse is over button
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)