# Polybrutus 42D — Exact rational Euclidean labelled squared-distance metric

## Immutable scientific parent and reproducible archive

The frozen scientific predecessor is `Topbrutus/polybrutus-d41@v0.1.0`, source commit `17cc53498fd96d2e50fbdfa63df6705a4c062299`, DOI `10.5281/zenodo.24414346`, original certificate SHA-256 `3f54bb52de47909707f85c134fcbba53c22137cb7c0d0321486500562c98e91a`, comprising 46 norm-one points and 1,035 labelled squared distances.

The **complete original scientific source and all ancestors** are archived as an immutable Git tag ZIP at `prior/d41/frozen_scientific_tag_v0.1.0.zip`; SHA-256 `d1abebf926052caaf171ecb19a81e23ac45926ae8686a87e42a5cf2a2bfc039e`; 494 entries, valid CRC. To run checkers without expanding Windows paths, an exact byte copy of the parent's certificate is placed at `prior/d41/results/certificate_d41.json`. Both checkers verify the full ZIP's hash, CRC, extracted entry equality and certificate's SHA-256. No original source, tag, DOI, repository, or prior release was modified.

## Explicit Euclidean construction

Embed all 46 predecessor norm-one vertices as `q_i=(p_i,0)`, then append one perpendicular norm-one unit vector `q47=e43` in one additional coordinate. All `C(46,2)=1035` old pairwise squared distances retain their original labels and rational values. Each new pair satisfies `||q47-q_i||²=1+1-2<q47,q_i>=2`, yielding `46` new pairs, so `C(47,2)=1081` labelled unordered pairs.

The seven original canonical norm-one points form a rational rank-three Gram block with entries `3*x_i*x_j+y_i*y_j+z_i*z_j`. Five centered regular-simplex unit points form an independent rank-four Gram block with unit diagonal and off-diagonal inner products `-1/4`. Thirty-five additional mutually orthogonal unit coordinate directions are perpendicular to both. The full rational Gram `G` is PSD by construction, has unit diagonal and exact rank `3+4+35=42`.

For the full labelled squared-distance matrix set `D_ii=0`, `D_ij=2-2G_ij` for each unordered pair. With centering projector `H=I-11ᵀ/47`, the unique Euclidean centered Gram is `B=-(1/2)HDH=HGH`, of exact rational rank **42**. The original two antipodal points place the origin in their affine span. Consequently the minimum Euclidean affine realization dimension of this **particular complete labelled metric** is exactly **42**, not merely the number of stored coordinates.

## Exact invariants, R=1

```text
Norm-one labelled vertices                  47
Unordered labelled squared-distance pairs  1081
Frozen predecessor pair labels preserved   1035/1035
New squared-distance pairs                 46 × 2
Histogram k=4*d²/R²                        4:6  7:2  8:1050  9:3  10:10  12:6  13:2  16:2
Sum of all squared distances at R=1        8695/4
Minimum affine/centered Gram rank          42
Ambient storage coordinates                43
```

## Separately stipulated ideal complete graph

For scalar unit masses and symmetric edge weights `w_ij=R²/d_ij²`, the appended unit vertex connects to each of the 46 parent vertices with edge weight 1/2. Its weighted Laplacian is

```text
L42 = [ L41 + I46/2       -1_46/2 ]
      [ -1_46ᵀ/2               23 ].
```

The uniform-join recurrence is `chi47(z)=z(z-47/2)chi46(z-1/2)/(z-1/2)`. With `f6(z)=chi_P7(z)/z` the original seven-point nonzero factor, the closed model expression is `chi47(z)=z(z-47/2)^36(z-23)^4*f6(z-20)`. Both independent rational rank calculations confirm `nullity(L42-(47/2)I)=36` and `nullity(L42-23I)=4`.

These are dimensionless chosen-model eigenmodes, not measured hertz.
