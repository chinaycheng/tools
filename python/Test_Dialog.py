 
import sys
from Tkinter import *

magic='--calling-python-from-/bin/sh--'                                                                                                                                          
"""exec" python -E "$0" "$@" """#$magic"
if __name__ == '__main__':
	print sys.argv[-1]
	print magic
	if sys.argv[-1] == '#%s' % magic:
	    del sys.argv[-1]
del magic
popupper = (len(sys.argv) > 1)

def dialog():
	win = Toplevel()
	Label(win,text = 'Do you always do what you are hold ?').pack()
	Button(win,text = 'Now Click this one',command=win.destroy).pack()
	if popupper:
		win.focus_set()
		win.grab_set()
		win.wait_window()
	print('You better obey me ...')

root = Tk()
Button(root,text = 'Click me',command = dialog).pack()
root.mainloop()
