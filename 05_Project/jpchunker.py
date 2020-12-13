import sys

# dictionary of chunk patterns
chunk_patterns = {
    'NOUN': 'NP',
    'ADJ NOUN': 'NP',
    'VERB': 'VP',
    'NOUN ADP VERB': 'VP',
    'SCONJ': 'CC',
    'PUNCT': 'PUNCT',
    'NOUN ADP': 'PP',
    'ADV': 'ADVP',
    }

# dictionary of words in the sentence with POS tags
parts_of_speech_dict = {
    '私': 'NOUN',
    'は': 'ADP',
    'ご飯': 'NOUN',
    'を': 'ADP',
    '食べた': 'VERB',
    '。': 'PUNCT',
    '忙しい': 'ADJ',
    'から': 'SCONJ',
    '、': 'PUNCT',
    '行けない': 'VERB',
    'ここ': 'NOUN',
    'に': 'ADP',
    'ある': 'VERB',
    '面白い': 'ADJ',
    'こと': 'NOUN',
     'だ': 'VERB',
    '早く': 'ADV',
    '手': 'NOUN',
    '洗う': 'VERB'
}


def find_chunk_pattern (parts_of_speech_list, parsed_chunks_list, index_modifier):
	options = []
	chunk_pattern_tag = ''
	counter = 0
	for part_of_speech in parts_of_speech_list:
		counter = counter + 1
		updated_tag = chunk_pattern_tag + ' ' + part_of_speech
		chunk_pattern_tag = updated_tag.strip()
		if chunk_pattern_tag in chunk_patterns:
			modified_counter = counter + index_modifier
			remaining_pos = parts_of_speech_list[counter:]
			chunk_tag = chunk_patterns[chunk_pattern_tag]
			new_parsed_chunks_list = parsed_chunks_list.copy()
			new_parsed_chunks_list.append(chunk_tag)
			option = (modified_counter,
                                  remaining_pos,
                                  new_parsed_chunks_list)
			options.append(option)
	return options


def find_tuple_with_biggest_index(options):
	biggest_index = -1
	best_option = ()
	for tup in options:
		current_index = tup[0]
		if current_index > biggest_index:
			biggest_index = current_index
			best_option = tup
	return best_option


def pattern(sentence):
	pos = []
	for word in sentence:
		pos.append(parts_of_speech_dict[word])
	options = find_chunk_pattern(pos, [], 0)
	chunk_keys = []
	while len(chunk_keys) == 0:
		biggestIndex = -1

		best_option = find_tuple_with_biggest_index(options)

		options.remove(best_option)

		modified_index = best_option[0]
		remaining_pos = best_option[1]
		chunk_pattern_list = best_option[2]

		if len(remaining_pos) == 0:
			chunk_keys = chunk_pattern_list

		options = options + find_chunk_pattern(remaining_pos, chunk_pattern_list, modified_index)
	return chunk_keys


sentence1 = ['私','は','ご飯','を','食べた','。']
sentence2 = ['ここ','に','ある','。']
sentence3 = ['面白い','こと','だ','。']
sentence4 = ['早く','手','を','洗う','。']

print (pattern(sentence1))

