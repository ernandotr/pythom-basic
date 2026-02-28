import termplotlib as tpl

values = [10, 4, 15, 7]
labels = ["Java", "C++", "Python", "Go"]
fig = tpl.figure()
fig.barh(values, labels)
fig.show()