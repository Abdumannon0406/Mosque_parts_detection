from pathlib import Path
import os,shutil

# val_labels=list(Path("Mosque_parts_detection/labels/val").glob("*"))
train_labels=list(Path("Mosque_parts_detection/labels/train").glob("*"))
val_images=list(Path("Mosque_parts_detection/images/val").glob("*"))
train_images=list(Path("Mosque_parts_detection/images/train").glob("*"))

val_labels='Mosque_parts_detection/labels/val'

os.makedirs(val_labels,exist_ok=True)

val_stem=[]
train_stem=[]

for path in val_images:
    val_stem.append(path.stem)
for path in train_images:
    train_stem.append(path.stem)

for path in train_labels:
    if path.stem in val_stem:
        shutil.move(path,val_labels)