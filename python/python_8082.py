# Map-summing items in a multidimensional array
&gt;&gt;&gt; c=[ (0.5, 0.6, 0.7), (0.1, 0.9, 0.8), (0.9, 1.0, 0.4),(0.5, 0.6, 0.7), (0.1, 0.9, 0.8), (0.9, 1.0, 0.4),(0.5, 0.6, 0.7), (0.1, 0.9, 0.8), (0.9, 1.0, 0.4)]
&gt;&gt;&gt; [ sum([t[i] for t in c]) for i in range(len(c[0]))]
[4.5, 7.5, 5.6999999999999993]
