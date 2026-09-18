from pyperclip import copy, paste



def reformat() -> None:
    """Reformat the data from clipboard (assuming of a DnD book or something similar) to more friendly formatting."""

    clipboard_data: str = paste()

    if clipboard_data:
        formatted_data = (clipboard_data
                          .replace('-\n', ' ')
                          .replace('\n', ' ')
                          .replace('-\r', '')
                          .replace('\r', '')
                          )

        copy(formatted_data)
        return None

    copy('Something went wrong or the clipboard was empty')
    return None
