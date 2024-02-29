def fib(index):
	n = 0
	sequence = []
	sequence.append(1)
	sequence.append(1)
	while n != index:
		sequence.append(sequence[n] + sequence[n+1])
		n += 1
	print(sequence)

def main():
	fib(6)

if __name__ == '__main__':
	main()