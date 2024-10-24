import kagglehub
import os
import shutil

data_dir = os.path.join(os.getcwd(), "data")
os.makedirs(data_dir, exist_ok=True)

original_path = kagglehub.dataset_download("rodolfomendes/abalone-dataset")

for file in os.listdir(original_path):
    src_file = os.path.join(original_path, file)
    dst_file = os.path.join(data_dir, file)
    shutil.copy2(src_file, dst_file)

print(f"Dataset downloaded and moved to: {data_dir}")
print("\nContents of the data directory:")
for file in os.listdir(data_dir):
    print(f"- {file}")