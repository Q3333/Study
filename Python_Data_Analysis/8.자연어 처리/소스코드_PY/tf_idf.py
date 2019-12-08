import scipy as sp
def tf_idf(t,d,D):
    tf = float(d.count(t)) / sum(d.count(w) for w in set(d))
    idf = sp.log( float(len(D))/ (len([doc for doc in D if t in doc])) )
    return tf, idf


a, abb, abc = ['a'], ['a','b','b'], ['a','b','c']
D = [a,abb,abc]

print(tf_idf('a',a,D))
print(tf_idf('b',a,D))
print(tf_idf('b',abb,D))