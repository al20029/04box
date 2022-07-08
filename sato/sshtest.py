from ssh import ssh

s = list()
s.append("a")
s.append("b")
s.append("c")
s.append("d")

argument = " " + str(len(s)) + " " + " ".join(s)
print(argument)