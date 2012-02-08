Tiny Unique Identifiers

Tiny Unique Identifiers is a module for generating short ids similar to what's seen in 
popular url shorteners. Typically, with short ids a uniqueness check is needed to ensure
the id does not exist yet. I wasn't happy with this approach, so instead I thought to use
something already unique (say a primary key or just a counter) and transform it
such that  at least looks random. Tuid uses a hill cipher to do this. With a proper key,
the hill cipher can be reversed, so it still guarantees the uniqueness.

NOTE: the current cipher used is not suitable for cryptographic applications    

Dependencies: Numpy

Basic Usage:

Intialize the module with:
tuid_init(seed, length, alphabet)
	seed - random number initialization
	length - length of each id
	alphabet - possible output characters
	
then start generating ids:
tuid(index)
