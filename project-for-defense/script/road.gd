extends TileMapLayer

@export var speed = 300

func _process(delta):
	position.y += speed * delta

	if position.y > 646:
		position.y = 0
