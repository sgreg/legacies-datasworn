#!/usr/bin/env python3
#
# Prints Markdown content listing all the moves and oracles Datasworn IDs
# of a given Datasworn JSON file. Creates either a list of links in form
# `[Name](datsworn:id)`, or just the id itself, depending on the optional
# second parameter (defaults to links).
#
# Note that this requires the datasworn Python package
#   https://github.com/tbsvttr/datasworn/tree/main/pkg/python
# which at least I had to rebuild locally to make it work.
#

import os
import sys
import json
from datetime import datetime

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <input file> [links|ids]", file=sys.stderr)
    sys.exit(1)

filename = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else "links"

with open(filename, "r", encoding="utf-8") as f:
    data = json.load(f)

from datasworn.core.models import Expansion

ruleset = Expansion.model_validate(data)


def dsprint(name: str, dsid: str):
    if mode == "links":
        print(f"[{name}](datasworn:{dsid})  ")
    elif mode == "ids":
        print(f"{dsid}  ")


print(f"""# Ironsworn: Legacies Datasworn IDs

Generated from {os.path.basename(filename)} on {datetime.now().ctime()}

## Moves
""")
for category in ruleset.moves.values():
    for move in category.contents.values():
        dsprint(f"{category.name} / {move.name}", move._id)

print("""
## Oracles
""")
for oracle in ruleset.oracles.values():
    for key, content in oracle.contents.items():
        dsprint(f"{oracle.name} / {content.name}", content._id)
    for collection in oracle.collections.values():
        for key, content in collection.contents.items():
            dsprint(f"{oracle.name} / {collection.name} / {content["name"]}", content["_id"])
            if key in collection.collections:
                for subcollection in collection.collections.values():
                    for subcontent in subcollection["contents"].values():
                        dsprint(f"{oracle.name} / {collection.name} / {subcollection["name"]} / {subcontent["name"]}", subcontent["_id"])
