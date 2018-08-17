import billionaires
list_of_billionaire = billionaires.get_billionaires()

inherited = 0
founder = 0
selfMade = 0
privatized = 0
executive = 0
print("The question is: How did Billionares Make Their Money?")
for money in list_of_billionaire:
    if money["wealth"]["type"] == "inherited":
        inherited += 1
    elif money["wealth"]["type"] == "founder non-finance":
        founder += 1
    elif money["wealth"]["type"] == "self-made finance":
        selfMade += 1
    elif money["wealth"]["type"] == "privatized and resources":
        privatized += 1
    elif money["wealth"]["type"] == "executive":
        executive += 1

import matplotlib.pyplot as plt

plt.bar(["Inherited", "Founder Non-Finance", "Self-Made Finance", "Privatized and Resources","Executive"],[inherited, founder, selfMade, privatized, executive])
plt.xlabel('Billionaires')
plt.ylabel('Type')
plt.title('Billionaire Wealth Type')
#plt.axis([0, 1.5, 0, 2])
plt.grid(True)
plt.show()
