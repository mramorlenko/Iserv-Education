extends Node2D

var car = preload("res://scen`s/evil_car.tscn").instantiate()
var interval = 5
var timer = 0
var cars = []

func _ready() -> void:
	create_right_car()

func create_right_car():
	var temp_car = car.duplicate()
	
	var rand_x = randf_range(630, 700)
	temp_car.position = Vector2(rand_x, 630)
	
	cars.append(temp_car)
	add_child(temp_car)

func create_left_car():
	var temp_car = car.duplicate()
	
	var rand_x = randf_range(545, 620)
	temp_car.position = Vector2(rand_x, 10)
	
	cars.append(temp_car)
	add_child(temp_car)

func _on_timer_timeout() -> void:
	timer += 1
	if timer % interval == 0:
		create_right_car()
		create_left_car()
	if timer > 5:
		interval -= 1
		timer = 0
	
