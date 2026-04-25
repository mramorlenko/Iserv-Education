extends Control

func _on_button_pressed() -> void:
	get_tree().call_deferred("change_scene_to_file", "res://scen`s/main_scene.tscn")
	
func _on_queue_pressed() -> void:
	get_tree().quit()
