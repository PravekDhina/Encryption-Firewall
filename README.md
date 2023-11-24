# Encryption-Firewall
1. Alternative Method of Public-Key Encryption

Pseudo Code 

Approach: The provided code implements an alternative method of public-key encryption. The public key consists of a list of integers 'h', while the private key consists of three integers 'e', 'q', and 'w'. To encrypt a message, the message is first converted into a sequence of bits. These bits are then split into blocks of size 'len(h)'. Each block is then encrypted by multiplying it, component-wise, with the corresponding elements of 'h'. The resulting encrypted blocks are then transmitted to the receiver. To decrypt the ciphertext, the receiver first computes the inverse of 'w' modulo 'q'. This inverse is then used to multiply each ciphertext block, modulo 'q'. The resulting products are then converted back into a sequence of bits, which is finally converted back into the original plaintext message.

Public Key Generation:
Generate a list 'e' of n random integers within a specified range.
Generate a random prime number 'q' greater than 2en.
Generate a random integer 'w' such that gcd(w, q) = 1.
Compute 'h' by multiplying corresponding elements of 'e' and 'w' modulo 'q'.
Public key = h, Private key = (e, q, w).

Encryption:
Convert plaintext to bit blocks of size len(h).
For each block, calculate the sum of corresponding elements of block and h modulo q.
Return list of encrypted blocks.

Decryption:
Compute w_inv = pow(w, -1, q).
For each encrypted block:
Calculate c_prime = block * w_inv modulo q.
Iterate through 'e' in reverse order:
If c_prime >= e_i, subtract e_i from c_prime and append 1 to 'bits'.
Else, append 0 to 'bits'.
Convert bits to plaintext by chunking into 8-bit characters.
Return plaintext.

Testing:
Two sets of public-private key pairs are generated for testing with n value of 16 and 32
Same text is given as input in both the cases. The text has over 500 characters. 

Observations: 
1.	16 and 32 random integers are generated respectively. Easy key has 16 and 32 integers with the property that each element is greater than the sum of the previous elements. 
2.	q and w generated are co-primes. 
3.	Public key, h, has 16 and 32 integers respectively, generated with the property hi = (w𝑒𝑖 mod q)
4.	Ciphertext is generated with public key. 
5.	The decryption code has worked successfully and regenerated the original plaintext message. 

Example 1: 

Enter the number of random integers to be generated: 16
Public key: [516196, 444986, 827625, 800730, 800424, 247858, 41867, 591067, 478897, 806511, 758502, 66215, 791046, 273723, 48976, 391655]
Private key: ([17, 18, 49, 110, 207, 433, 836, 1677, 3376, 6742, 13496, 26976, 53967, 107916, 215839, 431686], 863383, 792173)

Example 2: 

Enter the number of random integers to be generated: 32
Public key: [134410881130, 74411689584, 28154812818, 146308412955, 69547523977, 42560194874, 5513000919, 66499677397, 114731524027, 23321210372, 132115692076, 142222451286, 13108174099, 26216348198, 15226851604, 31123886466, 61577589674, 165556723385, 173909218886, 26873916243, 163354817088, 66434487451, 10860042036, 70657693870, 98913843703, 76488937798, 117782580578, 52886853486, 118845838494, 128754875644, 99635340146, 126869540482]
Private key: ([56, 78, 171, 309, 653, 1318, 2595, 5234, 10463, 20908, 41849, 83655, 167351, 334702, 669365, 1338759, 2677489, 5354980, 10709965, 21419919, 42839868, 85679732, 171359421, 342718865, 685437728, 1370875442, 2741750932, 5483501814, 10967003670, 21934007339, 43868014654, 87736029317], 175472058651, 108936801344)

Plaintext
Enter the message: To Amrutha: As I pen this letter, I'm filled with a mix of anticipation and uncertainty about the path that lies ahead. Yet, one thing remains constant: my unwavering belief in your resilience and potential.  Remember the dreams that ignite your soul, the aspirations that set your heart ablaze. Hold them close, for they are the beacon that will guide you through life's uncharted waters. Embrace the inevitable setbacks as opportunities for growth, stepping stones to propel you towards greater heights.  And above all, never cease to learn, never stop growing. Embrace new experiences, challenge your perspectives, and expand your horizons. The world is a vast and wondrous place, brimming with endless possibilities waiting to be explored.

*Ciphertext is added in the appendix


2. Firewall Rules Application

Pseudo Code

•	Create a Firewall class with an empty list of rules.

•	Function add_rule(rule_num, direction, addr):
o	Create a new rule with the given rule number, direction, and address.
o	Add the new rule to the list of rules.
o	Sort the rules based on their rule numbers.
•	Function remove_rule(rule_num, direction=None):
o	Remove a rule from the list based on the rule number and direction (if specified).
•	Function list_rules(rule_num=None, direction=None, addr=None):
o	Create a filtered list of rules based on the provided rule number, direction, and address.
o	Return the filtered list.
•	Function sort_rules():
o	Sort the list of rules based on their rule numbers.
•	Function parse_ipv4_network(addr):
o	Parse and return an IPv4 network from the provided address.
•	Function parse_ipv4_address(addr):
o	Parse and return an IPv4 address from the provided address.
•	In the main program:
o	Create an instance of the Firewall class.
o	Parse command-line arguments to determine the action, rule number, direction, and address.
•	If the action is 'add':
o	If no address is provided, print an error.
o	Otherwise, call add_rule with the provided rule number, direction, and address.
•	If the action is 'remove':
o	Call remove_rule with the provided rule number and direction.
•	If the action is 'list':
o	Call list_rules with the provided rule number, direction, and address.
o	Print the details of the filtered rules.




