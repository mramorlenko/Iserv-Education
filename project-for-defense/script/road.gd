extends TileMapLayer

func _process(delta):
	position.y += Global.speed * delta

	if position.y > 646:
		position.y = 0
