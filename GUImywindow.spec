# -*- mode: python ; coding: utf-8 -*-

import os

block_cipher = None

# --- 路径和元数据变量 ---
SITE_PACKAGES_PATH = 'C:\\ProgramData\\Anaconda3\\envs\\yolov11\\Lib\\site-packages'
ULTRALYTICS_SRC_PATH = 'E:\\myidea\\v11plus\\ultralytics-yolo11-main\\ultralytics'
TORCH_METADATA_NAME = 'torch-2.2.2+cu121.dist-info'
TORCHVISION_METADATA_NAME = 'torchvision-0.17.2+cu121.dist-info'
TORCHAUDIO_METADATA_NAME = 'torchaudio-2.2.2+cu121.dist-info'

a = Analysis(
    ['GUImywindow.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('./images', 'images'),
        (ULTRALYTICS_SRC_PATH, 'ultralytics'),
        (os.path.join(SITE_PACKAGES_PATH, TORCH_METADATA_NAME), TORCH_METADATA_NAME),
        (os.path.join(SITE_PACKAGES_PATH, TORCHVISION_METADATA_NAME), TORCHVISION_METADATA_NAME),
        (os.path.join(SITE_PACKAGES_PATH, TORCHAUDIO_METADATA_NAME), TORCHAUDIO_METADATA_NAME)
    ],
    
    hiddenimports=[
        # 保持核心依赖
        'ultralytics', 'torch', 'torchvision', 'torchaudio', 'cv2',
        'numpy', 'pandas', 'scipy', 'PIL', 'pydantic', 'mmcv', 'mmengine',
        'sklearn', 'skimage', 'albumentations', 'matplotlib', 'seaborn',
        'tqdm', 'rich', 'grad_cam', 'timm', 'huggingface_hub', 'safetensors',
        'efficientnet_pytorch', # efficientnet_pytorch 仍可能被其他部分需要，暂时保留
        'yaml', 'requests', 'IPython'
    ],
    
    hookspath=[],
    hooksconfig={},
    
    # --- 关键修改：在这里排除不需要的模块 ---
    excludes=[
        'swattention', # 同时也可以明确排除这个
    ],

    runtime_hooks=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz, a.scripts, a.binaries, a.zipfiles, a.datas,
    [], name='LMFAN', debug=False, bootloader_ignore_signals=False,
    strip=False, upx=False, runtime_tmpdir=None,
    console=False,
    icon='./images/physics2.png'
)

coll = COLLECT(
    exe, a.binaries, a.zipfiles, a.datas,
    strip=False, upx=True, upx_exclude=[],
    name='LMFAN'
)