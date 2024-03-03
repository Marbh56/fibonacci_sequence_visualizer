from tkinter import *
from tkinter import ttk

def fib(index):
	n = 0
	sequence = []
	sequence.append(1)
	sequence.append(1)
	while index != len(sequence):
		sequence.append(sequence[n] + sequence[n+1])
		n+=1
	print(sequence)

def fib_callback():
	return fib(int(num_of_fib_iters.get()))


def main():
	fib(10)
	root = tk.Tk()
	num_of_fib_iters = Entry(root)
	num_of_fib_iters.pack()
	b = Button(root, text="Num of Iterations to calculate the Fibonacci Sequence?", command=fib_callback)
	b.pack()
	


if __name__ == "__main__":
	main()