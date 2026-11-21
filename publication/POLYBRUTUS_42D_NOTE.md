# Polybrutus 42D: Exact 47-point Euclidean distance geometry and a thirty-sixfold ideal graph mode

**Gabriel St-Pierre** — Independent researcher  
**21 November 2026**  
**Exact mathematical case study / scientific preprint**  
**Material AI assistance:** OpenAI ChatGPT (Astra) helped exact rational computation, two separately implemented verifiers, scientific writing and controlled publication. AI is not a scientific author.

## Abstract

An exact Euclidean labelled squared-distance metric on 47 unit vertices is constructed by conservatively adjoining one perpendicular unit point to frozen Polybrutus 41D. Every one of 1,035 predecessor labelled squared distances is preserved. A new perpendicular unit point adds 46 squared distances equal to 2 at unit radius, giving 1,081 unordered labelled pairs. The exact rational centered Euclidean Gram is positive semidefinite of rank 42, establishing minimum affine realization dimension 42 for this particular metric. A separately stipulated ideal complete weighted graph with unit scalar masses and edge weights w_ij=1/d_ij² has graph Laplacian eigenvalue 47/2 of multiplicity 36 and eigenvalue 23 of multiplicity 4. Two separate exact-rational programs verify all labelled pairs, predecessor conservation, Euclidean ranks and ideal graph eigenspaces. These dimensionless mathematical statements do not establish extra physical spacetime dimensions or experimentally observed resonances.

## 1. Immutable parent and compressed preservation of the full scientific lineage

The sole scientific parent is Topbrutus/polybrutus-d41 at immutable tag v0.1.0, source commit 17cc53498fd96d2e50fbdfa63df6705a4c062299, DOI 10.5281/zenodo.24414346. Its original exact certificate contains 46 norm-one points and 1,035 unordered labelled squared distances; SHA-256 3f54bb52de47909707f85c134fcbba53c22137cb7c0d0321486500562c98e91a.

Because expanding many generations of nested predecessor directories exceeded Windows maximum path length, the complete frozen D41 tag including all ancestral sources is preserved, not modified, as prior/d41/frozen_scientific_tag_v0.1.0.zip. This exact Git archive has 494 entries, valid CRC and SHA-256 d1abebf926052caaf171ecb19a81e23ac45926ae8686a87e42a5cf2a2bfc039e. The predecessor certificate is copied byte-identically from the ZIP to prior/d41/results/certificate_d41.json for direct verification. Both independent programs check the ZIP and certificate integrity. All preceding tags and DOI remain unchanged.

For each predecessor unit vector p_i, i=1,...,46, embed q_i=(p_i,0) in one more coordinate and append perpendicular unit vertex q47=e43. Every inherited scalar product and labelled pair distance is preserved. By orthogonality ||q47-q_i||²=||q47||²+||q_i||²-2<q47,q_i>=2. Hence C(47,2)=1081=1035+46 exact unordered labelled squared distances.

## 2. Exact rational Gram and minimal Euclidean affine dimension

Seven canonical norm-one points form a rational rank-three Gram block with inner products 3*x_i*x_j+y_i*y_j+z_i*z_j. Five centered regular-simplex norm-one points form an independent rank-four block with unit diagonal and off-diagonal products -1/4. Thirty-five additional mutually perpendicular unit coordinate vectors are orthogonal to both blocks. Thus the 47-by-47 rational Gram G is positive semidefinite with unit diagonal and exact rank 3+4+35=42.

For the complete labelled squared-distance matrix set D_ii=0 and D_ij=2-2G_ij. Let H=I-(1/47)11^T be the centering projector. The uniquely determined Euclidean centered Gram B=-(1/2)HDH=HGH has exact rational rank 42. Two original canonical points are antipodal, so the origin is in their affine span. Every Euclidean realization of this complete labelled metric has the same centered Gram rank; therefore the minimum affine realization dimension is exactly 42.

## 3. Complete labelled squared-distance invariants

With R=1 let the normalized class index be k=4d²/R². There are exactly eight classes: k=4 six times, k=7 twice, k=8 1,050 times, k=9 three times, k=10 ten times, k=12 six times, k=13 twice, and k=16 twice. Their counts total 1,081. The sum of all unordered squared pair distances is exactly 8695/4.

Each original predecessor pair label is explicitly checked against the authenticated 41D certificate. Matching histograms would not suffice because a permutation of labels changes correspondence without changing an unlabeled distribution. A deliberately incorrect label permutation is rejected.

## 4. Separately stipulated ideal complete weighted graph

Independently stipulate a complete weighted graph with scalar unit masses and symmetric edge weights w_ij=1/d_ij². The newly appended perpendicular point connects to all 46 older vertices with uniform weight 1/2, producing weighted Laplacian

L42 = [ L41 + (1/2)I46         -(1/2)1_46 ]
      [ -(1/2)1_46^T                  23 ].

Its characteristic polynomial satisfies the exact uniform-join recurrence chi47(z)=z(z-47/2)chi46(z-1/2)/(z-1/2). With f6(z)=chi_P7(z)/z the inherited nonzero original seven-point graph factor, the closed model expression is chi47(z)=z(z-47/2)^36(z-23)^4*f6(z-20).

Two separate exact rational matrix rank computations establish nullity(L42-(47/2)I)=36 and nullity(L42-23I)=4. These are dimensionless chosen-model eigenspaces, not experimentally measured frequencies, particle excitations, acoustic resonance or a claim about physical spacetime.

## 5. Independent verification and falsification controls

The primary src/verify_d42.py computes the full exact rational Gram and all 1,081 labelled squared distances, independently authenticates the frozen parent ZIP and certificate SHA-256, and verifies full label conservation, centered Gram rank and chosen model eigenspaces. Four negative cases are rejected: corrupted pair distance, duplicated vertex, nonorthogonal tilt and histogram-preserving relabelling.

Separately, tests/independent_d42.py calculates all 1,081 labelled squared distances using Python fractions.Fraction structural rules, without importing the primary Gram generator. It independently validates the original archive checksum and certificate-entry equality, all 1,035 predecessor labels, 1,081 present labels, Euclidean ranks and ideal graph nullities. Both programs output identical deterministic SHA-256 for results/certificate_d42.json. Public GitHub Actions reruns both and checks byte determinism, archived source SHA and predecessor certificate SHA.

To reproduce: Python with sympy==1.14.0; run python src/verify_d42.py and python tests/independent_d42.py. The entire immutable D41 tag and earlier ancestors are in the frozen ZIP under prior/d41/.

## 6. Scientific limits and references

Perpendicular extensions of Euclidean point configurations and uniform joins of weighted graphs are established mathematical techniques. This reports one reproducible synthetic labelled metric and a separately chosen ideal graph, not a new universal theorem or experimental proof of 42 physical dimensions. No observed particles, measured resonances or independent human peer review is claimed.

References: Gabriel St-Pierre, Polybrutus 41D (2026), DOI 10.5281/zenodo.24414346; scientific source github.com/Topbrutus/polybrutus-d41 tag v0.1.0; original seven-point geometry github.com/Topbrutus/polybrutus.
