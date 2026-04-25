extends Area2D

@onready var cars = [
	$car_1,
	$car_2
]

var num_car = 0

func _ready() -> void:
	num_car = randi_range(0, 1)
	
	for i in range(2):
		if i == num_car:
			cars[i].show()
		else:
			cars[i].hide()

func _physics_process(delta: float) -> void:
	position.y -= Global.speed * delta

func _on_body_entered(body: Node2D) -> void:
	if body.name == "Car":
		get_tree().call_deferred("change_scene_to_file", "res://scen`s/main_menu.tscn")
