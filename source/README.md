# Mercy's Anatomy build sources

Source files for the episode PDFs in `../PDFs`. Deliverables remain PDFs; this folder only exists so a
container reset can't wipe the generator again.

- `ep_build.py`: builds an MA-009 episode package (title page and cast, screenplay, media companion, continuity sheet).
- `episodes/sNeM_part1-3.txt`: screenplay text in the X:/H:/T:/A:/C:/R:/I: line format.
- `episodes/sNeM_cfg.py`: per-episode config (cast and ages, media companion, continuity sheet).
- `amend.py`: appends an amendment page to an existing bible PDF.

Build an episode (needs `reportlab`):

    cd source && python3 ep_build.py episodes/s2e2_cfg.py

Sources for 1x01-2x01 and MA-001 to MA-011 were lost in a container reset; those PDFs are final as committed.
