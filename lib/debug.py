#!/usr/bin/env python3

from dog import Dog
import ipdb

# Create a Dog instance to inspect
my_dog = Dog(name="Buddy", breed="Beagle")

# Set a trace for debugging
ipdb.set_trace()

# Example action after debugging
print(f"Dog's name: {my_dog.name}, Breed: {my_dog.breed}")