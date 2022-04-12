import os
from tqdm import tqdm

def create_data_lookup_map(dir):
  chunk_dirs = [f for f in os.listdir(dir) if f.startswith("chunk")]
  lookup_map = {
      "train": {},
      "val": {},
      "test": {}
  }
  for chunk in tqdm(chunk_dirs):
    for split in lookup_map.keys():
      split_dir = os.path.join(
        dir, 
        chunk, 
        "finished_files_openie_3",
        split
      )
      if os.path.isdir(split_dir):
        for filename in os.listdir(split_dir):
          lookup_map[split][filename] = chunk

  return lookup_map