from app.app_logic import navigate_to

def go_back_to_home(controller):
    navigate_to(controller, "HomePage")


def go_to_decode(controller):
    navigate_to(controller, "DecodePage")
