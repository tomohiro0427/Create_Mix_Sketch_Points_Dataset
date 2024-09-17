import shutil
import os
from pathlib import Path
# tqdm で進捗を表示
from tqdm import tqdm

# コピー元とコピー先のパスを定義
copy_folder = '../Dataset/Mix_Sketch_PointCloud_dataset/'
base_folder = '../Dataset/Random_pyrender_unet/'

# base_folder pathlib
base_folder_path = Path(base_folder)
copy_folder_path = Path(copy_folder)

# base_folder_pathのなかでfix_sketch.pngを持つフォルダを取得 pathlib
fix_sketch_folder = list(base_folder_path.glob('**/fix_sketch.png'))



for view_folder in tqdm(fix_sketch_folder):
    base_data_folder = view_folder.parent
    copy_data_folder = Path(*view_folder.parts[-6:-1])
    copy_dir_path = copy_folder_path / copy_data_folder
    
    
    if not copy_dir_path.parent.exists():
        raise FileNotFoundError(f"フォルダが存在しません: {copy_dir_path.parent}")
    

    #保存場所の作成
    os.makedirs(copy_dir_path, exist_ok=True)

    # ディレクトリ全体をコピー
    shutil.copytree(base_data_folder, copy_dir_path, dirs_exist_ok=True)  # ここでcopytreeを使用





