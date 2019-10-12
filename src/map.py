def map(initial_a, final_a, initial_b, final_b, value):
	if value < initial_a or value > final_a:
		print("Valor fora dos limites da escala.")
		return

	percent_a = (value - initial_a)*100/(final_a - initial_a)

	value_b = (final_b - initial_b)*percent_a/100

	return round(value_b)