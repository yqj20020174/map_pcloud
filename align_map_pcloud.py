import json
import os
import sys
from tile_scheme_utils import Tile, MortonCode

dirs_dict = {}
dirs = os.listdir(r"D:\j6e\map-pointcloud\bin")
for _, dir in enumerate(dirs):
    dir_name, _ = os.path.splitext(dir)
    if dir_name not in dirs_dict:
        dirs_dict[dir_name] = dir
        
# with open(r"D:\j6e\map-pointcloud\dirs_dict.json", 'w') as f:
#     json.dump(dirs_dict, f, indent=4)

with open(r"D:\j6e\map-pointcloud\track.json", 'r') as f:
    data = json.load(f)

output_list = []
tile = Tile()

for _, p in enumerate(data):
    record = {}
    
    key = p['cloud_url'].split('.')[0]
    replaced_key = key.replace('PIPELINEV2', 'pipelinev2')
    if replaced_key in dirs_dict:
        point = (float(p['x']), float(p['y']))
        level = 13
        result = tile.get_tile_id_from_point(point, level)
        
        record['x'] = p['x']
        record['y'] = p['y']
        record['cloud_url'] = p['cloud_url']
        record['tile_id'] = result
        
        output_list.append(record)

print(len(output_list))

with open(r"D:\j6e\map-pointcloud\pcloud_tile.json", 'w') as f:
    json.dump(output_list, f, indent=4)


