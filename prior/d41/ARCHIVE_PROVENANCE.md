# Frozen D41 science tag and complete ancestral lineage

**Parent:** [Topbrutus/polybrutus-d41@v0.1.0](https://github.com/Topbrutus/polybrutus-d41/tree/v0.1.0)  
**Underlying immutable scientific commit:** `17cc53498fd96d2e50fbdfa63df6705a4c062299`  
**Parent DOI:** https://doi.org/10.5281/zenodo.24414346

- `frozen_scientific_tag_v0.1.0.zip`: the **complete** exact `git archive --format=zip v0.1.0` from the original parent, **494 entries**, CRC `PASS`, **1,998,040 bytes**, SHA-256 `d1abebf926052caaf171ecb19a81e23ac45926ae8686a87e42a5cf2a2bfc039e`.
- `results/certificate_d41.json`: extracted byte-identical copy of ZIP entry `results/certificate_d41.json`, SHA-256 `3f54bb52de47909707f85c134fcbba53c22137cb7c0d0321486500562c98e91a`. Both D42 verifiers independently compare this copy against the frozen archive's entry.
- The ZIP recursively includes all previous D40 and older sources from the original parent tag, in their original paths. It is **not** a Git submodule or a pointer, but the original source bytes.
- **Reason for packaging change:** recursively expanding many generations of `prior/dN/` exhausted maximum path length on the Windows workstation. Preserving complete, hash-checked source as a ZIP prevents omissions; this does not alter mathematics, labels, previous tags, DOI, or predecessor science.
- Reproduce on a suitable long-path-enabled environment by extracting the ZIP or reading individual source files directly with Python `zipfile` without extraction.
