from app.app_logic import navigate_to

def go_to_encode(controller):
    navigate_to(controller, "EncodePage")

def go_back_to_home(controller):
    navigate_to(controller, "HomePage")
