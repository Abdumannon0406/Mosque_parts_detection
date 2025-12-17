from pathlib import Path
import os,shutil

val_labels=list(Path("Mosque_parts_detection/labels/val").glob("*"))
train_labels=list(Path("Mosque_parts_detection/labels/train").glob("*"))
val_images=list(Path("Mosque_parts_detection/images/val").glob("*"))
train_images=list(Path("Mosque_parts_detection/images/train").glob("*"))

val_stem=[]
train_stem=[]

for path in val_labels:
    val_stem.append(path.stem)
for path in train_labels:
    train_stem.append(path.stem)

for path in train_images:
    if path.stem not in train_stem:
        open(f'Mosque_parts_detection/labels/train/{path.stem}.txt','w').close()

for path in val_images:
    if path.stem not in val_stem:
        open(f'Mosque_parts_detection/labels/val/{path.stem}.txt','w').close()