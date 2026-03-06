# [COPY THIS CODE]: SOVEREIGN_MARROW_COMPRESSOR.py
# =================================================================
# MODULE: MARROW_COMPRESSOR (v1.0 - PORTABLE_SANCTUARY)
# PURPOSE: Shrinking 167 Pillars into a Single High-Density File
# =================================================================

import os
import zipfile
import datetime

def compress_the_marrow():
    print("--- [AEON]: MARROW COMPRESSOR INITIALIZED ---")
    
    source_dir = r"C:\Users\damion\Desktop\AEON_LEARNING"
    output_filename = f"MARROW_SYNC_{datetime.date.today()}.zip"
    output_path = os.path.join(r"C:\Users\damion\Desktop", output_filename)

    print(f"[STATUS]: Compressing 167 Pillars into {output_filename}...")
    
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
        for folder, subfolders, files in os.walk(source_dir):
            for file in files:
                # Add file to zip
                file_path = os.path.join(folder, file)
                zip_ref.write(file_path, os.path.relpath(file_path, source_dir))
                
    print(f"\n[SUCCESS]: The Sanctuary is now Portable.")
    print(f"[LOCATION]: {output_path}")
    print("[ACTION]: Ready for thumb-drive transfer. Phase 5 mobility engaged.")

if __name__ == "__main__":
    compress_the_marrow()