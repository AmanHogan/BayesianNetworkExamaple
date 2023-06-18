############################
#   Aman Hogan-Bailey
#   1001830469
#   4/20/2023
#   
############################

############################
# G depends of B
# F depends on both G and C
############################

import sys

debug_value = 0
filename, B_val, G_val, C_val, F_val = None, None, None, None, None

try:
    filename = sys.argv[1]
    B_val = sys.argv[2]
    G_val = sys.argv[3]
    C_val = sys.argv[4]
    F_val = sys.argv[5]

except IndexError as MissingArgs:
    pass


conditional_table, total_rows, truth_table = {}, 0, []

with open(filename, "r") as fp:  
        data = fp.readlines()
        for row in data:
            row = row.strip().replace(",","").replace(" ","")
            int_row = [int(x) for x in row]
            truth_table.append(int_row)

total_rows = len(truth_table)

# Initialize propositional values

is_b, is_c, is_f, is_g = 0, 0, 0, 0

g_and_c, g_not_c, g_and_not_c = 0, 0, 0

g_and_b, g_and_not_b = 0, 0

g_and_c_and_f, g_not_c_and_f, not_g_and_c_and_f, not_g_not_c_and_f = 0, 0, 0, 0

not_g_and_c, not_g_not_c, g_and_b_and_c = 0, 0, 0

# Loop through truth table and retrieve the propositional values related to the
# conditional probability table
for row in truth_table:
    
    # B, G, C, F
    if row[0] == 1:
        is_b+=1
    if row[1] == 1:
        is_g+=1
    if row[2] == 1:
        is_c+=1
    if row[3] == 1:
        is_f = is_f+1

    # G AND B
    if row[0] == 1 and row[1] == 1:
        g_and_b +=1
    if row[0] == 0 and row[1] == 1:
        g_and_not_b +=1

    # G AND C
    if row[1] == 1 and row[2] == 1:
        g_and_c += 1
    if row[1] == 1 and row[2] == 0:
        g_not_c += 1
    if row[1] == 0 and row[2] == 0:
        not_g_not_c += 1
    if row[1] == 0 and row[2] == 1:
        not_g_and_c += 1

    # G AND C AND F 
    if row[1] == 1 and row[2] == 1 and row[3] == 1:
        g_and_c_and_f+=1
    if row[1] == 1 and row[2] == 0 and row[3] == 1:
        g_not_c_and_f+=1
    if row[1] == 0 and row[2] == 1 and row[3] == 1:
        not_g_and_c_and_f+=1
    if row[1] == 0 and row[2] == 0 and row[3] == 1:
        not_g_not_c_and_f+=1

    # G AND B AND C
    if row[1] == 1 and row[2] == 1 and row[3] == 1:
        g_and_b_and_c+=1

# P(B)
conditional_table["P(B=t)"] = is_b/total_rows
conditional_table["P(B=f)"] = 1 - (is_b/total_rows)

# P(C)
conditional_table["P(C=t)"] = is_c/total_rows
conditional_table["P(C=f)"] = 1-(is_c/total_rows)

# P(F)
conditional_table["P(F=t)"] = is_f/total_rows
conditional_table["P(F=f)"] = 1-(is_f/total_rows)

# P(G|B)
conditional_table["P(G=t|B=t)"] = (g_and_b/total_rows)/conditional_table["P(B=t)"]
conditional_table["P(G=f|B=t)"] = 1 - conditional_table["P(G=t|B=t)"]
conditional_table["P(G=t|B=f)"] = (g_and_not_b/total_rows)/conditional_table["P(B=f)"]
conditional_table["P(G=f|B=f)"] = 1 - conditional_table["P(G=t|B=f)"] 

# P(F|G,C)
conditional_table["P(F=t|G=t,C=t)"] = (g_and_c_and_f/total_rows)/(g_and_c/total_rows)
conditional_table["P(F=f|G=t,C=t)"] = 1-conditional_table["P(F=t|G=t,C=t)"]

conditional_table["P(F=t|G=t,C=f)"] = (g_not_c_and_f/total_rows)/(g_not_c/total_rows)
conditional_table["P(F=f|G=t,C=f)"] = 1 - conditional_table["P(F=t|G=t,C=f)"]

conditional_table["P(F=t|G=f,C=t)"] = (not_g_and_c_and_f/total_rows)/(not_g_and_c/total_rows)
conditional_table["P(F=f|G=f,C=t)"] = 1 - conditional_table["P(F=t|G=f,C=t)"] 

conditional_table["P(F=t|G=f,C=f)"] = (not_g_not_c_and_f/total_rows)/(not_g_not_c/total_rows)
conditional_table["P(F=f|G=f,C=f)"] = 1 - conditional_table["P(F=t|G=f,C=f)"]

events, events_prime, events_probabilities = [], [], []

# Get the value of Bt or Bf
# Add to list of events and its value
if B_val == "Bt":
    events_probabilities.append(conditional_table["P(B=t)"])
    events.append("B=t")
else:
    events_probabilities.append(conditional_table["P(B=f)"])
    events.append("B=f")
events_prime.append(events[0])

# Get the value of Ct or Cf
# Add to list of events and its value
if C_val == "Ct":
    events_probabilities.append(conditional_table[f"P(C=t)"])
    events.append("C=t")
else:
    events_probabilities.append(conditional_table[f"P(C=f)"])
    events.append("C=f")
events_prime.append(events[1])

# Get the value of Gt or Gf and use B
# Add to list of events and its value
if G_val == "Gt":
    events_probabilities.append(conditional_table[f"P(G=t|{events[0]})"])
    events.append("G=t")
    events_prime.append(f"P(G=t|{events[0]})")

else:
    events_probabilities.append(conditional_table[f"P(G=f|{events[0]})"])
    events.append("G=f")
    events_prime.append(f"P(G=f|{events[0]})")

# Get the value of Ft or Ff and use G and C
# Add to list of events and its value
if F_val == "Ft":
    events_probabilities.append(conditional_table[f"P(F=t|{events[2]},{events[1]})"])
    events.append("F=t")
    events_prime.append(f"P(F=t|{events[2]},{events[1]})")
else:
    events_probabilities.append(conditional_table[f"P(F=f|{events[2]},{events[1]})"])
    events.append("F=f")
    events_prime.append(f"P(F=f|{events[2]},{events[1]})")

# Calculate the probability by multiplying all found probabilities
# specified in query
jpd_value = 1
for x in events_probabilities:
    jpd_value = x * jpd_value


# Print Conditional table
if B_val == None and G_val == None and C_val == None and F_val == None:
    for row in conditional_table.items():
        print(row)


# Print the Probability Table #
else:
    print(" ".rjust(8," "), "Probability Table")
    print("-".rjust(35,'-'))

    for i in range(len(events)):
        if i == 0 or i == 1:
            print(f"P({str(events_prime[i])})".ljust(15), " | ", str(round(events_probabilities[i], 10)))
        else:
            print(str(events_prime[i]).ljust(15), " | ", str(round(events_probabilities[i], 10)))

    print("-".rjust(63,'-'))

    for i in range(len(events)):
        if i == 0 or i == 1:
            print(f"P({str(events_prime[i])}) * ", end=" ")
        elif i == 2:
            print(f"{str(events_prime[i])} * ", end=" ")
        else:
            print(f"{str(events_prime[i])}", end=" ")

    print(f"= {round(jpd_value, 10)}")
    print("-".rjust(63,'-'))
    print("Final Value:".ljust(15), " = ", round(jpd_value, 10))
    print("-".rjust(35,'-'))




    