#!/bin/sh
DIRECTORY=$HOME/dev/projects/barrios/server/barrios/media/seed-data
OUTPUT_DIR=$HOME/dev/projects/barrios/server/barrios/media/seed-data/tables

for f in "$DIRECTORY"/*.csv; do
  name="${f##*/}"
  name="${name%.*}"
  
  header=$(pandoc -t gfm --from csv "$f" | head -n 1)
  divider=$(echo "$header" | sed -E 's/[^|]/-/g')

  echo "## $name" > "$OUTPUT_DIR/$name.md"
  echo >> "$OUTPUT_DIR/$name.md"
  echo "$header" >> "$OUTPUT_DIR/$name.md"
  echo "$divider" >> "$OUTPUT_DIR/$name.md"
  echo >> "$OUTPUT_DIR/$name.md"  
done
```