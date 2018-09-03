#What it is
This is a rather simple tool for generating word lists from a pre-defined set of letters and a pre-defined length of the word.

It could be used for example within word guessing games where you are provided with a set of characters (which might be more than the word has positions) and need to create a word from them.
The tool will provide you with a list of all "words" (actually combinations) there are - you could exclude some combinations and you could set combinations which need to be within the created words.

#Usage
	python3 letters.py -c <list of letters> -l <wordlength> -n [not allowed combinations] -m [required letters/combinations] 

* -c -> Characters - Required: Space seperated list of letters which could be used - if a letter could be used twice, it needs to be listed twice 
* -l -> Wordlength - Required: Length of the word(s) to generate
* -n -> Not - Optional: Space seperated list of letter-combinations which are not allowed in any word
* -m -> ? - Optional: Space seperated list of letters and letter-combinations which need to be in every word

The amount of characters provided via the -c option must at least match the word length given by -l -> it must be at least that many, but could be more, but not less


# Requirements

Following modules need to be installed:

* copy
* argparse
