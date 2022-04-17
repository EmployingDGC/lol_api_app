from pyclbr import Function
import PySimpleGUI as sg


def get_layout(
    text: str
):
    sg.theme("DarkAmber")
    
    layout = [
        [ sg.Text(text) ],
        [ sg.Push() ],
        [ sg.Push() ],
        [ sg.Button("Recarregar") ]
    ]

    layout_center = [
        [ sg.VPush() ],
        [
            sg.Push(),
            sg.Column(
                layout=layout,
                element_justification="c"
            ),
            sg.Push()
        ],
        [ sg.VPush() ]
    ]

    return layout_center


def loop(
    text: str,
    window_name: str,
    window_size: tuple[int, int],
    func_button: Function,
    **kwargs
):
    layout = get_layout(
        text=text
    )

    window = sg.Window(
        title=window_name,
        layout=layout,
        size=window_size
    )

    while True:
        event, _ = window.read()

        if event == sg.WIN_CLOSED:
            break
            
        elif event == "Recarregar":
            func_button(
                path=kwargs.get("path"),
                text=text
            )

    window.close()


if __name__ == "__main__":
    window_name = "LOL API APP"

    window_size = (300, 200)

    loop(
        text="teste",
        window_name=window_name,
        window_size=window_size,
        func_button=lambda path, text: print(path, text),
        path="./pdl.txt"
    )
