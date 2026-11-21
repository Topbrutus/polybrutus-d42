# Polybrutus 42D — Exact 47-point Euclidean metric and a 36-fold ideal graph mode

**Scientific author and responsibility:** Gabriel St-Pierre, independent researcher.  
**Material AI assistance:** OpenAI ChatGPT (Astra) materially assisted exact mathematics, two separate verification implementations, scientific preprint and publication. AI is not a scientific author.

## Exact results at R=1

- **47 labelled norm-one points**, **1,081 unordered labelled squared-distance pairs**, minimal affine Euclidean realization dimension **42**.
- **1,035/1,035** parent squared-distance values preserved with pair labels from the immutable [Polybrutus D41 scientific tag](https://github.com/Topbrutus/polybrutus-d41/tree/v0.1.0), source commit `17cc53498fd96d2e50fbdfa63df6705a4c062299`, [DOI 10.5281/zenodo.24414346](https://doi.org/10.5281/zenodo.24414346).
- One new perpendicular norm-one vertex contributes **46** new squared distances all equal to `2R²`.
- Histogram of exact normalized squared distances `k=4d²/R²`: `{4:6,7:2,8:1050,9:3,10:10,12:6,13:2,16:2}`. Exact sum of pair squared distances at R=1 **8695/4**.
- The complete Euclidean centered rational Gram matrix is positive semidefinite with exact rank **42**.
- For one **separately stipulated ideal complete weighted graph** with scalar unit masses and symmetric weights `w_ij=R²/d_ij²`, graph Laplacian eigenvalue **47/2** has multiplicity **36** and eigenvalue **23** has multiplicity **4**. These are *dimensionless model eigenvalues*, not measured physical frequencies.
- Two differently implemented exact-rational verifiers check all 1,081 labelled pairs, all 1,035 frozen parent labels, Euclidean and ideal graph ranks; **4/4** principal adversarial controls pass.

## Reproduce

```bash
python -m pip install sympy==1.14.0
python src/verify_d42.py
python tests/independent_d42.py
```

Both scripts emit identical SHA-256 for deterministic `results/certificate_d42.json`.

**Important lineage packaging change:** The complete immutable D41 scientific tag, including all its ancestors, is included **byte-for-byte** as `prior/d41/frozen_scientific_tag_v0.1.0.zip` (SHA-256 `d1abebf926052caaf171ecb19a81e23ac45926ae8686a87e42a5cf2a2bfc039e`; 494 ZIP entries). Its original `results/certificate_d41.json` is also extracted as `prior/d41/results/certificate_d41.json`, verified byte-identical to the ZIP entry. This avoids the Windows MAX_PATH failure of deeply recursively expanded `prior/` directories, without omitting or changing any ancestor source. See [archive provenance](prior/d41/ARCHIVE_PROVENANCE.md). There are no Git submodules or nested repositories.

## Official DOI and verified public release

- **Official DOI:** [10.5281/zenodo.24414577](https://doi.org/10.5281/zenodo.24414577).
- **Public Zenodo record:** https://zenodo.org/records/24414577, all 3 public files checked for exact sizes and MD5 against the original bytes.
- **Frozen science tag:** [v0.1.0](https://github.com/Topbrutus/polybrutus-d42/tree/v0.1.0), source commit `cba477c53ccdadaed888730ee0d3d25504eeff10`.
- **Tag CI:** [GitHub Actions 44883938805](https://github.com/Topbrutus/polybrutus-d42/actions/runs/44883938805), success.
- **Durable Memoria checkpoint:** https://github.com/Topbrutus/topbrutus_one/blob/main/memoria/checkpoints/POLYBRUTUS_D42_PUBLICATION_2026-11-21.md .
- **Publications registry:** https://github.com/Topbrutus/topbrutus_one/blob/main/memoria/projects/POLYBRUTUS_X72_PUBLICATIONS_INDEX.md .

## Scientific materials

- [Exact specification](SPECIFICATION_D42.md); [constructive proof and negative controls](PREUVE_D42.md); [provenance and scientific limits](PROVENANCE.md).
- [Scientific PDF preprint](publication/POLYBRUTUS_42D_NOTE.pdf); [Markdown manuscript](publication/POLYBRUTUS_42D_NOTE.md); [complete 1,081-pair exact certificate](results/certificate_d42.json).

**Scientific limits:** This is a single reproducible synthetic mathematical metric and a separately chosen ideal graph using established orthogonal Euclidean extensions and uniform graph joins. It does **not** establish additional physical spacetime dimensions, measured resonances, particle discoveries, a novel universal theorem or independent human peer review.

**Licenses:** software MIT; scientific preprint CC BY 4.0.
