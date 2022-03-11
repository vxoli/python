# Challenge 5 for LinkedIn Python challenges
# Waiting game - generate random time to wait and press enter after that time
# return seconds too fast or slow

import time
import random

def waiting_game():
	target_time = random.randint(2,4) # target time to wait
	print("\nYour target time is: {} seconds".format(target_time))
	input("Press enter to begin")
	time.perf_counter()
	input("\nPress Enter after {} seconds".format(target_time))
	elapsed = time.perf_counter() - start
	print("\nElapsed time: {0:.3f} seconds".format(elapsed))
	if elapsed == target_time: print("Perfect timing!")
	elif elapsed < target_time: print("({0:.3f} seconds too fast)".format(target_time - elapsed))
	else: print("({0:.3f} seconds too slow)".format(elapsed-target_time))

waiting_game()