extends CharacterBody2D

func _physics_process(delta: float) -> void:

	var x = 0
	var y = 0

	if Input.is_action_pressed("move_right"):
		x = 1
	elif Input.is_action_pressed("move_left"):
		x = -1

	if Input.is_action_pressed("move_down"):
		y = 1
	elif Input.is_action_pressed("move_up"):
		y = -1

	if x != 0 and y != 0:
		x *= 0.5
		y *= 0.5

	velocity.x = x * (Global.speed / 2)
	velocity.y = y * (Global.speed / 2)
	move_and_slide()
