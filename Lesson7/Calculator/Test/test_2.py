from Lesson7.Calculator.Pages.Calcmainpage import CalMain

def test_calculator_assert(chrome_browser):
    calcmain = CalMain(chrome_browser)
    calcmain.insert_time()
    calcmain.clicking_buttons()
    assert "15" in calcmain.wait_batton_gettext()