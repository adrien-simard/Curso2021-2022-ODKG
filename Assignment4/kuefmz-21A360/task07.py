# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U8_z3qe_QHb5fpreXr_5W8xmshvrnE7g

**Task 07: Querying RDF(s)**
"""

#!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"

"""Read the RDF file"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/resources/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""


#RDFLib
print("TASK 7.1 - RDFLib")
ns = Namespace("http://somewhere#")
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(s)

#SPARQL
print("TASK 7.1 - SPARQL")
from rdflib.plugins.sparql import prepareQuery
q = prepareQuery('''
  SELECT ?x 
  WHERE {?x rdfs:subClassOf ns:Person }''', 
  initNs = {'rdfs':RDFS, 'ns':ns} )

for i in g.query(q):
    print(i.x)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

#RDFList
print("TASK 7.2 - RDFLib")
for s, p, o in g.triples((None, RDF.type, ns.Person)):
  print(s)

for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
  for s1, _, _ in g.triples((None, RDF.type, s)):
    print(s1)

#SPARQL
print("TASK 7.2 - SPARQL")
from rdflib.plugins.sparql import prepareQuery
q = prepareQuery('''
  SELECT ?x 
  WHERE {{?x rdf:type ns:Person } UNION 
        {?s rdfs:subClassOf ns:Person. 
         ?x rdf:type ?s}}''', 
  initNs = {'rdf':RDF, 'ns':ns, 'rdfs':RDFS} )

for i in g.query(q):
    print(i.x)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

#RDFList
print("TASK 7.3 - RDFLib")
for s, p, o in g.triples((None, RDF.type, ns.Person)):
  for s1, p1, o1 in g.triples((s, None, None)):
    print(s1, p1, o1)

for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
  for s1, _, _ in g.triples((None, RDF.type, s)):
      for s2, p2, o2 in g.triples((s1, None, None)):
        print(s2, p2, o2)

#SPARQL
print("TASK 7.3 - SPARQL")
from rdflib.plugins.sparql import prepareQuery
q = prepareQuery('''
  SELECT ?s ?p ?o 
  WHERE {{?s rdf:type ns:Person.
          ?s ?p ?o } UNION 
        {?sc rdfs:subClassOf ns:Person. 
         ?s rdf:type ?sc.
         ?s ?p ?o}}''', 
  initNs = {'rdf':RDF, 'ns':ns, 'rdfs':RDFS} )

for i in g.query(q):
    print(i.s, i.p, i.o)
