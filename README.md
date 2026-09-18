<h1>DnD Book Formatter</h1>

<h2>Description</h2>

A little script to help coping from DnD books (column style) into your texts. It can be truly tiresome to format sometimes.

<h2>Requirements</h2>

This script utilizes the python library pyperclip. As from its documentation for the script to work you need:<br>  
On Windows, no additional modules are needed.<br>

On Mac, the pyobjc module is used, falling back to the pbcopy and pbpaste cli
    commands. (These commands should come with OS X.).<br>

On Linux, install xclip, xsel, or wl-clipboard (for "wayland" sessions) via package manager.<br>
For example, in Debian:<br>

    sudo apt-get install xclip<br>
    sudo apt-get install xsel<br>
    sudo apt-get install wl-clipboard<br>

Otherwise on Linux, you will need the qtpy or PyQt5 modules installed.

This module does not work with PyGObject yet.

Cygwin is currently not supported.