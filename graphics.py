import tkinter

class Window:
	def __init__(self, width,height):
		self.__root = TK()
		self.__root.title("Fibonacci Visualizer")
		self.__root.protocol("WM_DELETE_WINDOW",self.close)
		self.__canvas = Canvas(self.__root, bg='whiteb', height=height, width=width)
		self.__canvas.pack(fill=BOTH, expand=1)
		self.__running = False
		
	def redraw(self):
		self.__running = True
		while self.__running:
			self.redraw()
		print("Window closed...")

	def close(self):
		self.__running = False

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Line:
	def __init__(self,p1,p2):
		self.p1 = p1
		self.p2 = p2

	def draw(self,canvas,fill_color='black'):
		canvas.create_line(self.p1.x,self.p1.y,self.p2.x,self.p2.y,fill=fill_color,width=2):
		canvas.pack(fill=BOTH,expand=1)
		

class Box:
	def __init(self,x1,y1,x2,y2,window = None):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.win = window
