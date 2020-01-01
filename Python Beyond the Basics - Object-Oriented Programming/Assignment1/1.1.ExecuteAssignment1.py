from Assignment1 import MaxSizeLIst

a = MaxSizeLIst(3)
b = MaxSizeLIst(1)

a.push('hey')
a.push('hi')
a.push("let's go")
a.push('go')


b.push('hey')
b.push('hi')
b.push("let's go")
b.push("go")

print('a list is ', a.get_list())   #Result size should not be bigger than list size
print('b list is ', b.get_list())   #Result size should not be bigger than list size
