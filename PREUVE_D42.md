# Polybrutus D42 — Constructive proof, two exact verifiers and negative controls

**Immutable scientific parent:** `Topbrutus/polybrutus-d41@v0.1.0`, source commit `17cc53498fd96d2e50fbdfa63df6705a4c062299`, DOI `10.5281/zenodo.24414346`, certificate SHA-256 `3f54bb52de47909707f85c134fcbba53c22137cb7c0d0321486500562c98e91a`.

**Frozen archive integrity.** Full original D41 scientific tag and ancestors reside inside `prior/d41/frozen_scientific_tag_v0.1.0.zip` (SHA-256 `d1abebf926052caaf171ecb19a81e23ac45926ae8686a87e42a5cf2a2bfc039e`). 494 archive entries, CRC checked. Original certificate is extracted byte-identically to `prior/d41/results/certificate_d41.json`. Both separate verifiers enforce ZIP SHA-256, CRC and certificate-entry match.

**Exact conservation.** Embed each parent point with a zero coordinate, conserving all **1,035** predecessor labelled squared distances. Append a perpendicular norm-one point with squared distance `2R²` to each old point. Exactly **1,081 = C(47,2) = 1,035 + 46** pairs result.

**PSD and minimum Euclidean realization dimension.** Explicit rational Gram has canonical seven-point block rank 3, centered simplex block rank 4 and 35 perpendicular unit axes. It is PSD by Gram construction, with unit diagonal and rank **42**. Complete labelled metric determines unique centered Euclidean Gram `B=-(1/2)HDH=HGH` with exact rank **42**. The original antipodal pair puts the origin in the affine hull. Therefore the metric cannot be realized in fewer than 42 affine Euclidean dimensions.

**Exhaustive arithmetic.** Histogram `k=4d²/R²`: `{4:6,7:2,8:1050,9:3,10:10,12:6,13:2,16:2}`, totaling 1,081. Exact sum of pair squared distances at R=1 is `8695/4`; 1,035 old distances are compared by original labels, not just histogram.

**Ideal model.** A separately stipulated complete scalar-unit-mass weighted graph `w_ij=1/d_ij²` has Laplacian eigenvalue **47/2** of multiplicity **36**, and **23** of multiplicity **4**, established by exact rational matrix ranks. These modes are dimensionless and not experimental frequencies.

**Independent exact programs.** The primary `src/verify_d42.py` builds exact rational Gram entries, computes all 1,081 pair labels, checks frozen source ZIP and parent SHA, and validates exact Gram and graph ranks. Four adversarial primary controls detect corrupted squared distance, duplicated point, nonperpendicular tilt and histogram-preserving relabelling. The independently implemented `tests/independent_d42.py` calculates every pair via Python `fractions.Fraction` rules **without importing the primary Gram generator** and independently validates the parent archive, all 1,035 labels and rank conditions. Both output identical SHA-256 for deterministic `results/certificate_d42.json`.

**Scientific scope.** Established perpendicular Euclidean embedding and uniform graph joining provide a single synthetic mathematical construction. No new universal theorem, physical spacetime dimension, measured resonance, particle observation or independent human peer review is claimed.
