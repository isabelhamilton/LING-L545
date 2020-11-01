Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |    100.00 |    100.00 |    100.00 |    100.00
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |    100.00 |    100.00 |    100.00 |    100.00
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |     85.28 |     85.28 |     85.28 |     85.28
LAS        |     83.05 |     83.05 |     83.05 |     83.05
CLAS       |     77.08 |     76.97 |     77.02 |     76.97

These are the results of the training for UD_English-GUM, evaluated using the evaluation script from the 
CoNLL-17 shared task. 
The most common errors for the ten trees inspected were in matching the HEAD+DEPREL. The model had the most
trouble with NON-CORE relations, such as conj, obl, and vocative. This error was the most common among the 
trees. The unlabelled attachment score was higher than the labelled attachment score. In general, as 
indicated above, the model performed high in UAS and LAS. However, the CLAS score, which can be considered 
a more in-depth analysis, was much lower.
