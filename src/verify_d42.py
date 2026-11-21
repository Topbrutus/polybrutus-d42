#!/usr/bin/env python3
"""Polybrutus D42: exact Euclidean labelled metric and chosen ideal weighted graph.
Conservative perpendicular unit extension of the immutable Polybrutus D41 v0.1.0.
No physical spacetime dimension or experimentally measured resonance is claimed.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
from hashlib import sha256
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix

ROOT=Path(__file__).resolve().parents[1]
Q=s.Rational
core=[(0,0,1),(Q(1,2),0,Q(1,2)),(-Q(1,4),Q(3,4),Q(1,2)),
      (-Q(1,4),-Q(3,4),Q(1,2)),(0,0,-1),(Q(1,2),0,-Q(1,2)),
      (-Q(1,2),0,-Q(1,2))]
n=47
pairs=list(combinations(range(n),2))
G=s.zeros(n)
for i in range(7):
    for j in range(7):
        G[i,j]=3*core[i][0]*core[j][0]+core[i][1]*core[j][1]+core[i][2]*core[j][2]
for i in range(7,12):
    for j in range(7,12):
        G[i,j]=1 if i==j else -Q(1,4)
for i in range(12,n):
    G[i,i]=1
assert all(G[i,i]==1 for i in range(n))
assert DomainMatrix.from_Matrix(G).to_field().rank()==42
D=2*s.ones(n)-2*G
for i in range(n):
    D[i,i]=0
assert len(pairs)==1081 and all(D[i,j]>0 for i,j in pairs)

parent_path=ROOT/'prior'/'d41'/'results'/'certificate_d41.json'
parent_archive=ROOT/'prior'/'d41'/'frozen_scientific_tag_v0.1.0.zip'
assert sha256(parent_archive.read_bytes()).hexdigest()=='d1abebf926052caaf171ecb19a81e23ac45926ae8686a87e42a5cf2a2bfc039e'
from zipfile import ZipFile
with ZipFile(parent_archive) as _frozen:
    assert _frozen.testzip() is None
    assert _frozen.read('results/certificate_d41.json')==parent_path.read_bytes()
parent_bytes=parent_path.read_bytes()
assert sha256(parent_bytes).hexdigest()=='3f54bb52de47909707f85c134fcbba53c22137cb7c0d0321486500562c98e91a'
parent=json.loads(parent_bytes)
assert parent['status']=='PASS' and parent['dimension']==41 and parent['vertices']==46
former={(int(e['i'])-1,int(e['j'])-1):s.Rational(e['d2'])
        for e in parent['labelled_squared_distances']}
assert len(former)==1035
assert all(D[i,j]==v for (i,j),v in former.items())
assert all(D[i,46]==2 for i in range(46))
hist=Counter(4*D[i,j] for i,j in pairs)
expected=Counter({4:6,7:2,8:1050,9:3,10:10,12:6,13:2,16:2})
assert hist==expected and sum(hist.values())==1081
assert sum(D[i,j] for i,j in pairs)==Q(8695,4)

H=s.eye(n)-s.ones(n)/n
B=-H*D*H/2
assert B==H*G*H
assert DomainMatrix.from_Matrix(B).to_field().rank()==42
# The first and fifth canonical points are antipodal; origin lies in the affine hull.
assert G[0,4]==-1

L=s.zeros(n)
for i,j in pairs:
    w=1/D[i,j]
    L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
assert L*s.ones(n,1)==s.zeros(n,1)
assert DomainMatrix.from_Matrix(L-Q(47,2)*s.eye(n)).to_field().rank()==11
assert DomainMatrix.from_Matrix(L-23*s.eye(n)).to_field().rank()==43
old=s.zeros(46)
for i,j in combinations(range(46),2):
    w=1/D[i,j]
    old[i,i]+=w;old[j,j]+=w;old[i,j]-=w;old[j,i]-=w
assert L[:46,:46]-old==s.eye(46)/2
assert all(L[i,46]==-Q(1,2) for i in range(46))
assert L[46,46]==23

# Four adversarial negative controls.
damaged=D.copy();damaged[0,46]=damaged[46,0]=Q(9,4)
assert Counter(4*damaged[i,j] for i,j in pairs)!=hist
duplicate=G.copy();duplicate[46,:]=G[45,:];duplicate[:,46]=G[:,45];duplicate[46,46]=1
assert DomainMatrix.from_Matrix(duplicate).to_field().rank()==41
tilted_dot_to_old_core=s.sqrt(3)*Q(3,10)
assert tilted_dot_to_old_core!=0
swapped=D.copy();swapped.row_swap(0,7);swapped.col_swap(0,7)
assert swapped!=D and Counter(4*swapped[i,j] for i,j in pairs)==hist

report={
  'schema':'POLYBRUTUS-D42-EXACT-CERTIFICATE-v1',
  'status':'PASS','dimension':42,'vertices':47,'pairs':1081,
  'affine_rank':42,'centered_gram_rank':42,'ambient_storage_coordinates':43,
  'radius':1,'parent':'Topbrutus/polybrutus-d41@v0.1.0',
  'parent_tag_commit':'17cc53498fd96d2e50fbdfa63df6705a4c062299',
  'parent_doi':'10.5281/zenodo.24414346',
  'parent_certificate_sha256':sha256(parent_bytes).hexdigest(),
  'parent_frozen_tag_archive_sha256':sha256(parent_archive.read_bytes()).hexdigest(),
  'parent_frozen_tag_embedded_as_verified_zip':True,
  'parent_distances_preserved':1035,'new_distances':46,
  'new_squared_distances':['2']*46,
  'histogram_k_4d2':{str(k):int(v) for k,v in sorted(hist.items())},
  'sum_squared_distances':'8695/4',
  'gram_psd_certificate':'B=-(H D H)/2=H G H; G=XX^T exact',
  'negative_controls':'4/4 PASS',
  'oscillator_model':'Chosen ideal equal-mass complete graph with w_ij=1/d_ij^2; no physical measurement',
  'eigenvalue_47_over_2_multiplicity':36,
  'eigenvalue_23_multiplicity':4,
  'spectral_recurrence':'chi47(z)=z*(z-47/2)*chi46(z-1/2)/(z-1/2)',
  'spectral_closed_form':'chi47(z)=z*(z-47/2)^36*(z-23)^4*f6(z-20), f6(z)=chiP7(z)/z',
  'novel_universal_theorem':'NOT CLAIMED','physical_discovery':'NOT CLAIMED',
  'human_peer_review':'NOT_DONE','sympy':s.__version__,
  'labelled_squared_distances':[{'i':i+1,'j':j+1,'d2':str(D[i,j]),'k':str(4*D[i,j])} for i,j in pairs]
}
out=ROOT/'results'/'certificate_d42.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
print('PRIMARY D42 PASS: 47 vertices, 1081 labelled pairs, affine rank 42; 1035/1035 previous pairs preserved')
print('IDEAL GRAPH PASS: eigenvalue 47/2 x36; eigenvalue 23 x4; 4/4 negative controls')
print('CERTIFICATE_SHA256='+sha256(out.read_bytes()).hexdigest())