Appendix

1. Alternative Method of Public-Key Encryption

Example 1
Plaintext
To Amrutha: As I pen this letter, I'm filled with a mix of anticipation and uncertainty about the path that lies ahead. Yet, one thing remains constant: my unwavering belief in your resilience and potential.  Remember the dreams that ignite your soul, the aspirations that set your heart ablaze. Hold them close, for they are the beacon that will guide you through life's uncharted waters. Embrace the inevitable setbacks as opportunities for growth, stepping stones to propel you towards greater heights.  And above all, never cease to learn, never stop growing. Embrace new experiences, challenge your perspectives, and expand your horizons. The world is a vast and wondrous place, brimming with endless possibilities waiting to be explored.

Keys
Enter the number of random integers to be generated: 32
Public key: [134410881130, 74411689584, 28154812818, 146308412955, 69547523977, 42560194874, 5513000919, 66499677397, 114731524027, 23321210372, 132115692076, 142222451286, 13108174099, 26216348198, 15226851604, 31123886466, 61577589674, 165556723385, 173909218886, 26873916243, 163354817088, 66434487451, 10860042036, 70657693870, 98913843703, 76488937798, 117782580578, 52886853486, 118845838494, 128754875644, 99635340146, 126869540482]
Private key: ([56, 78, 171, 309, 653, 1318, 2595, 5234, 10463, 20908, 41849, 83655, 167351, 334702, 669365, 1338759, 2677489, 5354980, 10709965, 21419919, 42839868, 85679732, 171359421, 342718865, 685437728, 1370875442, 2741750932, 5483501814, 10967003670, 21934007339, 43868014654, 87736029317], 175472058651, 108936801344)

Ciphertext
Encrypted message: [881660157394, 1473405391329, 851455390124, 981034994445, 1343879862804, 1294838171461, 1472154467061, 1438662647763, 1144989794938, 1270036959836, 1209020163610, 1347772953555, 832135935174, 1128320117843, 978617279563, 1538317776337, 1322309941157, 1177623736015, 902737466448, 1438802676656, 1428374151701, 1262197874154, 1493285704555, 1169442505142, 1031222984121, 1009802653170, 909231741836, 1364564560348, 1167432295593, 883060576484, 1367702081706, 1299278198981, 1294838171461, 968894141782, 1287622219377, 1158882931866, 1320446017844, 1200979414817, 972175074079, 1403356204706, 1326912046164, 916007288296, 1429762187149, 1397741416160, 1523601997821, 1213599443404, 1529798700848, 1292494263701, 1117857284598, 1352500396774, 1294375894339, 896168750583, 1254225222668, 1237733604693, 1132395311187, 1096436208479, 1511763356757, 1175992332967, 1546560530184, 1302526465652, 1523601997821, 1502738315914, 1074177316376, 1054320890948, 1319403027469, 1313709948507, 1062315350916, 1246017070425, 1224636275720, 1523601997821, 1339220302213, 1032509311680, 1230126239519, 1069053723404, 1277353017206, 1304747208611, 1276145501417, 1472638409681, 1222601609792, 1304747208611, 1273955156956, 1089633769584, 1143963985558, 1563134375693, 1175992332967, 1377829781530, 1132876139532, 1413400114865, 1523601997821, 1201644986117, 1442222010465, 1219056424958, 981949328015, 1302024099024, 1364622665604, 1112675530081, 1355075400383, 1149281902366, 1251865743804, 1089633769584, 1458728092638, 1500120628944, 1358881115163, 1224636275720, 1255246207910, 1336790174380, 882765206009, 1535130238860, 1292617428502, 1152207419529, 1323013598441, 1385705408468, 991126712128, 1117710477719, 1053802726331, 1837043850981, 1105458932869, 1131936162167, 1502776609409, 1523601997821, 1605221625600, 1361516067349, 1083254636586, 1316293717331, 1113244910309, 1292122050594, 655158921830, 896890750562, 1242721988639, 1225843081056, 1302389447093, 1004707729390, 1271143206461, 1444893525856, 1020615420013, 985857296628, 1326494681787, 1210274450278, 1307786746837, 1449779058314, 980532356927, 1106476569381, 965194524487, 1065039021733, 1338629695522, 1472122575541, 1200597206966, 1053904271553, 1427501342250, 1096699482428, 1136668969095, 1312515205509, 1258548978152, 1527937633394, 1224009432546, 1119804723300, 1338577387137, 1523601997821, 1557701480853, 1662988710069, 1096538460015, 1026166078130, 1423632084426, 1324384095071, 864173408270, 1063633198146, 902737466448, 1507701634228, 1472595371416, 1216210472220, 908837421833, 1563185934884, 1610489425157, 1347772953555, 1322295414707, 1290109498103, 1487720257405, 1532282997228, 1382766829256, 1017031015886, 1499400278196, 1053802726331, 1000363350454, 1186304400697, 1441203034826, 807838190780]

Firewall rules conflict:

• Issue- During addition rules. ‘add_rule’ method adds a new rule without checking the 
existing rule.

• When a new rule overlaps an existing rule, there are possibilities of rule conflicts.

Possible Solution:

• Add calidation mechanism in ‘add_rule’ method.

• Check for existing rules and directions prior to adding any new rule.
