import poplib

M = poplib.POP3('mail.comcast.net')
M.user("jasonfister")
M.pass_("")
numMessages = len(M.list()[1])
for i in range(numMessages):
     for j in M.retr(i+1)[1]:
         print j